# Checkpoint

Issue: make certificate error wrappers accept reply/errors consistently, render escaped error HTML for single and multiple errors, and provide the requested Qt 5/Qt 6 certificate decision behavior.

Implemented:
- WebKit wrapper accepts named `reply` and `errors` parameters, preserves one-argument compatibility, and does not query or operate on the reply during construction.
- Certificate HTML is rendered as escaped paragraphs for one error and escaped list items inside a `<ul>` for other counts.
- Added abstract certificate decision state, `UndeferrableError`, Qt-specific WebEngine wrappers, and the Qt-version factory; WebEngine page construction now uses the factory.

Verification:
- `tests/unit/browser/webkit/test_certificateerror.py` and `tests/unit/utils/usertypes/test_misc.py`: 6 passed.
- `tests/unit/browser/webkit/network/test_networkmanager.py`: passed.
- `tests/unit/browser/webengine/test_webenginetab.py` terminated after collection/start without a pytest summary (exit status 1); standalone rerun had the same behavior.
- `flake8` is unavailable in the environment.
