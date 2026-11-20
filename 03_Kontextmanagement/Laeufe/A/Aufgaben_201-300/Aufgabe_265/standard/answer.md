Updated [QtColor](/app/qutebrowser/config/configtypes.py:990) so HSV and HSVA hue percentages scale to 359, while the other channels scale to 255. `to_py` now validates the function name and component count before constructing a `QColor`; RGB and RGBA behavior is preserved.

Updated [tests](/app/tests/unit/config/test_configtypes.py:1235). All 35 `TestQtColor` tests pass.