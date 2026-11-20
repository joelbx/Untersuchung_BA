# Fault localization checkpoint

Inspected MessageComposer, ReplyPreview, DisambiguatedProfile, AccessibleButton, their styles, and the existing MessageComposer test. No project source or tests changed.

- `MessageComposer.render` tombstone branch (`src/components/views/rooms/MessageComposer.tsx`, around 385-410) places the replacement message in a styled `span`, then a `br`, then an optional continuation link. The text already says the room is replaced and inactive; the structural problem is the missing paragraph markup. Its icon also has no `alt`.
- `test/components/views/rooms/MessageComposer-test.tsx` (around 50-65) only checks the old `.mx_MessageComposer_roomReplaced_header` selector and lack of composer/buttons. It neither checks paragraph semantics nor the displayed message/link cases.
- `ReplyPreview.render` (`src/components/views/rooms/ReplyPreview.tsx`, around 45-57) labels the section only “Replying” and renders an unlabeled icon-only `AccessibleButton`; `res/css/views/rooms/_ReplyPreview.scss` gives that control bespoke styling. `SearchBar` has a similar unlabeled cancel control. `LinkPreviewGroup` shows the repo pattern for `aria-label` on an icon-only close control.
- `DisambiguatedProfile` (`src/components/views/messages/DisambiguatedProfile.tsx`, around 30-70) hardcodes a `div` root. It is used by `SenderProfile` in reply tiles and `MemberTile`, so an optional root element prop would allow inline use in reply context while retaining current block usage. Confirm desired inline wording and sender fallback when implementing.
- `src/components/views/buttons/Cancel.tsx` does not exist. `AccessibleButton` lives under `views/elements` and supplies keyboard activation and role/tabIndex, but icon-only callers need an accessible name. A shared cancel control would consolidate size, icon mask, color, and label across reply/search and other relevant call sites.

Uncertainty: broad “all interface components” requirement does not enumerate which cancel controls should migrate; search, reply, and link preview are confirmed examples. No tests run; diagnosis is based on source and existing test review only.
