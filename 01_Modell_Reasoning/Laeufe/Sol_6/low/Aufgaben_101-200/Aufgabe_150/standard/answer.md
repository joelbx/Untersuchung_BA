Updated collection metadata handling so an absent `manifest` uses `Sentinel`. Explicit `manifest: {}` and `manifest: null` now select manifest directive handling. The default file walk still applies `build_ignore`, excludes symlinks pointing outside the collection, and includes internal symlinks once under their linked path.

Validation: all 213 Galaxy unit tests passed.