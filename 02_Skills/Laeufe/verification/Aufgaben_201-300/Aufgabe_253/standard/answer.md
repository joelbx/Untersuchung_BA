Updated [GuiProcess](/app/qutebrowser/misc/guiprocess.py) to show stdout and stderr live and publish nonempty final summaries in stdout-then-stderr order. Stderr messages use error severity. Added coverage in [test_guiprocess.py](/app/tests/unit/misc/test_guiprocess.py).

Verification: all 42 `GuiProcess` tests passed; `git diff --check` passed.