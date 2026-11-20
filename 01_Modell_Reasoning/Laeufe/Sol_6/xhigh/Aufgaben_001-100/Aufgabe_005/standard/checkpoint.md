Issue: Improve Qt wrapper error handling and early initialization
Status: Implementation complete. Machinery returns SelectionInfo, autoselect records typed import failures, and no-wrapper failures raise NoWrapperAvailableError. Early initialization passes info to the Qt checker and logs selection details.
Verification: 63 targeted tests passed; git diff --check and compileall passed. Broader version test file stops in an existing GUI Chromium test requiring a display.
