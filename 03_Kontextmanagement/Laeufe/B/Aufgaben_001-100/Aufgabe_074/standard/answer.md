Updated [FnToCLI](/app/scripts/solr_builder/solr_builder/fn_to_cli.py) to parse `Path` and typed lists, accept `--<parameter_name>` options, and return synchronous or asynchronous function results. Added coverage in [test_fn_to_cli.py](/app/scripts/solr_builder/tests/test_fn_to_cli.py).

Validation passed: 7 focused tests, Ruff, and `git diff --check`.