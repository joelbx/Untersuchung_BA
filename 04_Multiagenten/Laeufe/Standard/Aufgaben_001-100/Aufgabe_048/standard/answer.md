Updated the repository so plugin removal and redirect failures carry resolution context. Added `get_with_context()` for callers that need the plugin instance and its metadata, centralized deprecation and removal message formatting, and updated the connection, action, and Jinja callers.

Relevant tests passed: **95 passed**. `git diff --check` also passed.