# Checkpoint

Task: Replace inline CSS `height` values containing `vh` with `auto` in the mail HTML preparation pipeline, after `transformStylesheet` and before `transformRemote`.

Initial inspection: transform implementations and existing tests are under `applications/mail/src/app/helpers/transforms/`.

Implementation: Added `transformStyleAttributes`, which checks the root and descendant `[style]` elements, replaces parsed inline heights containing `vh` with `auto`, and preserves other declarations. Wired it after `transformStylesheet` and before `transformRemote`.

Verification: The focused Jest test reported PASS. A broader transform test invocation stalled without producing results and was interrupted.
