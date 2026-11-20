# Checkpoint

Task: support version-aware modes for qt.workarounds.disable_accelerated_2d_canvas.
Status: implementation and regression tests complete; verification in progress.

Initial red check: `python -m pytest tests/unit/config/test_qtargs.py -k accelerated_canvas_workaround -q` aborted in pytest-qt's `qapp` fixture (exit 134), before test execution, likely due unavailable display. Retrying with `QT_QPA_PLATFORM=offscreen`.

Red checks with `QT_QPA_PLATFORM=offscreen` failed as expected: string modes rejected by Bool validation; default was `true` rather than `auto`.

Green check: `QT_QPA_PLATFORM=offscreen python -m pytest tests/unit/config/test_qtargs.py -q --override-ini addopts=''` passed (114 tests) before a minor test-only argument correction.

Repository-wide check: `QT_QPA_PLATFORM=offscreen python -m pytest -q --override-ini addopts=''` entered repeated end-to-end errors in `tests/end2end/test_adblock_e2e.py` and `tests/end2end/test_hints_html.py`; terminated before completion. A focused run, `QT_QPA_PLATFORM=offscreen python -m pytest tests/end2end/test_adblock_e2e.py -q --maxfail=1 --reruns=0 --override-ini addopts=''`, showed `test_adblock[auto]` fails at setup because Chromium refuses to run as root without `--no-sandbox`. The suite's remaining outcome is unknown.

`QT_QPA_PLATFORM=offscreen python -m pytest tests/unit -q --maxfail=1 --reruns=0 --override-ini addopts=''` exited 1 before a usable failure summary while entering browser tests. `QT_QPA_PLATFORM=offscreen python -m pytest tests/unit/config -q --maxfail=1 --reruns=0 --override-ini addopts=''` failed at `test_init_benchmark` because a slow YAML load logged a warning (3.66s versus a 2s local threshold). Retrying with `--benchmark-skip` reached 1031 passing tests, then `TestAll.test_completion_validity[Proxy]` failed due Qt/OpenSSL warnings (`QSslSocket: cannot resolve EVP_PKEY_base_id`, `SSL_get_peer_certificate`). Remaining config tests were not run in that command.

Final focused check: `QT_QPA_PLATFORM=offscreen python -m pytest tests/unit/config/test_qtargs.py tests/unit/config/test_configdata.py -q --benchmark-skip --reruns=0 --override-ini addopts=''` passed (144 passed, 1 benchmark skipped). `git diff --check` passed. Qt 6 behavior was tested with version fixtures and the Qt 6 machinery flag; no Qt 6 runtime is installed locally.
