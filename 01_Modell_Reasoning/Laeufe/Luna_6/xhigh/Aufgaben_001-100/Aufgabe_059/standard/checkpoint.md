# Checkpoint

Task: Resolve the `ModalTwo` JSDOM dialog incompatibility in `/app`.

Initial findings: the repository is a Yarn workspace with installed dependencies; `rg` is unavailable in this environment, so use `find`/`grep` for repository searches. The existing `ModalTwo` renders a closed `<dialog>` because it never sets `open`; its tests mock portals and use DOM queries. Git reported no existing working-tree changes.

Implementation complete: added the public `forwardRef` Dialog abstraction with native dialog feature detection, an accessible div fallback, `aria-*`/`data-*` typing, forwarded attributes/ref, and a package export. `ModalTwo` now uses it with `open` and `aria-modal`; the focus trap accepts the dialog ref type.

Verification: `components/modalTwo/ModalTwo.test.tsx` passed (8 tests), and `yarn workspace @proton/components check-types --pretty false` passed. `git diff --check` is clean.
