Task: implement proxy_service.kube_listen_addr shorthand and related validation/address behavior.
Status: implementation complete; go test ./lib/config ./lib/client running.
Changes: shorthand parsing, conflict validation, warning, wildcard client host resolution.
