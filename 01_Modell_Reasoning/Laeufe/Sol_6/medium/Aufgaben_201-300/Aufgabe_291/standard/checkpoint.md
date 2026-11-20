# Checkpoint

Task: Add NVD CVSS v4.0 storage, conversion, and aggregation in source order Mitre, Nvd.
Completed: CveContent fields already existed. NVD conversion now fills them by metric source; aggregation includes Nvd after Mitre. Updated go-cve-dictionary to the locally cached version exposing Nvd.Cvss40. Added conversion and aggregation tests.
Verification: GOPROXY=off GOSUMDB=off go test ./models ./detector passed; git diff --check passed.
