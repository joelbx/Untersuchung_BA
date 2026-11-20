# Checkpoint

Task: add `isFromProton` for mail elements and provide the specified verified badge component.
Status: complete.
Changes: declared optional `IsProton` on message metadata, conversations, and encrypted search messages; added strict `IsProton === 1` helper; added focused tests; extracted the existing list badge into `VerifiedBadge` with a tooltip.
Verification: 22 element tests passed; mail TypeScript check passed; Prettier check passed; `git diff --check` passed.
