Implemented token lifecycle utilities in [src/api/utils.js](/app/src/api/utils.js): listing, generation, retrieval, description updates, deletion, usage logging, and last-seen lookup. Tokens now use the requested records and sorted indexes, with numeric timestamps and aligned last-seen results.

Connected user token creation/deletion and bearer authentication to the utilities, retaining fallback support for tokens in existing settings.

ESLint, JavaScript syntax checks, and `git diff --check` passed. The existing authentication test could not start because Redis at `127.0.0.1:6379` refused the connection.