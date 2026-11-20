Task: Fix teleport-kube-agent Kubernetes backend environment variable handling in /app.
Status: Complete. Exported NamespaceEnv and ReleaseNameEnv; all backend namespace/release environment reads use them. Existing backend tests now set required environment variables explicitly, and constructor tests cover missing variables, config values, and release metadata.
Verification: gofmt and git diff --check passed. GOPROXY=off GOSUMDB=off GOTOOLCHAIN=local go test ./lib/backend/kubernetes passed.
