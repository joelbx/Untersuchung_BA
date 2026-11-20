Updated [QtColor](/app/qutebrowser/config/configtypes.py:990) so HSV and HSVA hue percentages scale to 359, while other channels scale to 255. It now rejects unsupported color function names and incorrect component counts. Added regression cases in [test_configtypes.py](/app/tests/unit/config/test_configtypes.py:1235).

All 54 focused color tests pass.