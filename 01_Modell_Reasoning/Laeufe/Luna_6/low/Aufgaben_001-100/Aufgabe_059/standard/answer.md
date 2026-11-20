Added the exported `Dialog` abstraction and updated ModalTwo to use it. It forwards props and refs, renders a `<dialog>` when available, and falls back to a `<div>` when `HTMLDialogElement` is unavailable.

`git diff --check` passed. The ModalTwo test and package type check both stalled without producing output, so I couldn’t confirm their results.