Implemented structured plugin resolution context, contextual removal errors, centralized deprecation formatting, and updated connection, action, and Jinja plugin handling.

Verification: 40 focused tests passed; syntax compilation and `git diff --check` passed. A broader template run had one unrelated failure: `test_template_convert_data_to_json` expected `'"bar"'` but received `'bar'`.

Work notes are in `.codex-role-output/checkpoint.md` (ignored by git).