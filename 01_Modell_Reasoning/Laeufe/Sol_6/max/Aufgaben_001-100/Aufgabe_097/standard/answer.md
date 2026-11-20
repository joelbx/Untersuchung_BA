Updated the controller minimum to **Python 3.12** across the CLI, `ansible-test`, package metadata, and release note. Collection extraction now passes `dirname` unchanged to `TarFile.getmember()` and no longer uses the private TarFile cache.

Verification: 73 tests passed, 1 skipped. Another 20 passed on Python 3.11 after temporarily preloading the CLI with a simulated 3.12 version; both entry points correctly reject an actual 3.11 controller with the same message. A real 3.12 run was unavailable.

The Azure Galaxy and Generic CI matrices still list 3.10 and 3.11; harness configuration was left untouched.