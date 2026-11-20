Implemented the PassAliases setup hook and helper module. Vault lookup now returns `undefined` without creating a vault; requesting alias options creates one if needed and loads its aliases. The provider exposes the typed contract, refreshes cached aliases after creation, handles errors and quota upsells, and shows a clear “No aliases” state.

Updated the bridge types, factory, integration example, and the existing bridge mock.

**Verification:** PassAliases Jest suite passed (3 tests); TypeScript checks passed for `packages/components` and `packages/pass`; `git diff --check` passed.

Key files: [usePassAliasesProviderSetup.ts](/app/packages/components/components/drawer/views/SecurityCenter/PassAliases/usePassAliasesProviderSetup.ts), [PassAliasesProvider.helpers.ts](/app/packages/components/components/drawer/views/SecurityCenter/PassAliases/PassAliasesProvider.helpers.ts), [PassBridgeFactory.ts](/app/packages/pass/lib/bridge/PassBridgeFactory.ts).