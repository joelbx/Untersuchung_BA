Resolved the tsh test environment failures. `Run` and its command handlers now return errors, runtime options can be applied after parsing, and a mock SSO login function is passed through to the client. Auth and Proxy services now propagate their OS assigned listener addresses, including ports chosen for `:0`.

I added regression coverage for returned CLI errors and dynamic proxy addresses. The client, service, and tsh package tests pass with module network access disabled; `git diff --check` passes.

Three subagents handled the client, service, and `tsh.go` edits. I integrated the database handler changes and tests, then verified the final patch.