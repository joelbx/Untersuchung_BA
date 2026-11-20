Updated [mathstuff.py](/app/lib/ansible/plugins/filter/mathstuff.py) so `min` and `max` use Jinja’s enhanced filters when available, forward keyword arguments, raise the specified error when enhanced support is unavailable, and retain builtin fallback behavior.

Expanded [test_mathstuff.py](/app/test/units/plugins/filter/test_mathstuff.py) to cover attribute selection, `case_sensitive`, error handling, and fallback behavior.

Verification: **55 passed** in the mathstuff unit test module; `git diff --check` passed.