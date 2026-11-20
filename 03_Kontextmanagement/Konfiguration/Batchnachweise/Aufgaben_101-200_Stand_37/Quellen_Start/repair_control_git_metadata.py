#!/usr/bin/env python3
"""Restore missing Git objects from the exact public base commit, without changing source.

Trusted pre-model environment repair only. No reference patches, tests, or model calls.
The unchanged working tree must match the fetched canonical commit before an overlay
is registered. Existing official images remain pinned and untouched.
"""
import argparse
import asyncio
import json
import re
import shlex
import uuid
from pathlib import Path
import run as runner


async def repair(numbers, stage_only=False):
    selection = json.loads((runner.LAB / 'selection-extended.json').read_text())
    if runner.sha(runner.DATA / 'swebench_pro_verified.jsonl') != selection['dataset_sha256']:
        raise RuntimeError('Dataset hash mismatch')
    rows = {d['instance_id']: d for d in map(json.loads, (runner.DATA / 'swebench_pro_verified.jsonl').read_text().splitlines())}
    output = runner.DATA / 'dependency-cache-overrides.json'
    overrides = json.loads(output.read_text()) if output.exists() else {}
    for number in numbers:
        case = selection['scored_tasks'][number-1]
        if case['repo'] != 'internetarchive/openlibrary' or not re.fullmatch('[0-9a-f]{40}', case['base_commit']):
            raise RuntimeError('This repair is restricted to the diagnosed OpenLibrary images')
        directory = runner.LAB / 'validation/git-metadata-repair' / f'task-{number:02d}' / uuid.uuid4().hex[:12]
        directory.mkdir(parents=True)
        image = await runner.ensure_image('jefzda/sweap-images:' + case['dockerhub_tag'], directory)
        if case['instance_id'] in overrides:
            existing = overrides[case['instance_id']]
            if existing['official_image_id'] != image['Id'] or existing['base_commit'] != case['base_commit']:
                raise RuntimeError('Existing overlay origin mismatch')
            await runner.host(['docker', 'image', 'inspect', existing['cached_image_id']])
            if existing.get('dependency_kind') == 'canonical-base-submodules-and-evaluator-test-commit-recovery':
                print(f'Task {number}: existing complete overlay retained', flush=True)
                continue
            if existing.get('dependency_kind') not in ('canonical-base-git-metadata-recovery', 'canonical-base-and-submodule-git-metadata-recovery'):
                raise RuntimeError('Refusing to replace an unrelated existing overlay')
            runner.save(directory / 'previous-overlay.json', existing)
        cid = None
        commands = []
        async def command(argv, timeout=180):
            result = await runner.host(['docker', 'exec', cid, *argv], timeout=timeout, check=False)
            commands.append({'command': argv, 'returncode': result.returncode,
                             'stdout': result.stdout, 'stderr': result.stderr})
            runner.save(directory / 'commands.json', commands)
            if result.returncode:
                raise RuntimeError(f'Task {number}: {argv[0]} failed: {result.stderr[-1600:]}')
            return result.stdout.strip()
        try:
            cid = (await runner.host(['docker','run','-d','--network','bridge','--cpus','2','--memory','4096m',
                '--name','swe-git-repair-'+uuid.uuid4().hex[:12], '--workdir','/app','--entrypoint','/bin/sh',
                image['Id'],'-c','exec tail -f /dev/null'])).stdout.strip()
            print(f'Task {number}: fetching exact base commit {case["base_commit"]}; no reference/model access',flush=True)
            original_index = await command(['git','ls-files','--stage'])
            await command(['git','init','--bare','/tmp/recovered.git'])
            await command(['git','--git-dir=/tmp/recovered.git','fetch','--no-tags','--depth=1',
                           'https://github.com/internetarchive/openlibrary.git',case['base_commit']],timeout=600)
            fetched = await command(['git','--git-dir=/tmp/recovered.git','rev-parse','FETCH_HEAD'])
            if fetched != case['base_commit']: raise RuntimeError('Fetched commit differs from pinned base')
            await command(['git','--git-dir=/tmp/recovered.git','update-ref','HEAD',fetched])
            await command(['git','--git-dir=/tmp/recovered.git','config','core.bare','false'])
            await command(['git','--git-dir=/tmp/recovered.git','config','core.hooksPath','/dev/null'])
            await command(['mv','/app/.git','/tmp/broken.git'])
            await command(['mv','/tmp/recovered.git','/app/.git'])
            # Populate the index without checking out or modifying any source file.
            await command(['git','reset','--mixed',fetched])
            await command(['git','diff','--ignore-submodules=all','--exit-code',fetched,'--'])
            await command(['git','diff','--cached','--ignore-submodules=all','--exit-code',fetched,'--'])
            if await command(['git','ls-files','--stage']) != original_index:
                raise RuntimeError('Original tracked blob/mode/gitlink index differs from canonical base')
            # Restore only Git metadata for the two pinned submodules as well.
            repositories = {'vendor/infogami': 'https://github.com/internetarchive/infogami.git',
                            'vendor/js/wmd': 'https://github.com/internetarchive/wmd.git'}
            for line in original_index.splitlines():
                if not line.startswith('160000 '): continue
                fields, subpath = line.split('\t', 1)
                subcommit = fields.split()[1]
                if subpath not in repositories: raise RuntimeError('Unexpected submodule path')
                url = await command(['git','config','-f','.gitmodules','--get',f'submodule.{subpath}.url'])
                url = url.replace('git://github.com/', 'https://github.com/', 1)
                if url != repositories[subpath]: raise RuntimeError('Submodule repository differs from pinned allowlist')
                gitdir = '/app/.git/modules/' + subpath
                worktree = '/app/' + subpath
                await command(['git','init','--bare',gitdir])
                await command(['git','--git-dir='+gitdir,'fetch','--no-tags','--depth=1',url,subcommit],timeout=600)
                if await command(['git','--git-dir='+gitdir,'rev-parse','FETCH_HEAD']) != subcommit:
                    raise RuntimeError('Fetched submodule differs from canonical gitlink')
                await command(['git','--git-dir='+gitdir,'update-ref','HEAD',subcommit])
                await command(['git','--git-dir='+gitdir,'config','core.bare','false'])
                await command(['git','--git-dir='+gitdir,'config','core.worktree',worktree])
                await command(['git','--git-dir='+gitdir,'config','core.hooksPath','/dev/null'])
                await command(['git','--git-dir='+gitdir,'reset','--mixed',subcommit])
                await command(['git','--git-dir='+gitdir,'diff','--ignore-submodules=all','--exit-code',subcommit,'--'])
                await command(['git','--git-dir='+gitdir,'fsck','--no-reflogs',subcommit],timeout=300)
            # The unchanged official evaluator checks out test files from a pinned
            # test commit. Keep those objects in this TRUSTED image only. prepare()
            # creates a no-local shallow base-only clone before any agent can run.
            last = str(rows[case['instance_id']]['before_repo_set_cmd']).strip().splitlines()[-1]
            checkout = shlex.split(last)
            if checkout[:2] != ['git', 'checkout'] or len(checkout) < 5 or checkout[3] != '--':
                raise RuntimeError('Unexpected official test checkout command')
            testcommit, testpaths = checkout[2], checkout[4:]
            if not re.fullmatch('[0-9a-f]{40}', testcommit): raise RuntimeError('Invalid test commit')
            await command(['git','fetch','--no-tags','--depth=1',
                           'https://github.com/internetarchive/openlibrary.git',testcommit],timeout=600)
            if await command(['git','rev-parse','FETCH_HEAD']) != testcommit:
                raise RuntimeError('Official test commit mismatch')
            # Confirm that every official test file exists, without checking it out.
            for testpath in testpaths:
                await command(['git','cat-file','-e',testcommit+':'+testpath])
            # Exercise the evaluator's checkout operation before registering the image.
            await command(['git','checkout','--detach',fetched])
            tree = await command(['git','rev-parse',fetched+'^{tree}'])
            if await command(['git','write-tree']) != tree: raise RuntimeError('Canonical index tree mismatch')
            await command(['git','fsck','--no-reflogs',fetched],timeout=300)
            if await command(['git','rev-list','--all','--count']) != '1': raise RuntimeError('Unexpected additional history')
            await command(['rm','-rf','/tmp/broken.git'])
            cached=(await runner.host(['docker','commit',cid],timeout=300)).stdout.strip()
            record={'official_image_id':image['Id'],'cached_image_id':cached,'base_commit':fetched,
                'canonical_tree':tree,'dataset_sha256':selection['dataset_sha256'],'at':runner.now(),
                'dependency_kind':'canonical-base-submodules-and-evaluator-test-commit-recovery','reference_code_applied':False,
                'reference_source_executed':False,'model_tokens':0,'audit':str(directory.relative_to(runner.LAB)),
                'evaluator_test_commit':testcommit,'evaluator_test_paths':testpaths,
                'test_commit_scope':'trusted evaluator image only; agent snapshot must exclude it'}
            overrides[case['instance_id']]=record
            if not stage_only: runner.save(output,overrides)
            runner.save(directory/'summary.json',record)
            if stage_only: runner.save(runner.LAB/'validation/git-metadata-repair'/f'pending-task-{number}.json',record)
            print(f'Task {number}: Git objects restored; source matches canonical tree {tree}',flush=True)
        finally:
            if cid: await runner.host(['docker','rm','-f',cid],check=False)


if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--tasks',required=True)
    p.add_argument('--stage-only', action='store_true', help='Create overlay and audit without changing active cache registry')
    args=p.parse_args();numbers=[int(x) for x in args.tasks.split(',')]
    if not numbers or any(n not in (161,184,199) for n in numbers):p.error('Only diagnosed tasks 161,184,199 are supported')
    asyncio.run(repair(numbers, args.stage_only))
