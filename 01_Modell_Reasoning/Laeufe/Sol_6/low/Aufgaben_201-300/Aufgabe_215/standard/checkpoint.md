Task: add HTTPS configuration and serving support.
Status: implemented configuration, validation, REST/UI TLS, gRPC TLS, and gateway TLS.
Verification: go test ./cmd/flipt passed; git diff --check passed.
