# Checkpoint

Task: resolve the WebKit certificate error wrapper constructor and safe HTML rendering issue in `/app`.

Implementation:
- `CertificateErrorWrapper` now accepts `reply` and `errors` in signal order, supports named arguments, and keeps compatibility with `CertificateErrorWrapper(errors)`.
- The reply is retained as data only; construction makes no network calls.
- The WebKit network manager supplies both arguments explicitly. Existing HTML behavior renders one error in a paragraph and multiple errors in a list; both paths escape content (the single path uses `html.escape` in the abstract wrapper and the list template uses the autoescaping Jinja environment).

Verification: `python -m pytest tests/unit/browser/webkit/test_certificateerror.py -q` passed (4 tests); `git diff --check` passed.
