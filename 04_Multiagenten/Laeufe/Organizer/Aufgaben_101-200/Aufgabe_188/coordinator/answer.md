Centralized storage multipliers in [helpers/size.ts](/app/packages/shared/lib/helpers/size.ts). Member allocation, organization setup, CSV import, bonus storage, and other production storage calculations now use `sizeUnits` or `BASE_SIZE` from that module. Drive Pro and Drive Business initial allocations now use `sizeUnits.TB`.

The CSV suite passed (64 tests, 5 snapshots), focused lint passed, and `git diff --check` passed. The components type check remains blocked by an unrelated OpenPGP type conflict in `packages/crypto/lib/worker/api.ts`.

No delegation was used.