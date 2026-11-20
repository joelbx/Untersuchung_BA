Added Amazon Linux 2023, 2025, 2027, and 2029 version recognition and EOL dates. The scanner now detects those releases from `/etc/system-release`, and ALAS2023 advisories get the correct source links. Unrecognized releases remain unmatched.

`go test ./config ./scanner ./oval` passed.