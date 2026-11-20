Implemented structured plugin resolution in [loader.py](/app/lib/ansible/plugins/loader.py): `get_with_context` returns the plugin object and resolution metadata, while `get` returns the object. Removed plugins now raise a context carrying `AnsiblePluginRemovedError`; deprecated redirects retain metadata without emitting warnings during lookup.

I also centralized removal and deprecation message formatting, updated the connection and action callers, and made removed Jinja filters surface as `TemplateSyntaxError`. Focused tests were added and the action test fixture was updated.

**Verification:** 97 relevant tests passed; `git diff --check` passed. No delegation was used.