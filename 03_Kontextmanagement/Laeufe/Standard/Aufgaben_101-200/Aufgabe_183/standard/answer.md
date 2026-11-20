Updated [Ubuntu lifecycle data](/app/config/os.go) so 20.04 has extended support through April 1, 2030, and 22.04 is recognised with standard support through April 1, 2027 and extended support through April 1, 2032. Added [regression tests](/app/config/os_test.go) for the dates and extended support checks.

`go test ./config` and `git diff --check` passed.