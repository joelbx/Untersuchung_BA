Implemented Jinja2 keyword support for `min` and `max` in [mathstuff.py](/app/lib/ansible/plugins/filter/mathstuff.py:135). When enhanced Jinja filters are available, keyword arguments are forwarded; otherwise keyword calls raise the requested error and calls without keywords use Python’s built-ins.

Added coverage for `attribute`, `case_sensitive`, and fallback behavior in [test_mathstuff.py](/app/test/units/plugins/filter/test_mathstuff.py:64).

Verification: 55 tests passed; `git diff --check` passed.