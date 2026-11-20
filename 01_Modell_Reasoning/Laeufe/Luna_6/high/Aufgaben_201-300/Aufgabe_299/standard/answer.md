Implemented filesystem completion for `:open` with configurable favorites, matching for absolute paths, `file:///` URLs, and `~` paths, and Filesystem category ordering through `completion.open_categories`. Updated the setting definitions and help docs.

**Verification:** `py_compile` and `git diff --check` passed. The focused completion suite had 65 passing tests when excluding two tests that expect the old default category list. Those two fail because the required new default includes Filesystem.

Key files: [filepathcategory.py](/app/qutebrowser/completion/models/filepathcategory.py), [urlmodel.py](/app/qutebrowser/completion/models/urlmodel.py), [configdata.yml](/app/qutebrowser/config/configdata.yml), [settings.asciidoc](/app/doc/help/settings.asciidoc).