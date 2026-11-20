# Checkpoint

Issue: config loading must retain `Default()` values for omitted settings and load DB pool settings plus `meta.check_for_updates`.

Plan: inspect `config/config.go`, its existing tests, and shipped configs; implement the loader/default merge behavior while preserving existing fields; run relevant existing config tests.
