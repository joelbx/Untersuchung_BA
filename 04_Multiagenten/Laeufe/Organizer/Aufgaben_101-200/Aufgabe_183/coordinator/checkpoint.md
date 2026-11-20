# Checkpoint

Issue: Ubuntu 20.04 extended support and Ubuntu 22.04 lifecycle recognition.

Implemented: Ubuntu 20.04 extended support through 1 April 2030; Ubuntu 22.04 standard support through 1 April 2027 and extended support through 1 April 2032. Added date and boundary coverage in config tests.

Verified: `GOPROXY=off GOSUMDB=off go test ./config` and `GOPROXY=off GOSUMDB=off go test ./models` passed; `git diff --check` passed.

Delegation: none; solved directly.
