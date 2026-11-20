Amazon Linux 2023 now parses from `/etc/system-release`, and ALAS2023 advisories get the corresponding source links. Version normalization and EOL mappings cover 2023, 2025, 2027, and 2029; unrecognized releases remain unfound. I added tests for version handling and EOL boundaries.

`go test ./config ./scanner ./oval` passed with dependency downloads disabled.