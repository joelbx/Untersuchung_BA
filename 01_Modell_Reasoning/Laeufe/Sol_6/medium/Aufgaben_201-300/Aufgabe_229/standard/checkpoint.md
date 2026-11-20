# Image cleanup issue

Implemented cleanup of user cover and avatar variants in `src/user/picture.js`, including safe local URL mapping, path lookup helpers, and centralized field clearing. Socket handlers delegate to these functions and retain removal hooks. Account deletion invokes both cleanup functions. Group cover removal deletes local cover and thumbnail files before clearing all cover fields.

Validation: ESLint, `node --check`, and `git diff --check` pass for changed source files. Targeted existing Mocha user tests could not start: the configured Redis test database refused connection at 127.0.0.1:6379.
