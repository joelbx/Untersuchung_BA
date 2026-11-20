Task: fix password lookup key=value parameter handling, chars formats, defaults, and seed determinism.
Status: implementation complete; password lookup unit suite passes (33 tests).
Changes: parsing is now LookupModule._parse_parameters; run resolves plugin options before parsing; chars accepts raw list or comma-separated string; term options override plugin options. Tests cover precedence and deterministic seed.
Delegation: none.
