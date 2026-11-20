# Checkpoint

Task: Fix RPM installed-package parsing for non-standard `SOURCERPM` filenames and epoch-bearing source filenames.

Completed: `scanner/redhatbase.go` shares source-package parsing between installed-package and repoquery lines. Malformed source filenames append a scanner warning and skip only source metadata while preserving the binary package. `splitFileName` extracts numeric epochs from the filename prefix and includes them in the parsed version. Source package versions avoid duplicate epochs, retain `Arch: "src"`, and preserve the binary-name link.

Validation: `gofmt` and `git diff --check` pass. Existing tests passed:
- `go test ./scanner -run 'Test_redhatBase_parseInstalledPackagesLine$|Test_redhatBase_parseInstalledPackagesLineFromRepoquery$'`
- `go test ./scanner -run '^Test_redhatBase_parseInstalledPackages$'`

The full `go test ./scanner` run was stopped after remaining silent for over two minutes; the focused parser tests completed successfully.
