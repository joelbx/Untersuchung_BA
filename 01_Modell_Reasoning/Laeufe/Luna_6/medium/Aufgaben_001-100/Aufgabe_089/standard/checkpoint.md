Task: Fix CUE configuration validation and filesystem snapshot referential integrity.

Plan: Inspect repository guidance and current validation/snapshot implementation, make validation return a multi-unwrappable error with source locations, integrate validation into snapshot constructors, and run relevant existing tests.
