Updated [redhatbase.go](/app/scanner/redhatbase.go:634) so malformed source RPM filenames add a scan warning, skip the source package, and keep the binary package. Epochs in source filenames are now included in the parsed source version without duplicating the binary epoch. The fix applies to both RPM and repoquery parsing.

`go test ./scanner` passed. `git diff --check` passed.