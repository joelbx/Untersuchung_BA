Task: align OS EOL data and Windows KB mappings.
Status: complete. Updated EOL entries, appended modern Windows KB rollups, and adjusted existing tests plus a focused modern detection test.
Validation: go test ./config ./scanner passed; git diff --check passed.
Constraints: preserved existing mapping entries and git baseline; used local code and tests only.
