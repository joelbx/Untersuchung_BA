# Checkpoint

Task complete: Amazon Linux 2023 and specified future releases are normalized in configuration and OVAL lookup. EOL dates are mapped through 2029. Scanner parses release strings including legacy AMI form. ALAS2023 advisory links are generated. Extended support check has the correctly spelled method with the existing misspelled method retained for compatibility.

Verification: `GOPROXY=off GOSUMDB=off go test ./config ./scanner ./models ./oval` passed in package runs. `git diff --check` passed. No delegation used.
