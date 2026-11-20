Role: Go service listener specialist
Task: use bound auth and proxy listener addresses throughout lib/service/service.go.
Status: implementation complete.
Changes: auth SSH bind updates configured auth address and matching AuthServers entries. Proxy listeners now include SSH; bound web, tunnel, kube, and SSH addresses update proxy configuration before handlers and services are built. SSH listener is closed with proxy listeners and on initialization failure.
Validation: gofmt; git diff --check; GOPROXY=off GOSUMDB=off go test ./lib/service -run 'TestMonitor|TestConfig|TestProcessStateGetState' -count=1 (pass); GOPROXY=off GOSUMDB=off go test ./lib/service -count=1 (pass).
Scope: service.go only, plus this required checkpoint. No git history/index or harness changes.
