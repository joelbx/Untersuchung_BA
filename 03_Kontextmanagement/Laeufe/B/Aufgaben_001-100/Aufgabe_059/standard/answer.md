Resolved the `ModalTwo` JSDOM issue. `ModalTwo` now uses a public, ref-forwarding [Dialog](/app/packages/components/components/dialog/Dialog.tsx) abstraction that uses an accessible fallback host when native dialog support is limited. Open modal children are discoverable by role.

Validation passed: 11 focused tests, the TypeScript check, and formatting checks.