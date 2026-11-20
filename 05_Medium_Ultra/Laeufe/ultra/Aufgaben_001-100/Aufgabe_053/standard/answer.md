Fixed `oval.major("")` to return `""` without changing parsing for non-empty input. Added a regression case and the three requested report interfaces as wrappers around existing detectors.

Two read-only subagents reviewed the oval behavior and report interfaces; I integrated and verified the changes. The focused regression test and the full `oval` and `report` package tests passed offline.