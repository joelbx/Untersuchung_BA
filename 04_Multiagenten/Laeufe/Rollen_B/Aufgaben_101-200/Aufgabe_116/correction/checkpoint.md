Correction round started: inspecting current chat privilege patch and reviewer findings.
Reviewed patch and reviewer findings. Added chat:privileged to the middleware privilege-set expectation. Running the reviewer test commands.
Verification: Redis was initially unavailable; started existing local redis-server. messaging.js: 79 passing. middleware.js + controllers.js: 152 passing, 1 unrelated export failure at test/controllers.js:1692 (export-profile.js:61). controllers.js alone: 140 passing, same export failure. git diff --check clean.
