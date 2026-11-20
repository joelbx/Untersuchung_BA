Task: Resolve plugin redirection, removal, and deprecation handling issue.
Status: Implemented and verified.
Changes: Added contextual plugin errors and get_with_context result, made tombstones fatal in direct resolution and structured in get_with_context, centralized deprecation formatting, updated action/connection/template consumers, and added focused tests.
Verification: 52 focused unit tests passed; git diff --check passed.
Note: An earlier broader run had three failures outside the focused set (Display singleton warning state, Jinja to_json rendering, and an action test still mocking the retired find_plugin call). The action test was updated and now passes. The other two were not changed.
