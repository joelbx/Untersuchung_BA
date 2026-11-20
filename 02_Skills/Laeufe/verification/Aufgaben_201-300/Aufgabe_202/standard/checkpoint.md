# Checkpoint

Task: validate the admin upload target directory against the configured upload base path; reject missing directories with HTTP 500 and `[[error:invalid-path]]`.

Change: `src/controllers/admin/uploads.js` checks that the resolved folder remains under `nconf.get('upload_path')` and that `fs.promises.stat` identifies an existing directory before saving. Missing paths, non-directory components, and file targets use the existing invalid-path error. `test/uploads.js` covers a missing folder and a file used as a folder.

Verification:
- `./node_modules/.bin/eslint src/controllers/admin/uploads.js test/uploads.js` exited 0.
- `git diff --check` exited 0.
- Initial `./node_modules/.bin/mocha test/uploads.js --grep 'should (upload regular file|fail to upload regular file in wrong directory|reject an upload)'` exited 1 before tests ran: `connect ECONNREFUSED 127.0.0.1:6379`.
- Started the locally installed Redis server with `redis-server --port 6379 --save '' --appendonly no --daemonize yes`.
- Repeated the focused Mocha command: 4 passing, exit 0.
- `./node_modules/.bin/mocha test/uploads.js`: 43 passing, exit 0.
