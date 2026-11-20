# Checkpoint

Task: fix auth service crash when multiple audit event backends include stdout.

Completed: WriterEmitter writes JSON audit events with a newline and closes its writer; MultiLog validates emitters, fans out events, and closes all loggers; stdout backend uses WriterEmitter. Added tests for emission, validation, fanout, close errors, and combined file/stdout configuration.

Verification: focused lib/events tests passed; focused lib/service TestInitExternalLog passed; git diff --check passed.
