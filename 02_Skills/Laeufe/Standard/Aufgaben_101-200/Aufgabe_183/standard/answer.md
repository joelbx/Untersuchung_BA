Updated [Ubuntu lifecycle data](/app/config/os.go) so 20.04 has extended support through April 1, 2030, and 22.04 is recognized with standard support through April 1, 2027 and extended support through April 1, 2032. Added boundary tests in [config/os_test.go](/app/config/os_test.go).

Offline tests passed for `./config`, `./models`, and `./scanner`; `git diff --check` passed.