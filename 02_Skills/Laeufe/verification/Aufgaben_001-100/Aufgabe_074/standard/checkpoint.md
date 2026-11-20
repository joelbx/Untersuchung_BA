# FnToCLI checkpoint

Implemented `Path` and typed `list[int | str | float | Path]` parsing. Required lists use positional arguments with at least one value; lists with defaults and nullable list annotations use `--<parameter_name>` options. Optional nullable lists omitted from the CLI receive `None`. `parse_args` accepts a token sequence, and `run` returns synchronous or asynchronous function results. Option names preserve parameter spelling.

Verification:
- `python -m pytest scripts/solr_builder/tests/test_fn_to_cli.py -q`: 13 passed.
- `python -m ruff check scripts/solr_builder/solr_builder/fn_to_cli.py scripts/solr_builder/tests/test_fn_to_cli.py && git diff --check`: exit 0.
- `python -m black --check scripts/solr_builder/solr_builder/fn_to_cli.py scripts/solr_builder/tests/test_fn_to_cli.py`: exit 1, `/usr/local/bin/python: No module named black`. Black formatting remains unverified because the offline environment lacks Black. No dependency download attempted.

Initial search limitation: `rg` unavailable (`/bin/bash: rg: command not found`); used local grep/find.
