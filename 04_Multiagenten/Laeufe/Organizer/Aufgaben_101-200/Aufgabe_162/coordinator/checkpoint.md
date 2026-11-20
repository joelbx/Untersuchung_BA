# Checkpoint

Task: Add optional encoding validation to FormatString and require ASCII for the HTTP user-agent setting.

Completed:
- FormatString now extends String and accepts an optional encoding, reusing String's to_py encoding validation.
- content.headers.user_agent specifies ASCII.
- Added unit coverage for ASCII acceptance/rejection, UTF-8 and unrestricted compatibility, and the configured user-agent type.
- Focused type/data tests: 1139 passed, 10 xfailed.
- Config, configfiles, and configinit tests: 390 passed, 9 skipped.
- test_websettings.py in isolation has 4 passed, 1 skipped, 1 failure because PyQt5.QtWebKit is unavailable. A broader suite also exited at this file; with that test deselected the file passes in isolation.

No delegation used.
