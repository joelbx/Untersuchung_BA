# Checkpoint

Task: Correct Ubuntu 20.04 extended support lifecycle and add Ubuntu 22.04 lifecycle metadata.
Status: Complete.
Changes: Added Ubuntu 20.04 extended support through 2030-04-01; registered Ubuntu 22.04 standard support through 2027-04-01 and extended support through 2032-04-01; enabled Ubuntu 22.04 Gost CVE lookup; added focused regression tests.
Verification: GOPROXY=off GOSUMDB=off go test ./config ./gost passed; git diff --check passed.
