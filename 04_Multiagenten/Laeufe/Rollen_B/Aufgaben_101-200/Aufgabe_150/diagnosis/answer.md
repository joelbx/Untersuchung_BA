I traced the issue to two places:

- [concrete_artifact_manager.py](/app/lib/ansible/galaxy/collection/concrete_artifact_manager.py:570) defaults an absent `manifest` to `{}`, losing the distinction between absent and explicitly empty configuration.
- [collection/__init__.py](/app/lib/ansible/galaxy/collection/__init__.py:1061) selects the file-walking path by truthiness. It needs an explicit `Sentinel` check so an absent manifest still produces a format-1 file list with `build_ignore` applied, while `{}` and `null` can be handled as explicit manifest settings.

The walking path already excludes external **directory** symlinks and lists internal directory symlinks once. External **file** symlinks can still enter its file branch, so the symlink requirement needs coverage for both types. Existing [unit tests](/app/test/units/galaxy/test_collection.py:590) exercise these walking behaviors with `{}`, but none pass `Sentinel`.

I updated [checkpoint.md](/app/.codex-role-output/checkpoint.md). I did not edit source or tests: the assigned fault-localization role explicitly limits this pass to diagnosis.