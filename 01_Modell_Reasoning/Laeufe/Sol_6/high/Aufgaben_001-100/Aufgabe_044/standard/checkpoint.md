Task: Fix namespace authorization so users can list and navigate only namespaces they may view without access to default.
Status: Implemented and verified.
Changes: Namespaces verifier method; bundle and rego viewable_namespaces evaluation and result validation; middleware context propagation; authorized namespace filtering before pagination and count; UI selection and redirect from inaccessible or unscoped routes; role mapping and error tests.
Verification: `GOPROXY=off GOSUMDB=off go test ./internal/server/authz/... ./internal/server -count=1` passed. `GOPROXY=off GOSUMDB=off go test ./internal/cmd -run '^$' -count=1` passed. `git diff --check` passed. UI dependencies are absent, so UI tests could not be run locally without downloads.
Constraints observed: local code/tests only; no git history, index, or harness configuration changes.
