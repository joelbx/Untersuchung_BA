Resolved the collection manifest issue. A missing `manifest` now uses `Sentinel`; explicit `{}` and `null` are accepted as minimal manifest configurations. The `Sentinel` path still applies `build_ignore`, excludes symlinks pointing outside the collection, and includes internal links once.

Validation passed: 69 collection tests and 56 collection install tests.