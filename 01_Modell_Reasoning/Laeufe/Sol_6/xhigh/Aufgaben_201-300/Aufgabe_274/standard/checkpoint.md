# Checkpoint

Issue: support `always`, `auto`, and `never` for `qt.workarounds.disable_accelerated_2d_canvas`.

Plan: inspect the current Qt argument path and focused tests, update the schema and resolver, then run the relevant existing tests.

Status: complete.

Changed `configdata.yml` to use the `always`/`auto`/`never` string enum with
`auto` as default. Updated `qtargs.py` to resolve `auto` from runtime Qt and
Chromium major version, and added boundary coverage in `test_qtargs.py`.

Verification: `QT_QPA_PLATFORM=offscreen python -m pytest -q
tests/unit/config/test_qtargs.py tests/unit/config/test_configdata.py`
(147 passed).
