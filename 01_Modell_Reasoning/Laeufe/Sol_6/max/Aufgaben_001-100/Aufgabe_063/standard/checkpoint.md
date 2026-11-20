# Kubernetes proxy shorthand work

Objective: add `proxy_service.kube_listen_addr` shorthand, preserve legacy behavior, detect conflicts, and fix Kubernetes address selection and warnings.

Status: implemented shorthand parsing, conflict validation, Kubernetes service listen parsing, warning, and client wildcard address resolution. Updated configuration reference and added focused regression coverage.

Validation: `GOPROXY=off GOSUMDB=off go test -mod=vendor ./lib/config ./lib/client` passed after the final changes. `git diff --check` passed.
