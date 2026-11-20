Task: implement well-known force_disable E2EE policy for room creation.
Implemented: well-known type, strict policy helper, private default precedence, shared async server/well-known decision, dialog enforced state and submission, focused dialog tests.
Validation: targeted CreateRoomDialog Jest suite passed (12 tests); git diff --check passed. Full lint:types failed on pre-existing src/Unread.ts:167 missing getLastUnthreadedReceiptFor on Thread | Room.
