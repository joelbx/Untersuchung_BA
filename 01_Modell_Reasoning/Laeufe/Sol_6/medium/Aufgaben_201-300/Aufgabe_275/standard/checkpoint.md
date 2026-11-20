# Checkpoint

Task: preserve Kubernetes proxy authentication error classifications.

Completed: authenticate returns AccessDenied for access failures from setupContext and wraps other errors. Existing authentication table now checks that unknown local Kubernetes clusters and remote requests without a tunnel remain BadParameter and non-AccessDenied.

Validation: go test ./lib/kube/proxy -run '^TestAuthenticate$' -count=1; go test ./lib/kube/proxy -count=1; git diff --check. All passed.
