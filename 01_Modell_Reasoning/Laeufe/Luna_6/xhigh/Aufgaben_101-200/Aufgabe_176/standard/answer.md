Updated [`urlutils.py`](/app/qutebrowser/utils/urlutils.py:532) to skip percent-encoded digits, preserve encoded URL components, validate operations and counts, reject decrements below zero, preserve zero padding, and search path → query → anchor → host. Ports are ignored.

Updated the existing [`TestIncDecNumber` cases](/app/tests/unit/utils/test_urlutils.py:617) for the revised selection and port behavior.

Verification: the URL utility module passed: **401 passed, 1 skipped**. I used `QT_QPA_PLATFORM=offscreen` and overrode pytest’s outdated `--strict` setting. `git diff --check` passed.