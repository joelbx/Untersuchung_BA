# Fault-localization checkpoint

Inspected `qutebrowser/utils/urlutils.py` and existing unit tests; no source or tests changed.

- `_get_incdec_value` (lines 532-551) checks only `val <= 0` before decrement, so a positive value below `count` becomes negative. It does not validate `count` type or positivity. Its zero-padding adjustment is ad hoc.
- `incdec_number` (lines 554-605) defaults to `{'path', 'query'}`, accepts and changes `port`, iterates components in reverse URL order, and uses decoded QUrl getters/setters. Its regex has no exclusion for percent-encoded triplets. Invalid `incdec` is checked only after a numeric match.
- Direct QUrl inspection: `QUrl('http://localhost/%3A5').path()` is `/:5`, while `.path(QUrl.FullyEncoded)` is `/%3A5`; similar encoded-preservation concerns apply to component access. QUrl itself normalizes some escapes during initial parse (e.g. `/%35` to `/5`).
- `qutebrowser/browser/navigate.py:46-49` supplies configured segments. `qutebrowser/config/configdata.yml:1792` currently allows `port` and defaults to `[path, query]`.
- Existing tests `tests/unit/utils/test_urlutils.py:649-657` require port modification and lines 676-690 expect decrement by 100 from 20 to yield -80, conflicting with issue requirements. Lines 708-715 expect query to win over path for the selected set. The issue itself conflicts on target selection: last sequence in URL order versus first match in first applicable segment ordered path/query/anchor/host.
- Focused existing test run: 9 passed (`pytest -q -o addopts='' tests/unit/utils/test_urlutils.py -k 'TestIncDecNumber and (test_incdec_port or test_number_below_0 or test_incdec_leading_zeroes)'`). Initial plain pytest invocation was blocked by deprecated `--strict` in repository pytest.ini under installed pytest.
