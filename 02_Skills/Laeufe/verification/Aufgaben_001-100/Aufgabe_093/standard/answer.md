Popper now reports RTL-adjusted placement: `top` and `bottom` swap `start` and `end` in RTL, while left/right and all LTR placements stay unchanged. The conversion function and middleware are exported for consumers.

Verification passed: 19 Popper tests, TypeScript, ESLint, Prettier, and `git diff --check`.