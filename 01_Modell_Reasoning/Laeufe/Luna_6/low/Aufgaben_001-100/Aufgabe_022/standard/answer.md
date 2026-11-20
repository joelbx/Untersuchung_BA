Updated RPM parsing so malformed source RPM filenames produce a warning while preserving the binary package, and epoch prefixes are included in parsed source package versions. Added regression cases in [redhatbase_test.go](/app/scanner/redhatbase_test.go).

`gofmt` completed. `go test ./scanner` was still running when I stopped polling, so I can’t confirm its result.