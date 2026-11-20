Implemented `guessDateFromText` and used it for CSV date imports and vCard text conversion. Added coverage for ISO timestamps, month-name dates, and both slash-separated formats.

The existing property test bundle compiled successfully, but Karma could not run because the configured ChromeHeadless binary is missing. `yarn workspace @proton/shared check-types` completed without errors.