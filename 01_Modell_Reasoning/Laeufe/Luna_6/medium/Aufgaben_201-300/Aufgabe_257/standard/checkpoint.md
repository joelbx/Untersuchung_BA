# Checkpoint

Task: resolve testability issues in tsh SSO login, listener address propagation, and command error handling.

Initial state: working tree status and code search pending. External research is intentionally excluded; inspect repository code and existing tests only.

Plan: inspect target implementations and call sites, implement the public SSO override and runtime listener address propagation, convert command handlers/dispatch/refuseArgs to return errors, then run relevant existing tests.
