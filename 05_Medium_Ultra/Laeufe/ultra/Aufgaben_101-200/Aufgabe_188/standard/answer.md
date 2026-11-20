Centralized storage units in [size.ts](/app/packages/shared/lib/helpers/size.ts) and migrated member allocation, CSV import, organization setup, bonuses, plan defaults, offers, and file size limits. Removed the old `GIGA` and `BASE_SIZE` definitions from `constants.ts`.

The CSV suite passed (64 tests), Offers passed (4 tests; 1 skipped), and dashboard upsells passed (14 tests). Prettier, ESLint, and `git diff --check` passed. Both type checks stopped at an unrelated OpenPGP type mismatch in [api.ts](/app/packages/crypto/lib/worker/api.ts:579); shared browser tests could not launch because the configured Chromium binary is missing.

Three subagents handled the shared helper, provisioning flows, and selector/setup components. I integrated and verified their edits.