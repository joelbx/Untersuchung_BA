# Checkpoint

Task: Resolve ModalTwo JSDOM dialog incompatibility.

Status: Investigating root cause before changes.

## Investigation
- Reproduction: `./node_modules/.bin/jest --config packages/components/jest.config.js --runInBand --coverage=false packages/components/components/modalTwo/ModalTwo.test.tsx` failed only new role query: inaccessible button inside closed native dialog.
- Root cause: ModalTwo renders `<dialog>` without `open`; JSDOM's accessibility query treats descendants as hidden. JSDOM also lacks `HTMLDialogElement.prototype.showModal`.
- Local comparison: native dialog with `open` and a `div role="dialog"` both expose the button. Legacy modal uses `<dialog open>`.
- Hypothesis: forwarding active/open to a Dialog abstraction and using a role=dialog fallback when native modal support is missing preserves accessibility and animation lifecycle.

## Resolution
- Added public `Dialog` forwardRef wrapper. It renders native `<dialog>` when `showModal` is available and an accessible `div role="dialog"` fallback otherwise. Attributes, children, and ref reach the selected host.
- ModalTwo now uses Dialog, keeps its host open while active (including exit animation), and sets `aria-modal`.
- Added regression test for role-based child discovery and direct Dialog tests for fallback/native forwarding.
- Final checks: Jest 2 suites/11 tests passed; components TypeScript check passed; targeted ESLint passed; Prettier check passed; `git diff --check` passed.
