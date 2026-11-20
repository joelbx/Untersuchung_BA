# Checkpoint

Issue: YAML filters serialize `AnsibleUndefined` as a low-level YAML representation error.

Plan: inspect the dumper/filter code and existing tests, make undefined values trigger Jinja's undefined behavior during dumping, wrap YAML failures in filter-specific `AnsibleFilterError`, and run relevant existing tests.
