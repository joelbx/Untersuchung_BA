The fault is in [QtColor._parse_value](/app/qutebrowser/config/configtypes.py:1004): it scales every percentage by `255/100`. [QtColor.to_py](/app/qutebrowser/config/configtypes.py:1020) parses components before distinguishing HSV hue, so `100%` hue becomes 255 instead of 359.

A fix should use `359/100` for the first HSV/HSVA component, retain `255/100` for the other percentage components, and validate function names and component counts before dispatching to `QColor.fromHsv` or `QColor.fromRgb`. The [existing tests](/app/tests/unit/config/test_configtypes.py:1235) expect the old hue value; all 24 focused tests pass, but none checks `100%` hue.

I recorded the diagnosis in the checkpoint. Source and tests remain unchanged because this run is restricted to fault localization.