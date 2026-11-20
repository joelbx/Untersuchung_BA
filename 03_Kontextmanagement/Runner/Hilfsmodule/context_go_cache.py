"""Trusted main-module Go prefetch, without traversing unrelated graph modules.

Unlike `go mod download all`, ordinary `go mod download` uses the main module's
dependency set under Go's module-graph pruning rules. No versions or source files
are changed. Reference manifest requirements are checked separately, never code.
"""
import hashlib
import json
from pathlib import Path
import tempfile
import uuid


def download_command(*, offline):
    return ['env', 'GOTOOLCHAIN=local', 'GOFLAGS=', 'GONOPROXY=none', 'GONOSUMDB=none', 'GOPRIVATE=',
            'GOPROXY=off' if offline else 'GOPROXY=https://proxy.golang.org',
            'GOSUMDB=off' if offline else 'GOSUMDB=sum.golang.org',
            'go', 'mod', 'download']


async def warm(core, case, instance, directory):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    inspected = await core.ensure_image('jefzda/sweap-images:' + case['dockerhub_tag'], directory)
    official_id = inspected['Id']
    output = core.DATA / 'dependency-cache-overrides.json'
    overrides = json.loads(output.read_text()) if output.exists() else {}
    existing = overrides.get(case['instance_id'])
    if existing and (existing['official_image_id'] != official_id or existing['base_commit'] != case['base_commit']):
        raise RuntimeError('Dependency cache identity differs')
    source = existing['cached_image_id'] if existing else official_id
    await core.host(['docker', 'image', 'inspect', source])
    patch = core.go_manifest_patch(str(instance.get('patch', '')))
    core.save(directory / 'reference-manifests.patch', patch)
    record = {'at': core.now(), 'policy': 'main-module-download-v1', 'official_image_id': official_id,
              'source_image_id': source, 'download_command': ['go', 'mod', 'download'],
              'manifest_patch_sha256': hashlib.sha256(patch.encode()).hexdigest(),
              'reference_code_applied': False, 'reference_source_executed': False,
              'model_tokens': 0, 'downloads_needed': False}
    cid = None
    commands = []
    scratch = '/tmp/context-go-manifests-' + uuid.uuid4().hex
    originals = set()

    async def command(argv, *, check=True):
        result = await core.host(['docker', 'exec', cid, *argv], timeout=None, check=False)
        commands.append({'command': argv, 'exit_code': result.returncode,
                         'stdout': result.stdout, 'stderr': result.stderr})
        core.save(directory / 'commands.json', commands)
        if check and result.returncode:
            raise RuntimeError('Go main-module preparation failed: ' + result.stderr[-3000:])
        return result

    async def reset():
        await command(['git', '-c', 'core.hooksPath=/dev/null', 'reset', '--hard', case['base_commit']])
        for name in ('go.mod', 'go.sum', 'go.work', 'go.work.sum'):
            if name in originals:
                await command(['cp', '-p', scratch + '/' + name, '/app/' + name])
            else:
                await command(['rm', '-f', '/app/' + name])

    try:
        core.check_storage_reserve()
        cid = (await core.host(['docker', 'run', '-d', '--network', 'bridge', '--cpus', '4',
            '--memory', '8192m', '--name', 'context-go-prefetch-' + uuid.uuid4().hex[:12],
            '--workdir', '/app', '--entrypoint', '/bin/sh', source, '-c', 'exec tail -f /dev/null'])).stdout.strip()
        await command(['git', '-c', 'core.hooksPath=/dev/null', 'reset', '--hard', case['base_commit']])
        before = (await command(['git', 'write-tree'])).stdout.strip()
        await command(['mkdir', '-p', scratch])
        for name in ('go.mod', 'go.sum', 'go.work', 'go.work.sum'):
            if (await command(['test', '-f', '/app/' + name], check=False)).returncode == 0:
                originals.add(name)
                await command(['cp', '-p', '/app/' + name, scratch + '/' + name])
        if patch:
            with tempfile.TemporaryDirectory(prefix='context-manifests-') as tmp:
                path = Path(tmp) / 'manifests.patch'
                path.write_text(patch)
                await core.host(['docker', 'cp', str(path), cid + ':' + scratch + '/manifests.patch'])
        for phase in (('base', 'reference') if patch else ('base',)):
            await reset()
            if phase == 'reference':
                await command(['git', 'apply', '--include=go.mod', '--include=go.sum', scratch + '/manifests.patch'])
            probe = await command(download_command(offline=True), check=False)
            if probe.returncode:
                record['downloads_needed'] = True
                await reset()
                if phase == 'reference':
                    await command(['git', 'apply', '--include=go.mod', '--include=go.sum', scratch + '/manifests.patch'])
                await command(download_command(offline=False))
                await command(download_command(offline=True))
        await reset()
        await command(['rm', '-rf', scratch])
        after = (await command(['git', 'write-tree'])).stdout.strip()
        if before != after:
            raise RuntimeError('Prefetch altered canonical source')
        await command(['git', 'diff', '--exit-code', case['base_commit']])
        cached = source
        if record['downloads_needed']:
            core.check_storage_reserve()
            cached = (await core.host(['docker', 'commit', cid], timeout=300)).stdout.strip()
            overrides[case['instance_id']] = {'official_image_id': official_id, 'cached_image_id': cached,
                'base_commit': case['base_commit'], 'canonical_tree': before,
                'dataset_sha256': core.sha(core.DATA / 'swebench_pro_verified.jsonl'),
                'at': core.now(), 'dependency_kind': 'go-main-module-cache', 'model_tokens': 0,
                'reference_code_applied': False, 'reference_source_executed': False}
            core.save(output, overrides)
        record.update(completed=True, completed_at=core.now(), cached_image_id=cached, canonical_tree=before)
        core.save(directory / 'prefetch.json', record)
        return record
    except BaseException as error:
        record.update(completed=False, error=core.redact(str(error)))
        core.save(directory / 'prefetch.json', record)
        raise
    finally:
        if cid:
            await core.host(['docker', 'rm', '-f', cid], check=False)
