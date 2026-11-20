# Certificate error wrapper work

- WebKit wrapper accepts named or positional `reply` and `errors`, retains the errors-only form, and only calls the reply when a certificate is accepted.
- Single errors render as escaped paragraphs; multiple errors render as escaped list items using the same HTML escaping.
- Added shared certificate decision methods and `UndeferrableError`, Qt 5 and Qt 6 WebEngine wrappers, and a version-based factory. Updated WebKit and WebEngine call sites.
- Focused tests passed. Combined related run passed 54 tests.
- Qt 6 runtime is unavailable in this environment. Its wrapper behavior was tested with a fake error object.
