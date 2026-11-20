Fault localization complete (repository code and existing tests only; no source/test edits).
- scan/base.go:526-581 collects every lockfile into one FileMap, calls analyzer.GetLibraries once, then replaces l.LibraryScanners. This is the per-file analysis boundary; scan/library.go:10 converts analyzer applications into scanners using app.FilePath.
- models/library.go:22 Find filters only by name; lines 83-101 create LibraryFixedIn without path; lines 42-47 use NewDriver and nil check; lines 140-145 define LibraryFixedIn without Path.
- libmanager/libManager.go:41-47 assigns ScannedCves[CveID] for each hit, overwriting earlier same-CVE libraries.
- report/tui.go:747-753 and report/util.go:294-300 call Find(name), so one fixed-in record can render every same-name lockfile and pair wrong versions with fixed versions.
- models/library_test.go:10-99 explicitly expects Find(name) to return both paths for same-name libraries; tests must change for path-aware lookup. No existing scanLibraries tests were found.
- contrib/trivy/parser/parser.go:92-96 also creates LibraryFixedIn without a path; may need coverage if imported Trivy reports share these report views.
Exact fanal AnalyzeFile and Trivy driver error-returning API signatures are not verifiable from in-repo source; local dependency sources are absent. Tests were not run because this review is restricted to diagnosis and cannot fetch dependencies.
