VERDICT: FIX

**Code defects**

- [fileSaver.ts](/app/applications/drive/src/app/store/_downloads/fileSaver/fileSaver.ts:18) selects `sw` from file size and browser capability, but the saver can fall back to memory after service worker registration fails. The new counter then records an actual fallback download as `sw`. Pass the mechanism actually used by the saver to the metrics hook.
- [useDownloadProvider.tsx](/app/applications/drive/src/app/store/_downloads/DownloadProvider/useDownloadProvider.tsx:94) marks prebuffered downloads Done before `saveAsFile` settles. A failed save can therefore increment the new success counter. Set Done or Error after the save resolves or rejects.

**Tests:** `yarn workspace proton-drive test:ci src/app/store/_downloads/DownloadProvider/useDownloadMetrics.test.ts src/app/store/_downloads/fileSaver/fileSaver.test.ts` — passed, 2 suites and 21 tests. These tests do not cover the two cases above.

**TEST_ENVIRONMENT_PROBLEM:** None. Review notes are in [checkpoint.md](/app/.codex-role-output/checkpoint.md).