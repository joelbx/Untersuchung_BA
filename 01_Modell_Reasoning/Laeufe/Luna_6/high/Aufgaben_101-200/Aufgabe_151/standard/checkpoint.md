# Checkpoint

Completed the Qt WebEngine file picker suffix workaround in `qutebrowser/browser/webengine/webview.py`.

- Runtime Qt gate: >= 6.2.3 and < 6.7.0, checked with `version_check(..., compiled=False)`.
- Specific MIME types use `mimetypes.guess_all_extensions`; wildcard MIME types scan `mimetypes.types_map`.
- Existing suffixes are excluded; `chooseFiles` appends the missing suffixes before parent calls.
- Verification: `python -m pytest tests/unit/browser/webengine/test_webview.py -q` passed (6 tests); `git diff --check` passed.
