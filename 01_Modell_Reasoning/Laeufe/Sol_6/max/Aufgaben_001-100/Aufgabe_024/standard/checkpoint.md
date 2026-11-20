# Progress

- Started investigating author matching, honorific removal, and year extraction in `/app`.
- `rg` is unavailable; using local `grep` and `find` for repository inspection.
- Found that `find_author` stops after the first nonempty query even if dates later reject its candidates. The query backend maps every `*` to a wildcard, and `import_author` drops unlisted input fields.
- Implemented year-based ranking, honorific string handling, literal-asterisk equality fallback, and full-field preservation for new authors. The query backend lives in a submodule, so its experimental edit was reverted; only tracked project files are changed.
- Verified the full add-book suite: 163 passed, 1 expected failure. Earlier focused run: 143 passed across load-book, core helper, and catalog utility tests. Ruff and `git diff --check` passed.
- Final review: the vendor query backend does not honor escaped `*` in LIKE queries; exact literal equality queries provide the supported fallback without changing the submodule.
