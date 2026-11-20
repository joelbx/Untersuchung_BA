Fixed `Play` so it derives the display name from `hosts` when `get_name` is called, without changing the input data. Invalid `hosts` values now raise the specified `AnsibleParserError` messages. I also updated the existing empty-host integration expectation.

Verification: all 247 playbook unit tests passed. The empty-host playbook produced the expected parser error, and `git diff --check` passed.