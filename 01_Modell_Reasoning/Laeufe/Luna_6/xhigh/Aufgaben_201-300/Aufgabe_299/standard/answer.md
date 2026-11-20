Implemented filesystem completion for `:open`. The new [FilePathCategory](/app/qutebrowser/completion/models/filepathcategory.py:24) provides sorted matches for absolute paths and local `file:///` URLs, expands `~` while preserving its displayed form, and shows `completion.favorite_paths` for an empty pattern. It appears in the configured category order, including when it has no suggestions.

Added `filesystem` to the [default and valid `open_categories` values](/app/qutebrowser/config/configdata.yml:1141), and documented `completion.favorite_paths` there. Updated existing completion expectations for the empty category.

Verification passed: 96 tests passed, 2 skipped. Filesystem smoke checks and `git diff --check` also passed.