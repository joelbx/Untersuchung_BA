Implemented parent-domain blocking, early whitelist overrides, trailing-dot normalization, and the `widened_hostnames` utility with edge-case coverage.

The URL utility tests passed. Host-blocking tests passed except for the pre-existing `test_disabled_blocking_per_url` failure, which remains after the changes.