# Checkpoint

Updated `detector/wordpress.go` to map Enterprise summary, proof of concept, introduced version, and CVSS v3 fields. Records now use the first CVE, keep references in order, normalize timestamps to UTC, and use an empty optional map when no optional fields exist. Added JSON converter coverage for Enterprise, omitted, and null field payloads in `detector/wordpress_test.go`. `GOPROXY=off GOSUMDB=off go test ./detector` passed; `git diff --check` passed.
