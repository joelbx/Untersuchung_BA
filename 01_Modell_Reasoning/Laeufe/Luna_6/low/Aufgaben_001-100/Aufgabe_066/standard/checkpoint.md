# Checkpoint

Issue: normalize inline `height` values containing `vh` to `auto` in email HTML, and invoke the transform after stylesheet processing and before remote-resource processing.

Plan:
1. Inspect the existing transform pipeline and test conventions.
2. Implement `transformStyleAttributes` and integrate it in the required order.
3. Add focused tests using existing repository test conventions and run the relevant tests.
