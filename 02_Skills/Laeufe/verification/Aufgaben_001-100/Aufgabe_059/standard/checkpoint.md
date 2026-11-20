# Checkpoint

Task: Resolve ModalTwo JSDOM dialog accessibility through a Dialog abstraction.

Implemented: Added public `Dialog` component and export. It renders a native dialog when `showModal` is supported and an accessible div host otherwise, forwarding props, children, and ref. ModalTwo uses this component and marks active dialogs open.

Verification:
- Before implementation, `../../node_modules/.bin/jest components/modalTwo/ModalTwo.test.tsx --runInBand --coverage=false --silent` failed on the new role query (1 failed, 8 passed): no accessible dialog role was found.
- After implementation, `../../node_modules/.bin/jest components/dialog/Dialog.test.tsx components/modalTwo/ModalTwo.test.tsx --runInBand --coverage=false --silent` passed (2 suites, 11 tests).
- `../../node_modules/.bin/tsc --noEmit --project tsconfig.json` passed.
- `../../node_modules/.bin/eslint components/dialog/Dialog.tsx components/dialog/Dialog.test.tsx components/dialog/index.ts components/modalTwo/Modal.tsx components/modalTwo/ModalTwo.test.tsx components/index.ts --quiet` passed.
- `../../node_modules/.bin/prettier --check components/dialog/Dialog.tsx components/dialog/Dialog.test.tsx components/dialog/index.ts components/modalTwo/Modal.tsx components/modalTwo/ModalTwo.test.tsx components/index.ts` passed after formatting.
- `git diff --check` passed.

Tooling note: `rg` is unavailable (`/bin/bash: rg: command not found`); local `find` and `grep` were used.
