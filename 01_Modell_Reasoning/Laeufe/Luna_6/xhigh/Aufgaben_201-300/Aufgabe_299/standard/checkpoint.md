# Checkpoint

Task: Add filesystem path completion to `:open`.

Implemented a `FilePathCategory` table model and registered it in `:open` according to `completion.open_categories`. Added the `filesystem` option and default plus `completion.favorite_paths` (`List/String`, default `[]`) to the configuration help source. Updated existing completion expectations for the new empty category.

Verification: `python -m pytest tests/unit/config/test_configdata.py tests/unit/completion/test_models.py -q --benchmark-skip --disable-warnings --tb=short` passed (96 passed, 2 skipped). Filesystem smoke checks passed for deterministic absolute-path suggestions, equivalent `file:///` inputs, `~/` display preservation, and rejection of non-local/URL inputs. `git diff --check` passed.
