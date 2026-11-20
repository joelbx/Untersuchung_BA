Task: Correct Ubuntu lifecycle metadata for 20.04 and 22.04.
Status: Added Ubuntu 20.04 extended support through 2030-04-01 and Ubuntu 22.04 standard/extended support through 2027-04-01/2032-04-01. Enabled 22.04 in Gost's Ubuntu CVE release gate and added regression cases.
Validation: `GOPROXY=off GOSUMDB=off go test ./config ./gost` passed; `git diff --check` passed.
