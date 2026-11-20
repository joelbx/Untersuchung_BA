Fixed `onSSH` so a successful node lookup no longer hides the original SSH error. `Run` now receives that error as intended.

The reviewer’s checks passed: `go test ./tool/tsh ./lib/client ./lib/service` and `git diff --check`. No remaining failures or test environment problems.