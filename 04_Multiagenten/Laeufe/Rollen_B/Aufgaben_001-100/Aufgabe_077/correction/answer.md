The deprecation-by-date patch now treats `removed_at_date` arguments as deprecated during validate-modules documentation checks. I also added coverage for date display, C# date output, and the requested alias validation errors.

The reviewed Python module suite passed (**98 tests**), the display suite passed (**4 tests**), and `git diff --check` passed.

**TEST_ENVIRONMENT_PROBLEM:** The validate-modules test could not collect because `voluptuous` is missing. The C# integration test could not run because `pwsh` is unavailable.