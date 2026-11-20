Added a public `Dialog` component that forwards attributes, children, and its ref to a native dialog when supported, or to an accessible fallback host in JSDOM. `ModalTwo` now uses it and keeps the host open through its exit animation, so interactive children are discoverable by role.

Verification passed: 11 relevant Jest tests, TypeScript, ESLint, Prettier, and `git diff --check`.