# Checkpoint

Issue: support `TELEPORT_KUBE_CLUSTER` in `tsh` configuration with CLI cluster precedence; correct `TELEPORT_CLUSTER`/`TELEPORT_SITE` site selection and CLI precedence; normalize and apply `TELEPORT_HOME` even over CLI HomePath; preserve empty fields when unset.

Starting investigation: identify the CLI configuration initialization and existing environment precedence tests, implement narrowly, then run relevant existing tests.
