Task: preserve source-specific Trivy CVE contents, severity, CVSS, references, and dates across converter, library detection, models, and TUI.
Status: implemented source-specific contents in both Trivy paths, model aggregation, and TUI references. Added converter regression test. Relevant Go packages pass; git diff --check passes.
