Fixed the pip module so that, when neither `executable` nor `virtualenv` is set, it uses the current Python interpreter’s pip module when available. Pip launchers now use argv lists, package listing falls back from `list --format=freeze` to `freeze`, and the virtualenv PATH prefix uses `os.path.join`.

Verification: all 9 pip module unit tests passed.