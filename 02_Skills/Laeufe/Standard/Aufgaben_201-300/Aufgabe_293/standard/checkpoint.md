# OCI storage issue checkpoint

Status: patched OCI configuration, validation, bundle root, server wiring, JSON schema, and integration test registration. `rg` is unavailable in this environment, so searches used `grep` and `find`.

Checks passed:
- `GOPROXY=off GOSUMDB=off go test ./internal/config ./internal/oci ./internal/storage/fs/oci ./internal/cmd ./cmd/flipt`
- `GOPROXY=off GOSUMDB=off go test ./testing -run '^$'` from `/app/build`
- `git diff --check`
- `python3 -m json.tool config/flipt.schema.json >/dev/null`

Uncertainty: the Dagger-backed `fs/oci` integration suite was registered and compiled but not executed locally; it needs the integration environment and service startup.
