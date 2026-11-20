`detectScanDest` now returns an IP-to-ports map. It deduplicates and sorts each IP’s ports and returns an empty map when no listening ports are found. I updated `execPortsScan` to consume the map and added test coverage for multiple ports and wildcard overlap.

The focused tests, full `./scan` test suite, and `git diff --check` passed.