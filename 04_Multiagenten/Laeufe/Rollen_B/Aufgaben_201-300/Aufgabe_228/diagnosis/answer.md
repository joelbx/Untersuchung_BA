I located the changes needed, but did not edit project source or tests: the task constraints for this run limit me to fault localization.

`utils.parse_version` is absent. In PyQt5, `QVersionNumber.fromString` returns a tuple; its version value needs `.normalized()` so `5.4` and `5.4.0` compare equal.

The affected paths are [qtutils.py](/app/qutebrowser/utils/qtutils.py:90), [earlyinit.py](/app/qutebrowser/misc/earlyinit.py:171), [version.py](/app/qutebrowser/utils/version.py:114), and [crashdialog.py](/app/qutebrowser/misc/crashdialog.py:358). They currently use `pkg_resources` parsing or older Qt version checks. The fix should use the shared helper for string versions, `QLibraryInfo.version()` for runtime Qt, preserve exact versus greater-or-equal behavior and the incompatible-flags error, and show the crash dialog note only for a strictly newer parsed version.

Existing distribution tests expect `pkg_resources` values, so they will need updating. One behavior needs care: Qt parsing drops prerelease suffixes such as `rc1`, which may affect the crash dialog comparison. I recorded the findings in [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md).