Fixed the RPM parsing issue. Nonstandard source filenames now produce a warning while the scan retains the binary package. Source filenames with an epoch now preserve that epoch in the source version, even when the binary epoch differs.

The targeted tests and full `./scanner` test suite passed. `TEST_ENVIRONMENT_PROBLEM: none.`