Task: Fix Ubuntu lifecycle metadata for 20.04 and 22.04.
Completed: Added Ubuntu 20.04 extended support through 1 April 2030; added Ubuntu 22.04 standard/extended support through 1 April 2027/2032; enabled 22.04 in Gost Ubuntu CVE release allowlist. Added lifecycle boundary and release support tests.
Validation: GOPROXY=off GOSUMDB=off go test ./config passed; GOPROXY=off GOSUMDB=off go test ./gost -run '^TestUbuntu_Supported$' -count=1 passed; git diff --check passed.
