Task: Fix password lookup key=value parsing, option defaults, chars handling, and deterministic seed behavior.
Status: Completed. Moved parameter parsing into LookupModule, wired plugin options into run(), and accepted string or list chars. Updated unit tests for option precedence and deterministic seed behavior.
Verification: 34 password lookup unit tests passed; lookup_password integration play passed (31 tasks, 0 failed); git diff --check passed.
