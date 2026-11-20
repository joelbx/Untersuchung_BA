# Checkpoint

Task: fix Kubernetes kubeconfig proxy address selection for `tctl auth sign --format=kubernetes`.

Plan: inspect `ProxyConfig` address handling and kubeconfig generation; implement canonical Kubernetes address selection with fallback through registered proxies; update/add focused tests and run existing relevant tests.
