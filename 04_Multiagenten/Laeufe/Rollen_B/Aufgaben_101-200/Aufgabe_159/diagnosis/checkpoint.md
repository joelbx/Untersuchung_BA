# Progress

Fault localization complete. `parsePkgName` is absent from this checkout. In `reporter/sbom/cyclonedx.go`, `libpkgToCdxComponents` (line 263) and `ghpkgToCdxComponents` (line 294) pass whole package names as the PURL name with empty namespace and subpath. The first uses `string(libscanner.Type)` and the second uses `m.Ecosystem()`; `models/github.go` maps Go to `gomod`, Maven to `pom`, and Python to `pip` or related names, which may need mapping to the requested PURL types. No tests exist under `reporter/sbom`. Source and tests remain unchanged.
