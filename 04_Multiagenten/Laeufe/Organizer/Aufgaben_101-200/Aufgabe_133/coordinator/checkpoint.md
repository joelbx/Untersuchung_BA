# Checkpoint

Issue: Teleport 6 OSS migration removes admin role and breaks trusted cluster mapping.
Status: implementation complete.
Changes: migration gets and downgrades existing admin role, uses its OSSMigratedV6 label as completion marker, assigns users and trusted-cluster mappings to admin; legacy tctl user creation and OSS role deletion guard use admin. Added NewDowngradedOSSAdminRole with limited permissions and updated migration tests.
Verification: TestMigrateOSS passes; lib/services and tool/tctl/common packages pass; isolated lib/auth TestAPI passes. Full lib/auth run fails only PasswordSuite.TestTiming's 10% timing threshold (11.87% and 23.15% on two runs). git diff --check passes.
Delegation: none.
