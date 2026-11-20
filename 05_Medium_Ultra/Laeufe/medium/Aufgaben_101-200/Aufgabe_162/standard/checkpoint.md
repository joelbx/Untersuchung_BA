# Checkpoint

Task: Add optional encoding validation to FormatString during to_py conversion.
Status: Complete.
Changes: FormatString accepts an optional encoding and reports UnicodeEncodeError as ValidationError; content.headers.user_agent requires ASCII; tests cover ASCII rejection, other encoding acceptance, and behavior without encoding.
Verification: Config unit suite: 1138 passed, 1 deselected, 10 xfailed. Focused tests: 15 passed. git diff --check passed.
