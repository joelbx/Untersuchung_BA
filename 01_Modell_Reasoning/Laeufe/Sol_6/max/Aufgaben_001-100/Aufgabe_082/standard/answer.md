Fixed auth startup with multiple audit backends. `stdout://` now uses `WriterEmitter` to write newline-delimited JSON events, and `MultiLog` validates emitters and fans events out across backends. Added coverage for emission, errors, closure, and multi-URI initialization.

The existing `events`, `service`, and `config` test suites pass.