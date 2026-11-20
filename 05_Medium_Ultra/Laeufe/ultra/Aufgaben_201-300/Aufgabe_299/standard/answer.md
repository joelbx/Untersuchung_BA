Added filesystem completion to `:open`. The new [FilePathCategory](/app/qutebrowser/completion/models/filepathcategory.py) suggests sorted local paths for absolute paths, `file:///` URLs, and `~` paths. Empty input shows exactly the configured favorites. The [URL model](/app/qutebrowser/completion/models/urlmodel.py) includes Filesystem when enabled and respects the configured category order.

Updated [configuration](/app/qutebrowser/config/configdata.yml) and [help](/app/doc/help/settings.asciidoc) for `completion.favorite_paths` and the new `filesystem` category. Native agents handled the config/help and test changes; I integrated and verified their work.

Verification: the completion and config-data suites passed with **325 passed, 1 skipped, 1 expected failure**.