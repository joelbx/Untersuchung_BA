Resolved the tsh test environment issue. Command handlers and `Run` now return errors, runtime options can inject an SSO login handler, and Auth and Proxy use their OS assigned listener addresses.

The existing tests passed for `tool/tsh`, `lib/client`, and `lib/service`. The work item is complete.