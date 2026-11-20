# Checkpoint

Implemented `-wp-ignore-inactive` in scan, report, and tui flags; added `WpIgnoreInactive` to global config and TOML loading. WordPress vulnerability lookup filters inactive packages before API calls, honoring the new setting, the setting saved with scan results, and the existing per-server setting. Added tests for filtering and TOML loading.

Verification: `GOPROXY=off GOSUMDB=off go test -p 1 ./wordpress ./config` and `GOPROXY=off GOSUMDB=off go test -p 1 ./commands ./report` passed. `git diff --check` passed. First concurrent test run had a transient vet import error; rerun of affected packages passed.
