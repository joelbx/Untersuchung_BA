Fixed `Play` so invalid `hosts` values raise `AnsibleParserError` with the requested messages instead of causing an unexpected exception. `Play.load` no longer derives or changes `name`; `get_name` derives it from `hosts` when needed.

Added regression tests. The relevant play and playbook tests pass: **15 passed**.