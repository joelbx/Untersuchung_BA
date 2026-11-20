# Checkpoint

Task: Extend `FnToCLI` to support `pathlib.Path`, typed lists, optional lists, explicit argument parsing, and return values from sync/async calls.

Completed: Updated `scripts/solr_builder/solr_builder/fn_to_cli.py`. Path annotations convert CLI strings to `Path`; supported list element types are converted with `nargs='+'`; required lists are positional and optional lists use `--<parameter>` with `None` when omitted. Snake case flags are accepted directly while retaining existing hyphenated aliases. `parse_args` accepts a sequence, and `run` returns wrapped sync/async results.

Verification: `pytest -q scripts/solr_builder/tests/test_fn_to_cli.py` passed (4 tests). `git diff --check` passed.
