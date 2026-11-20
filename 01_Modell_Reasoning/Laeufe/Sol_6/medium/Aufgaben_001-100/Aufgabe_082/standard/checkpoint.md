Task: fix multi-backend auth audit log initialization and stdout emitter.
Status: complete. WriterEmitter emits newline-delimited JSON, MultiLog validates and fans out emitters, stdout uses WriterEmitter, and regression tests cover fanout and URI-list initialization.
Verified: full lib/events suite passed on rerun; focused lib/service tests passed. Initial full lib/events run hit an existing one-second timestamp boundary in TestBasicLogging, which passed on rerun. git diff --check passed.
