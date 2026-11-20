Fixed the pip module so it uses the current interpreter’s `-m pip` when pip is importable and no executable or virtualenv is specified. Launchers are now argv lists, package listing tries `list --format=freeze` before `freeze`, and the virtualenv PATH prefix uses `os.path.join`.

Verification: 11 pip unit tests passed; `git diff --check` passed.