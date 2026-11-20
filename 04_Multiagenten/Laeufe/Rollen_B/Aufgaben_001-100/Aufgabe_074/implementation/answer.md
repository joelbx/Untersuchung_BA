Implemented `FnToCLI` support for `Path` and typed lists. Required lists parse positionally; optional lists use `--<parameter_name>` and pass `None` when omitted. `parse_args` now accepts a token sequence, and `run` returns synchronous or asynchronous results.

Updated the tests and documentation. All 13 Solr builder tests pass; Ruff and `git diff --check` pass.