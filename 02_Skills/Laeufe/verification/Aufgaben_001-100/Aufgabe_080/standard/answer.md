The album grid now requests square covers. The artwork API centers non-square images on a transparent square background, returns those images as PNG, and uses separate cache keys for square and original-shape versions.

Verification passed: Go tests for `core/...` and `server/...`, plus ESLint and Prettier checks for the changed UI files.

The listed OCI `Source` interfaces were not added: this checkout has no `internal/storage` tree or OCI snapshot types.