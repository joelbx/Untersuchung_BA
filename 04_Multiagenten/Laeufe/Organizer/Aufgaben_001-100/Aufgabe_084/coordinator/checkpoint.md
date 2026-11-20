Task: Implement removeTechnicalFields in src/api/common/utils/EntityUtils.ts.
Status: Complete. Added recursive in-place removal with cycle protection; EntityUtils tests cover unchanged entities and technical fields at root, nested object, and array levels.
Verification: Prettier check passed; tsc --incremental false --noEmit true passed; npm run fasttest passed (8682 assertions, old style total 9820); git diff --check passed.
Delegation: None.
