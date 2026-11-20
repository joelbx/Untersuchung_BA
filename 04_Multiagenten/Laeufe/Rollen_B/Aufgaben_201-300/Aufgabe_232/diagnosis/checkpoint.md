Progress: fault localization complete. No project source or tests changed.

Findings:
- config/config.go owns OS family constants and Distro.MajorVersion; no config/os.go or EOL model/lookup exists.
- scan/serverapi.go:GetScanResults converts each target then appends results, with no EOL evaluation. scan/base.go:convertToModel copies only existing l.warns into ScanResult.Warnings. ViaHTTP creates a result separately.
- report/util.go:formatScanSummary renders the warnings slice as one Go slice with `Warning for <server>:`; it does not emit ordered `Warning: <message>` lines.
- oval/util.go:major and gost/util.go:major duplicate extraction; oval implementation slices at a dot and can panic if absent. config.Distro.MajorVersion has separate Amazon logic; config imports cannot use util.Major directly because util imports config.
- scan/redhatbase.go:detectRedhat distinguishes Amazon v1/v2 by token pattern, but v2 release strings may need canonicalization to `2 (Karoo)`. Other detectors pass patch-level release strings, so EOL lookup needs family-specific normalization.
- Existing tests: config/config_test.go covers Amazon MajorVersion; oval/util_test.go covers epoch parsing. No EOL tests or scan-summary warning tests found.
