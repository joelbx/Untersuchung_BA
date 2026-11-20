# Fault localization progress

- Inspected Python deprecation recording/exit output, argument-spec handling, callback display, validator schema/checks, and C# module code.
- Python date entries are blocked by version-only signatures in `common/warnings.py` and `basic.py`; `_return_formatted` already preserves recorded-then-supplied order for strings and two-tuples, but mapping inputs discard `date`.
- Date-based argument deprecation additionally needs `common/parameters.py` and `basic.py` alias handling; the validator schema and expiration checks assume versions.
- `Display.deprecated` and callback dispatch need date support for presentation. C# `Deprecate` and alias validation are version-only, with `removed_in_version` in spec defaults.
- Existing tests cover version-only deprecations and ordering; no date cases found in inspected unit tests. No project source or tests changed.
