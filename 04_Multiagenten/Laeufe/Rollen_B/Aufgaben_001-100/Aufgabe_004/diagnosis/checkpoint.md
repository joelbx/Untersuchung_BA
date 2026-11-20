# Fault localization progress

Inspected PassAliases provider/view/form, bridge factory/types, memoizer, and existing component tests. Source and tests unchanged.

Findings: bridge `getDefault` creates a vault during initialization and takes a callback; the required contract is an optional vault and a separate `createDefaultVault`. Provider assumes a vault exists, so no-vault initialization cannot settle into the empty state. `getAliasOptions` throws without a vault, and the form closes after that error, blocking creation. Existing empty UI lacks literal “No aliases”; list intentionally slices to three. Existing component tests mock context and do not exercise the bridge/no-vault path. Need report behavioral coverage and uncertainty.
