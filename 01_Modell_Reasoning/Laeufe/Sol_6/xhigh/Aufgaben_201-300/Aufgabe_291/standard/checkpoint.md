# Checkpoint

Task: Add NVD CVSS v4.0 storage, conversion, and aggregation alongside MITRE.

Status: Complete. CveContent already contained the required fields. Updated go-cve-dictionary to the cached version that exposes Nvd.Cvss40, copied NVD v4 metrics into source-specific CveContent rows, and aggregated v4 scores in MITRE then NVD order. Added focused tests for conversion and aggregation.

Verification: Offline focused tests, full models tests, and detector tests passed. `git diff --check` passed.
