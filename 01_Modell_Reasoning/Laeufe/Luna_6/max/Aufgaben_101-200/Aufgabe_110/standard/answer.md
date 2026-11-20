Implemented mechanism-segmented download outcome metrics. The selector in [fileSaver.ts](/app/applications/drive/src/app/store/_downloads/fileSaver/fileSaver.ts:21) now drives both saver selection and metric labels. Terminal reports include status, retry, and mechanism; stateful downloads use `meta.size`, and previews pass `link.size` through [useDownload.ts](/app/applications/drive/src/app/store/_downloads/useDownload.ts:190).

Added the v1 label schema and registered the counter in [Metrics.ts](/app/packages/metrics/Metrics.ts:950).

**Verification passed:** Drive metrics hook tests (17), metrics package tests (107), Drive and metrics type checks, and `git diff --check`.