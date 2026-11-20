# Checkpoint

Task: align OS EOL data and Windows KB mappings.

Changes:
- Updated Fedora 37/38 cutoffs, added Fedora 40, added SUSE Enterprise Desktop/Server 13 and 14 dates, marked macOS 11 ended, and added macOS 15.
- Appended named Windows rollup entries for 19045, 22621, 22631, and 20348 in revision order.
- Updated existing expectations and added EOL and Windows rollup/detection tests.

Verification:
- `GOPROXY=off GOSUMDB=off go test ./config ./scanner` exited 0: both config and scanner passed.
- `git diff --check` exited 0.
- `test -z "$(gofmt -l config/os.go config/os_test.go scanner/windows.go scanner/windows_test.go)"` exited 0.
- Local script checked each specifically requested KB is present in its build branch; all 19045 (14), 22621 (14), 22631 (14), and 20348 (9) entries were found.

No offline tooling blockers occurred. No external source verification was possible under task constraints; revision and KB values follow the issue's requested mapping and local data conventions.
