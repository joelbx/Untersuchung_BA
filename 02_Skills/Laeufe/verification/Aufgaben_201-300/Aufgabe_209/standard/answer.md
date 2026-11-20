Updated the Subscribe to Calendar modal to use `MAX_LENGTHS_API.CALENDAR_URL` (10,000 characters). Overlong URLs now show the length warning and cannot be submitted; warnings follow the requested priority. The character counter and input `maxLength` were removed.

Moved ResizeObserver mocks into the calendar, components, and mail Jest setup files and removed the inline assignments. The new modal test uses a default-export mock for `useGetCalendarSetup`.

Verification: 23 relevant tests passed, the components type check passed, and formatting and lint checks passed. The initial lint run hit Node’s heap limit; targeted reruns with a larger heap passed. Details are in [checkpoint.md](/app/.codex-role-output/checkpoint.md).