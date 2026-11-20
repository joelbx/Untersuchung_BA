# Galaxy install issue checkpoint

- Updated `ansible-galaxy install -r` to parse one requirements file and install both roles and collections when no roles path is supplied.
- Kept explicit role and collection installs separate, with skip messages at the requested severity. An implicit install with `-p` or `--roles-path` warns that collections cannot use a roles path.
- Empty requirements files now print `Skipping install, no requirements found`. Role requirements still require a `.yml` or `.yaml` extension.
- Role dependency processing filters selected root roles before appending transitive dependencies and avoids repeatedly appending forced dependencies.
- Updated the existing integration assertion for empty requirements and added focused unit coverage, including a local role tarball install.
- Verified 290 tests: `ANSIBLE_DEVEL_WARNING=False PYTHONPATH=lib:test pytest -q test/units/cli/test_galaxy.py test/units/cli/galaxy test/units/galaxy`.
- Verified `git diff --check` and Python compilation. No external research or downloads used.
