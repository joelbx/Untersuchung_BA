Amazon Linux 2023 is now recognized from `/etc/system-release`, has an EOL mapping, and gets ALAS2023 advisory links. Release normalization and EOL mappings also cover 2025, 2027, and 2029; unrecognized releases return `found=false`.

The relevant tests passed: `GOPROXY=off GOSUMDB=off go test ./config ./scanner ./oval`.