Implemented the certificate wrapper changes:

- WebKit accepts `reply` and `errors` by name without querying the reply during construction. Single errors render as escaped paragraphs; multiple errors render as escaped list items.
- Added certificate decision state, `UndeferrableError`, Qt 5/Qt 6 WebEngine wrappers, and a version-aware factory.

**Verification:** certificate and usertype tests passed (6 total), and the WebKit network manager test passed. The WebEngine tab suite exited with status 1 before producing a pytest summary. `flake8` is unavailable in the environment.