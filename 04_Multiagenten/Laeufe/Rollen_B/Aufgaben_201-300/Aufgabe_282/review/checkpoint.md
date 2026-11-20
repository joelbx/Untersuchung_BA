VERDICT: FIX
Review finding: qutebrowser/config/configdata.yml advertises `debug` as a content.javascript.log_message.levels value, but JsLogLevel has only unknown/info/warning/error, so selecting debug can never show a UI message. Remove the unsupported value or implement a real debug level end to end.
Tests: DISPLAY=:0 QT_QPA_PLATFORM=offscreen python -m pytest -p no:xvfb -q tests/unit/browser/test_shared.py tests/unit/config/test_configdata.py tests/unit/config/test_configtypes.py => exit 0; 1151 passed, 10 xfailed.
Test environment: plain pytest aborted at Qt qapp setup; offscreen with the default Xvfb plugin ran tests but exited 1 after an XIO shutdown error; disabling xvfb and setting DISPLAY resolved this.
No project code or tests changed during review.
