Task: Raise the controller minimum Python version to 3.12 and align collection tar extraction behavior.

Plan:
- Locate version enforcement and user-facing checks, plus collection extraction/install logic.
- Update source, related existing tests, and a public changelog fragment.
- Run relevant existing tests and inspect the final diff.

Progress:
- Updated the controller guard to Python 3.12.
- Removed controller compatibility fallbacks and the collection tar member cache; directory extraction now passes the original name to `TarFile.getmember`.
- Updated the focused unit tests and added a breaking change changelog fragment.
- Focused extraction tests pass: 3 passed.
