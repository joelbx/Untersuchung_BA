Added `proxy_service.kube_listen_addr` to enable the Kubernetes proxy, with the Kubernetes default port when no port is supplied. Config validation rejects it alongside an enabled legacy Kubernetes block and accepts it when that block is explicitly disabled.

Client address resolution now replaces wildcard Kubernetes hosts with the web proxy host and prefers configured Kubernetes public addresses. I also corrected standalone Kubernetes listen address parsing and added the requested warning.

`go test ./lib/config ./lib/client -count=1` and `git diff --check` passed.