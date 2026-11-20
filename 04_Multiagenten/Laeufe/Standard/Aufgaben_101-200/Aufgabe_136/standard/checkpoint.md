# Checkpoint

Completed certificate wrapper fix. WebKit accepts `reply` and `errors` (including positional pairs and legacy positional errors), stores the reply without acting on it during construction, and invokes `ignoreSslErrors` only when accepted. Single errors render escaped paragraphs; multiple errors render escaped lists. Shared decision methods, `UndeferrableError`, Qt5/Qt6 wrappers, factory, and callers are updated.

Verification: focused certificate and network manager suite: 11 passed, exit 0. `git diff --check` passed. The pre-existing WebEngine tab suite could not initialize its display in this environment; Qt6 is not installed, so its wrapper was exercised with a mock Qt error.
