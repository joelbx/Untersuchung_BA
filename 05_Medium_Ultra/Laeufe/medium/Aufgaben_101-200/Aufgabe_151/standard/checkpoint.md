Task: Fix image file picker suffix handling in qutebrowser/browser/webengine/webview.py.
Status: Implemented version gated MIME suffix resolution and wired it into chooseFiles.
Verification: test_webview.py passes (11 tests); git diff --check passes.
Broader WebEngine unit suite aborted during Qt application fixture setup before related tests ran.
