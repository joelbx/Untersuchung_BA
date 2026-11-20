Task: automatic cleanup of uploaded files on post and topic purge, with ACP preservation setting.
Status: implemented and verified.
Changes: purge dissociates uploads, deletes only orphaned originals and resized copies; deleteFromDisk accepts strings/arrays, rejects other top-level inputs, ignores invalid or escaping paths; topic thumbnail purge respects shared references and preservation; ACP setting defaults to off.
Verification: mocha test/posts/uploads.js test/topics/thumbs.js --exit (55 passing); eslint on changed JavaScript passed; git diff --check passed.
