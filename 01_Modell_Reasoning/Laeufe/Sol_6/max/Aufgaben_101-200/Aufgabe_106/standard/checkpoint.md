# WordPress cache and inactive package filtering

Status: complete.

Changed the WordPress cache to pass the map directly and use nullable string values. `searchCache` returns `("", false)` for missing keys and nil values, while preserving present empty strings. The WordPress scan now honors each server's `IgnoreInactive` setting and the existing report flag; report filtering honors the same settings. Inactive themes and plugins are excluded by their `Status` field.

Verification: `GOPROXY=off GOSUMDB=off go test ./wordpress ./models ./report` passed. `git diff --check` passed. The report build emitted an existing sqlite C compiler warning.
