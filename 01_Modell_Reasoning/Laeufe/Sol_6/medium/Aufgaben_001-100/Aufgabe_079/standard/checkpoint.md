Task: Restore scanner directory traversal to native OS filesystem paths.
Status: Complete. Walker uses absolute OS paths, os.Stat/os.Open, OS symlink and ignore checks, and os.ReadDir for audio listing. Added utils.IsDirReadable; updated scanner tests and Windows ignore coverage call signatures.
Verification: GOPROXY=off go test ./scanner ./utils passed; git diff --check passed.
