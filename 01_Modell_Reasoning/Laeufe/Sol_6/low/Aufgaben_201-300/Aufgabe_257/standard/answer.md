Updated the checked-out files to support mocked SSO login, propagate the OS assigned auth and proxy listener addresses, and have tsh command handlers return errors to `Run` instead of terminating the process. `Run` also accepts runtime configuration options after argument parsing.

The tsh package tests, the service startup test, and `git diff --check` pass.