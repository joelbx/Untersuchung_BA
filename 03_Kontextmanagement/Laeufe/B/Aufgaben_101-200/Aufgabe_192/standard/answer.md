Implemented shared calendar event validation for invalid dates, pre-1970 starts, and start times that are not before end times. Manual creation and ICS imports now use the same rules.

`npm run types` and `npm run test:app` passed. The issue is complete.