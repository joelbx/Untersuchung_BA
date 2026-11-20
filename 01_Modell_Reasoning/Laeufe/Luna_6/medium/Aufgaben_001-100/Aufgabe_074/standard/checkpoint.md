# Checkpoint

Implemented in `scripts/solr_builder/solr_builder/fn_to_cli.py`:

- Added `Path` conversion and typed lists for `int`, `str`, `float`, and `Path`.
- Required lists parse positional values; optional lists use `--<parameter>` and default to `None` when omitted.
- `parse_args` accepts an optional `Sequence[str]` and direct underscore parameter flags are supported, with hyphenated aliases retained for compatibility.
- `run` returns synchronous results and the result from async functions run through `asyncio.run`.

Verification: `python -m pytest scripts/solr_builder/tests/test_fn_to_cli.py -q` passes (4 tests). A direct parse check verified integer positional lists, `Path` optional lists, and omitted optional lists.
