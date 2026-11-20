Updated the EOL data in [config/os.go](/app/config/os.go): corrected Fedora 37 and 38 dates, added Fedora 40, updated SUSE Desktop and Server dates, and marked macOS 11 ended while adding macOS 15.

Extended the Windows rollups in [scanner/windows.go](/app/scanner/windows.go) for builds 19045, 22621, 22631, and 20348. All added entries use named struct literals, and the prior mappings remain in revision order. Updated the existing tests and added kernel-version boundary checks.

The focused `config` and `scanner` Go tests pass; `git diff --check` also passes.