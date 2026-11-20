# Checkpoint

Task: Resolve plugin redirection, removal, deprecation, and context handling in Ansible.

Status: Implemented in checked-out files. Added `AnsiblePluginError` and contextual plugin exceptions; added `get_with_context_result` and `PluginLoader.get_with_context`; tombstones raise with resolution context, including empty tombstone entries, while `get_with_context` returns a structured failure. Centralized deprecation and removal text in `Display.get_deprecation_message`; updated action, connection, and template callers. Template routing now uses the loader while preserving legacy filter precedence and enforcing tombstones. Updated existing action mock and added focused regression tests.

Verification: 70 focused unit tests passed across plugin loader, action, filter, display, errors, template, task executor, and connection. `git diff --check` passed. The two existing display warning tests each pass individually; together they share singleton warning state and one fails on duplicate warning suppression.
