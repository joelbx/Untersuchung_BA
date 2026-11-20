Task: fix tsh testability, SSO injection, dynamic auth/proxy listener addresses, and handler error propagation.
Status: implemented in checked-out files. Run and every tsh command handler return errors; main alone reports fatal errors. Runtime CLI options can inject mock SSO login. Auth and proxy configurations use bound listener addresses, including SSH proxy listener.
Verification: go test ./tool/tsh ./lib/client ./lib/service passed; go test ./lib/service -run '^TestMonitor$' -count=1 passed after adding an auth-address assertion. Added SSO callback and Run error-return tests. Final formatting/diff review pending.
Constraints: local code/tests only; no git history, index, or harness changes.
