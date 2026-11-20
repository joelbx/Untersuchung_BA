Task: Export DefaultConfig and DecodeHooks; make Load use exported hooks; align storage pointers with requested API.
Completed: Moved canonical defaults from config_test.go into config.go; existing test helper now calls exported DefaultConfig. Exported DecodeHooks and composed them in Load using a copied slice plus the experimental skip hook. Added Version mapstructure tag. Changed Storage.Local/Git to pointers and guarded validation for missing sections. Updated existing storage test expectations to pointer literals.
Verification: go test ./internal/config passed; go test ./internal/cmd ./internal/cue passed; git diff --check passed.
Delegation: none.
