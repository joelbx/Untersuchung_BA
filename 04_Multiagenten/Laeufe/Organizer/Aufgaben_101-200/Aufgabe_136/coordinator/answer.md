Updated the WebKit certificate wrapper to accept named `reply` and `errors` arguments while preserving existing positional error-list calls. Construction stores the reply without calling it. The HTML tests now cover escaped special characters in both paragraph and list output.

Added the requested certificate decision methods, `UndeferrableError`, Qt5 and Qt6 WebEngine wrappers, and a version-based factory, then connected them to the existing certificate callbacks.

**Validation:** 11 focused certificate tests and the WebKit network manager test passed; `git diff --check` passed. The broader WebEngine tab test exited during its first case without a pytest traceback, so that suite remains unverified. No delegation was used.