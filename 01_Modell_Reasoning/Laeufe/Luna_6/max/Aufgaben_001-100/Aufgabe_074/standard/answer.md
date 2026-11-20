Implemented `FnToCLI` support for `Path`, typed lists, optional list flags, direct parameter-name options, `parse_args(args=...)`, and return values from sync and async functions in [fn_to_cli.py](/app/scripts/solr_builder/solr_builder/fn_to_cli.py:56).

Verification passed: `pytest -q scripts/solr_builder/tests/test_fn_to_cli.py` (4 tests) and `git diff --check`.