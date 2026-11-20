# Work checkpoint

Issue: standardize plugin routing/deprecation handling and expose plugin resolution context.

Implemented:
- Added `AnsiblePluginError` with `plugin_load_context`; migrated removed, redirect-cycle, and collection-version errors to this hierarchy.
- Added `get_with_context_result` and `PluginLoader.get_with_context`; `get()` now delegates and returns only the plugin object.
- Tombstones now raise `AnsiblePluginRemovedError` with resolution context. Plugin lookup retains deprecation metadata without printing legacy warnings.
- Centralized deprecation formatting in `Display.get_deprecation_message` and updated `Display.deprecated`.
- Updated connection loading, action module resolution, and Jinja filter removal handling to use/contextualize the new behavior.

Verification:
- 40 focused existing unit tests passed.
- Syntax compilation and `git diff --check` passed.
- A broader template run had one unrelated existing failure in `test_template_convert_data_to_json` (expected `'"bar"'`, got `'bar'`); plugin-related template tests otherwise passed.
