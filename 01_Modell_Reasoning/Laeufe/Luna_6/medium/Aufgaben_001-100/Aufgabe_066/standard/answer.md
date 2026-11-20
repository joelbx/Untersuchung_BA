Implemented `transformStyleAttributes` to change inline heights containing `vh` to `auto`, including on the root element, while preserving other style declarations. It runs after `transformStylesheet` and before `transformRemote`.

The focused Jest test passed. The broader transform test run stalled without reporting results, so I interrupted it.