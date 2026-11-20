# Debugging checkpoint

Task: restore whitespace parsing for scalar string values decoded into `[]string` in configuration, including YAML and ENV.

Status: patch complete; config tests passed. Initial inspection shows `rg` is unavailable; using local `find`/`grep` instead.

## Root cause and pattern

`Load` calls `v.Unmarshal` with `decodeHooks`; the current `mapstructure.StringToSliceHookFunc(",")` splits any string targeting a slice using commas. The library hook checks only the target kind (`Slice`), not exact `[]string`. `CorsConfig.AllowedOrigins` is `[]string`; its YAML value and ENV override both flow through that same hook. `advanced.yml` currently uses `foo.com,bar.com`, so the existing YAML/ENV test covers comma parsing. The library hook returns an empty non-nil slice for an empty string. A local hook using `strings.Fields` should preserve that empty-slice behavior and split all whitespace, with exact target type checking.

## Implementation and verification

Added a failing test before the fix. Before implementation, `GOPROXY=off GOSUMDB=off go test ./internal/config -run 'TestLoadAllowedOriginsFromScalar|TestStringSliceDecodeHookOnlyConvertsStringsToStringSlices' -count=1` exited 1: whitespace inputs stayed in one entry for YAML and ENV, and a string to `[]int` was incorrectly transformed to `[]string`.

Replaced the generic comma hook with an exact `[]string` hook using `strings.Fields`, returning `[]string{}` for empty input. Changed the advanced fixture to a whitespace-separated value.

`GOPROXY=off GOSUMDB=off go test ./internal/config -count=1` exited 0. `git diff --check` exited 0.

Broader check: `GOPROXY=off GOSUMDB=off go test ./internal/... -count=1`. It reported failures in `internal/server/cache/redis` because the Docker daemon is unavailable (`Cannot connect to the Docker daemon at unix:///var/run/docker.sock`). This is unrelated to config parsing. The command ultimately exited 1; the other reported internal packages, including config, passed. Docker-dependent Redis tests remain unverified.
