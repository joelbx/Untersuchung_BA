Updated Ubuntu lifecycle data: 20.04 has extended support through April 1, 2030, and 22.04 has standard support through April 1, 2027 and extended support through April 1, 2032. I also enabled 22.04 in the Gost and OVAL CVE lookup paths and added lifecycle tests.

Validation passed: `go test ./config ./gost ./oval` with downloads disabled.