Task: add configurable nmap host port scanning with validation while retaining native scanning.
Workflow: test first, verify red, implement, verify green and full suite.
Environment: rg unavailable; using grep/find. No external downloads.
Implemented PortScanConf with technique mapping, validation, per-server TOML activation, nmap XML scanning, native fallback, and discover template example. Preserved existing port correlation entry point.
TDD: config tests initially failed on missing PortScanConf API; external scanner test failed with empty ports; default connect/source port test failed; stderr/XML test failed with empty ports. Each passed after implementation.
Verification: go test ./config ./scanner -count=1 passed. go test ./... passed after final patch. Existing github.com/mattn/go-sqlite3 C compiler warning appeared; no Go test failures. git diff --check passed.
