Added an early return so `oval.major("")` returns `""` without panicking. Non-empty parsing remains unchanged, and the existing test now covers empty input.

The focused test and the full `oval` package test suite passed.