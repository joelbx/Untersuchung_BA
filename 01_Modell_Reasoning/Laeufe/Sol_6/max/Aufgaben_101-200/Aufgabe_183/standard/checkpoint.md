# Checkpoint

Task: Correct Ubuntu lifecycle metadata for 20.04 and add 22.04.
Status: Complete.
Changes: Added Ubuntu 20.04 extended support through 2030-04-01; added Ubuntu 22.04 standard support through 2027-04-01 and extended support through 2032-04-01. Added lifecycle boundary regression cases.
Validation: `go test ./config ./models` and `go test ./scanner` passed; `git diff --check` passed.
