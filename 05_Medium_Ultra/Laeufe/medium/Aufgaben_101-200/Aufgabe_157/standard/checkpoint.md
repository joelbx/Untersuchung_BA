Task: standardize mail metrics helpers and add @proton/metrics dependency.
Status: complete.
Changes: mail manifest and yarn.lock declare @proton/metrics; new mail metrics helper normalizes label IDs and page sizes; focused tests added.
Verification: Jest helper and label suites passed (30 tests); Prettier check passed; mail TypeScript check passed; git diff --check passed.
