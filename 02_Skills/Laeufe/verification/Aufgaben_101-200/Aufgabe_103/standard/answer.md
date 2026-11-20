Updated the RPM parsers to preserve empty release fields in installed-package and repoquery output, build source package versions without a trailing hyphen, and validate source RPM filenames including `-src.rpm` and hyphenated releases. Added regression tests for those cases and update candidate parsing.

Verification: `GOPROXY=off GOSUMDB=off go test ./scanner -count=1` passed.