# Checkpoint

Task: classify Kubernetes proxy authentication failures according to their underlying trace errors.

Status: investigating root cause. `rg` is unavailable (`/bin/bash: rg: command not found`); using local grep/find instead. No source edits yet.

Root cause evidence: `Forwarder.authenticate` (forwarder.go) unconditionally replaces every `setupContext` error with `trace.AccessDenied`. `setupContext` preserves `trace.BadParameter` for missing reverse tunnel; `kubeutils.CheckOrSetKubeCluster` returns `BadParameter` for an unknown explicit Kubernetes cluster. Existing `TestAuthenticate` incorrectly expects `AccessDenied` for both. Other access failures (unsupported user, authz denial, remote user to remote cluster) are already classified as access denied.

Hypothesis: preserving `setupContext` errors with `trace.Wrap(err)` will retain their trace classification while keeping access-related errors classified as access denied.

Reproduction: `GOPROXY=off GOSUMDB=off go test ./lib/kube/proxy -run '^TestAuthenticate$' -count=1` failed in exactly the missing tunnel and unknown cluster cases after changing test expectations. Applied one-line fix: `authenticate` returns `trace.Wrap(err)` for `setupContext` failures. Same focused command now passes. Existing `setupContext` classifications are unchanged.

Specified httplib interfaces: `ErrorWriter`, `MakeHandlerWithErrorWriter`, and `MakeStdHandlerWithErrorWriter` were absent. Added a focused test that initially failed to compile with the undefined identifiers. Implemented the wrappers, using the existing handlers as callers with `trace.WriteError`. Initial wrapper test failed because its expected JSON had a trailing newline; inspected output, corrected the test expectation, and reran.

Final verification: `GOPROXY=off GOSUMDB=off go test ./lib/httplib ./lib/kube/proxy -count=1` passed (both packages). `git diff --check` passed. Compiler emitted an existing warning from the sqlite3 C dependency but test exit code was 0. No source edits to `setupContext`; no downloads.
