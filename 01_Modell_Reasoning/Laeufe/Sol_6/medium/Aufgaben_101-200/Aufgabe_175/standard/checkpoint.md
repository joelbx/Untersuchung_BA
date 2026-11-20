Task complete: native SQLite backup/restore, CLI commands, scheduling, configuration, and pruning.
Implemented: backup config validation and startup directory creation; SQLite online backup/restore and timestamp-based retention; backup create/prune/restore CLI with confirmation; periodic backup and pruning; integration test.
Verification: go test ./... passed; focused backup integration test passed.
Constraints observed: local code/tests only; git history/index/harness unchanged.
