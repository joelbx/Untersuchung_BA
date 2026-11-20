Added optional encoding validation to `FormatString`, using the same clear `ValidationError` as `String`. Configured `content.headers.user_agent` to require ASCII; other format strings remain unconstrained.

The existing config tests passed: **1,134 passed, 10 xfailed**. `git diff --check` passed.

Changes are in [configtypes.py](/app/qutebrowser/config/configtypes.py:206) and [configdata.yml](/app/qutebrowser/config/configdata.yml:645).