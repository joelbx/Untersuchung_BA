Task: add isFromProton for mail elements. Checking local types and tests before editing.
Verified: Element is Conversation | Message | ESMessage; none exposes IsProton. The requested VerifiedBadge component is absent. Implementing typed helper and focused tests; leaving UI scope untouched.
Implemented isFromProton with strict IsProton === 1. Added optional IsProton to MessageMetadata, Conversation, and ESBaseMessage. Focused elements tests pass (22/22); mail type check passes. VerifiedBadge.tsx is absent and no UI integration was requested by the behavior requirements.
