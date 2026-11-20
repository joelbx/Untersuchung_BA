"""Binary patch export with an explicit environment baseline and private index.

Executed in a container by the host, never changes HEAD or the real Git index.
Initially untracked, nonignored files belong to the environment baseline. Their
subsequent edits/deletions remain genuine patch changes. Gitlinks stay gitlinks.
"""
import argparse
import json
import os
from pathlib import Path
import subprocess
import tempfile


def git(root, *args, index=None, data=None):
    env = dict(os.environ)
    if index:
        env['GIT_INDEX_FILE'] = str(index)
    return subprocess.run(['git', '--literal-pathspecs', '-C', str(root), *args],
                          input=data, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          env=env, check=True).stdout


def paths(value):
    return [os.fsdecode(p) for p in value.split(b'\0') if p]


def worktree(root, base):
    """Materialize tracked changes and visible untracked files in a private tree."""
    with tempfile.TemporaryDirectory(prefix='swe-export-') as tmp:
        index = Path(tmp) / 'index'
        git(root, 'read-tree', base, index=index)
        links = []
        for entry in git(root, 'ls-files', '--stage', '-z', index=index).split(b'\0'):
            if entry.startswith(b'160000 '):
                links.append(os.fsdecode(entry.split(b'\t', 1)[1]))
        changed = paths(git(root, 'diff', '--name-only', '-z', base, index=index))
        others = paths(git(root, 'ls-files', '--others', '--exclude-standard', '-z', index=index))
        selected = sorted(set(changed + others))
        selected = [p for p in selected if p != '.codex-role-output' and not p.startswith('.codex-role-output/')
                    and not any(p == link or p.startswith(link + '/') for link in links)]
        replacements = {p for p in selected if (Path(root) / p).is_symlink() or (Path(root) / p).is_file()}
        selected = [p for p in selected if not any(str(parent) in replacements for parent in Path(p).parents
                                                  if str(parent) != '.')]
        # Explicit literal paths preserve gitlinks and avoid indexing ignored
        # dependency trees. Chunks also work on older Git without pathspec stdin.
        for start in range(0, len(selected), 100):
            git(root, 'add', '--all', '--', *selected[start:start + 100], index=index)
        return git(root, 'write-tree', index=index).decode().strip()


def capture(root):
    head = git(root, 'rev-parse', 'HEAD').decode().strip()
    return {'head': head, 'tree': worktree(root, head), 'policy': 'environment-baseline-v1'}


def export(root, baseline):
    if git(root, 'rev-parse', 'HEAD').decode().strip() != baseline['head']:
        raise RuntimeError('Agent changed canonical HEAD; patch export refused')
    tree = worktree(root, baseline['tree'])
    return git(root, 'diff', '--binary', '--no-ext-diff', '--no-textconv', baseline['tree'], tree)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['capture', 'export'])
    parser.add_argument('--root', default='/app')
    parser.add_argument('--baseline', required=True)
    args = parser.parse_args()
    path = Path(args.baseline)
    if args.action == 'capture':
        path.write_text(json.dumps(capture(args.root)))
        print(path.read_text())
    else:
        import sys
        sys.stdout.buffer.write(export(args.root, json.loads(path.read_text())))
