Task: Normalize ISBN and publisher/place fields in Internet Archive metadata imports.

Status: Implemented public ISBN and publisher/place utilities and wired them into `get_ia_record`. Updated and expanded importer and utility tests. Relevant pytest run: 31 passed. `black` and `ruff` are unavailable in this environment; `git diff --check` passed.
