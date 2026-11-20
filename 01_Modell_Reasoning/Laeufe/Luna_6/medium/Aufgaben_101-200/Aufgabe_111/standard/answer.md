Added Amazon Linux 2023, 2025, 2027, and 2029 detection, EOL mappings, and regression tests. Legacy `YYYY.MM` versions still resolve to Amazon Linux 1; unrecognized versions return `unknown` and have no EOL mapping.

`go test ./config ./scanner` passed.