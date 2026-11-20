I located the change points, but did not edit project source or tests: my assigned fault localization role permits inspection and diagnosis only.

- Add `getLabelID` and `getPageSizeString` in [mailMetricsHelper.ts](/app/applications/mail/src/app/metrics/mailMetricsHelper.ts). The file does not exist yet. [labels.ts](/app/applications/mail/src/app/helpers/labels.ts:57) already identifies custom IDs; built-in IDs are defined in [constants.ts](/app/packages/shared/lib/constants.ts:859).
- Map the page size enum’s 50, 100, and 200 values to strings, and return `"50"` for missing or invalid settings. The enum is in [mailSettings.ts](/app/packages/shared/lib/mail/mailSettings.ts:155).
- Add `@proton/metrics` to [mail’s package manifest](/app/applications/mail/package.json) and its `proton-mail` entry in [yarn.lock](/app/yarn.lock:35924). The metrics workspace package already has a lockfile entry.

The remaining uncertainty is how the new helpers will be called; no mail metrics module or tests for these interfaces exist in the inspected tree. I recorded the diagnosis in `.codex-role-output/checkpoint.md`.