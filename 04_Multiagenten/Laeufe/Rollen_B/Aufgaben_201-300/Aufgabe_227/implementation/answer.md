Updated the MIME-suffix workaround to gate on runtime Qt alone: ≥ 6.2.3 and < 6.7.0. It now returns only dot-prefixed entries from `upstream_mimetypes`. I also clarified `version_check(compiled=False)` and changed the `compiled=True, exact=True` error to `RuntimeError`.

Verification: 31 focused tests passed with Qt’s offscreen platform setting; `git diff --check` passed.