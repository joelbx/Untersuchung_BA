Added a ref-forwarding [Dialog component](/app/packages/components/components/dialog/Dialog.tsx) that uses a compatible host when native dialog methods are unavailable. [ModalTwo](/app/packages/components/components/modalTwo/Modal.tsx) now uses it and marks the host open. A regression test confirms its child button is discoverable by role in JSDOM.

The ModalTwo test suite passed: 9 tests.