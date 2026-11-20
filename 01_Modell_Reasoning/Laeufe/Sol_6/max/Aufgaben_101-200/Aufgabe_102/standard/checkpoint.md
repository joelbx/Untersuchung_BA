# Checkpoint

- Task: add Linux locally reachable (scope host) IPv4 and IPv6 facts in the existing network fact workflow.
- Status: implemented `locally_reachable_ips` with IPv4 and IPv6 lists from local/host-scope routes; added selector documentation, usage documentation, a changelog fragment, and unit tests.
- Verification: network and fact workflow unit tests passed (197 passed, 7 skipped); Python compilation and `git diff --check` passed. The workspace has no `ip` executable, so route output was verified with unit fixtures.
- Status: implementation and verification complete.
- Constraints: use local repository code and tests only; preserve existing fact behavior and git history.
