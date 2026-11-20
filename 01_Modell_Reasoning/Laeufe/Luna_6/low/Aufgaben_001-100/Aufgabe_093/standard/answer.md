Implemented RTL placement support in Popper. Top and bottom `start`/`end` placements are mirrored in RTL; left and right placements and all LTR placements stay unchanged. The middleware detects direction from the floating element and supplies the adjusted placement to `usePopper`.

The helper and middleware are exported, and tests cover the placement transformations.

Verification passed: the Popper utils tests and the components TypeScript check.