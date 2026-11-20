Task: Resolve author import matching with Open Library keys and external identifiers.
Status: Implemented and verified. OL keys, remote IDs, and name/date matching run in priority order; matched authors gain compatible IDs, conflicts raise clear errors, and new authors retain supplied IDs. Wikisource exempts suspect dates.
Verification: 188 tests passed in the add-book package and core model test file; Ruff and git diff --check passed.
