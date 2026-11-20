Implemented and exported the `Dialog` abstraction. It forwards refs and attributes, renders a native dialog when supported, and uses an accessible fallback host in limited DOMs. `ModalTwo` now renders through `Dialog` with its host open, and the focus trap accepts the dialog ref.

Verification passed: all 8 existing `ModalTwo` tests, the components type check, and `git diff --check`.