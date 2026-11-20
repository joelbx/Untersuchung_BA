# Checkpoint

Task: Accept minimal collection manifest configurations and handle absent manifest via Sentinel.
Status: Complete.
Changes: Metadata normalization preserves an absent manifest as Sentinel. The files manifest builder uses the Sentinel to select directory walking and applies build_ignore there. Explicit empty or null manifests select default directive handling. Directory walking excludes file symlinks outside the collection; internal symlinks remain represented at their linked path.
Verification: `PYTHONPATH=/app/lib python -m pytest -q -o addopts='' test/units/galaxy` passed (215 tests). `git diff --check` passed.
Constraint: No git history, index baseline, or harness configuration changes.
