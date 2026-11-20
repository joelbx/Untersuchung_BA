Updated [GUIProcess](/app/qutebrowser/misc/guiprocess.py) to show stdout and stderr live. Nonempty streams now get separate final summaries, ordered stdout then stderr, with informational and error severity respectively. Updated the [tests](/app/tests/unit/misc/test_guiprocess.py).

Verification: all 41 focused tests passed, and `git diff --check` passed.