# Checkpoint

Task: Add filesystem path completion for `:open`.
Status: Complete.

Changes:
- Added `FilePathCategory` for favorite paths, absolute paths, local `file:///` URLs, and `~` paths. Results are sorted for filesystem scans and retain the entered path form.
- Registered the category in the URL completion model in the configured order.
- Added `filesystem` to `completion.open_categories` and `completion.favorite_paths` as List/String with default `[]`; regenerated settings help.
- Added focused path and URL model tests, and updated existing default-category expectations.

Checks executed:
- `QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/completion --disable-warnings`: 298 passed, 1 skipped, 1 xfailed.
- `QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/config/test_configdata.py tests/unit/config/test_config.py --disable-warnings`: 157 passed.
- `QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/completion/test_filepathcategory.py tests/unit/completion/test_models.py --disable-warnings`: 79 passed after final test additions.
- `python -m compileall -q qutebrowser/completion/models/filepathcategory.py qutebrowser/completion/models/urlmodel.py`: passed.
- `git diff --check`: passed.
- `python -c 'from scripts.dev import src2asciidoc; src2asciidoc.generate_settings("doc/help/settings.asciidoc")'`: passed.
