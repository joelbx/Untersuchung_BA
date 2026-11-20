Updated [qtargs.py](/app/qutebrowser/config/qtargs.py) to extract existing `--enable-features=` entries, combine their comma-separated values with QtWebEngine configuration features, and emit one consolidated argument when features are present. Other backends keep their arguments unchanged.

The existing Qt argument tests passed: `pytest -q tests/unit/config/test_qtargs.py` (77 collected).