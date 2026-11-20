# Checkpoint

Task: Improve message composer room replacement notice semantics and unify cancel controls across related composer, reply, and profile UI.

Implemented: Tombstone status and destination now render in paragraphs; the reply heading names the sender with an inline profile, including emote replies. Added a labeled, configurable cancel button and reused it in reply, search, and link previews. Updated CSS and English string catalog.

Verification: Four focused Jest suites pass (11 tests). Focused ESLint, Stylelint, and `git diff --check` pass. The full TypeScript check reports only five pre-existing errors in SDK HTTP request typings and room alias settings; no changed files appear in the error output.

Status: Repository edits are ready for coordinator export.
