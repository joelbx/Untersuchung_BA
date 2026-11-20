Fixed `QtColor` so HSV/HSVA hue percentages scale to 359, while the other channels scale to 255. The parser now validates color function names and component counts before conversion; RGB/RGBA behavior is preserved.

The focused color tests pass (54 tests), and `git diff --check` passes. The full config types test file has 60 unrelated failures, primarily Hypothesis fixture health checks.