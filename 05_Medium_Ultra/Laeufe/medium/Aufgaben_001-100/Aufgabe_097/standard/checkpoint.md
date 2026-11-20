Task: Raise controller minimum to Python 3.12 and update collection extraction/version references per issue.
Status: Source and tests updated. Final review complete.
Changes: Shared 3.12 entrypoint error, package and ansible-test metadata, removal of TarFile private cache, direct getmember dirname lookup, controller-only version workarounds removed, changelog fragment added.
Verification: 73 focused tests passed and 1 skipped with a simulated Python 3.12 version_info on Python 3.11; 7 role install tests passed with the same simulation. Both CLI entrypoints emitted identical minimum-version errors on Python 3.11. compileall and git diff --check passed.
Limitation: No native Python 3.12 interpreter is installed in this workspace.
