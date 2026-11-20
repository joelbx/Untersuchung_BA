# Checkpoint

Resolved collection symlink build and artifact install handling in `lib/ansible/galaxy/collection.py`.

- Manifest traversal records internal linked directories once and avoids recursion.
- Tar build stores internal links with relative linknames and copies external file link content.
- Extraction helpers expose `(TarInfo, stream)`; install checks paths and restores safe links.
- Updated collection unit tests and added build/install round trip and unsafe link coverage.

Checks: `python -m pytest test/units/galaxy/test_collection.py -q --disable-warnings --maxfail=1` passed (61 tests); `git diff --check` passed.

Tooling: `rg` was unavailable (`/bin/bash: rg: command not found`); repository search used grep/find. No external tooling was needed.
