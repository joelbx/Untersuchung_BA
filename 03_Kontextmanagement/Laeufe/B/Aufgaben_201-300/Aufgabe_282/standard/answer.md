Implemented JavaScript message filtering in [shared.py](/app/qutebrowser/browser/shared.py). The new `.levels` and `.excludes` settings let users hide matching CSP messages while still seeing other errors from the same source. I updated the settings documentation and added focused tests.

Validation: **43 relevant tests passed** with Qt offscreen; `git diff --check` is clean.