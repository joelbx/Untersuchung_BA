# Checkpoint

Task: Fix uploaded group/user cover and avatar cleanup on explicit removal and account deletion.

Findings: User image URLs are stored as `/assets/uploads/...` and may be exposed with `relative_path` prepended. User cover/avatar filenames include timestamps in current uploads, while account cleanup only checked legacy untimestamped names. Group cover cleanup currently clears fields without deleting files.

Completed: Added safe local path resolution and centralized avatar/cover removal; cleanup removes timestamped and legacy user image variants and matching group cover/thumbnail variants. Account deletion sweeps all supported profile image extensions.

Verification: `node --check` and ESLint pass for the changed files. `mocha test/user.js test/groups.js` passes (334 tests) with a temporary local Redis instance.

Constraints: Preserve the index baseline and git history; do not inspect credentials, private process files, or evaluator artifacts.
