Task: externalize MIME and lossless format definitions.
Status: implemented and verified.
Changes: moved built-in definitions from consts/mime_types.go to resources/mime_types.yaml; added mime package with conf.AddHook loader using resources.FS (embedded default plus DataFolder/resources override); updated server UI config and model startup registration; added focused MIME loader test.
Verification: go test ./mime ./model ./server ./core passed; git diff --check passed.
