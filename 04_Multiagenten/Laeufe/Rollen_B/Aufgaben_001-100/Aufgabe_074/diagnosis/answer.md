The fault is concentrated in [fn_to_cli.py](/app/scripts/solr_builder/solr_builder/fn_to_cli.py:35):

- `type_to_argparse` rejects `Path` and typed lists other than `list[str]`. It needs to convert each list token to its annotated element type.
- `__init__` changes underscores to hyphens in option names and uses a single dash for one-character names. The requested mapping is `--<parameter_name>`. Required lists should parse positionally; lists with defaults should use that option and preserve `None` when omitted.
- `parse_args` cannot accept a token sequence, and `run` discards both synchronous and asynchronous return values.

The four existing tests pass, but they do not cover these cases. One point needs care in a fix: a list annotated `list[Path] | None` *without a default* is currently treated as required; the issue does not make clear whether that annotation alone should make it optional. I left project source and tests unchanged because this run was scoped to fault localization.