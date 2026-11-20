Implemented filesystem completion for `:open`, including favorites, absolute path matching, `file:///` handling, and `~` expansion with contracted suggestions. Added the setting and updated the generated help. Updated existing expectations for the new default category.

Verification: **96 passed, 2 benchmark tests deselected**. Compilation and `git diff --check` passed.

Key files: [filepathcategory.py](/app/qutebrowser/completion/models/filepathcategory.py), [urlmodel.py](/app/qutebrowser/completion/models/urlmodel.py), [configdata.yml](/app/qutebrowser/config/configdata.yml), [settings.asciidoc](/app/doc/help/settings.asciidoc).