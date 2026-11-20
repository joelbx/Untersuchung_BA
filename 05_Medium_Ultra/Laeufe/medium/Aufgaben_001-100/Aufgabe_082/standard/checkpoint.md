# Checkpoint

Resolved the multi-backend auth startup failure. `MultiLog` now validates and embeds a `MultiEmitter`; `stdout://` uses `WriterEmitter`, which writes newline-delimited JSON events and closes its writer. Added focused emitter tests and expanded the external log URI test to cover stdout and a two-URI configuration.

Verification: `go test ./lib/events ./lib/service -run 'TestWriterEmitter|TestMultiLog|TestInitExternalLog' -count=1` passed (service gocheck case requires separate invocation); `go test ./lib/service -run '^TestConfig$' -check.f TestInitExternalLog -count=1 -v` passed; `git diff --check` passed.
