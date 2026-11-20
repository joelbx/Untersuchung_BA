Progress: Fault localization complete from local code and existing tests; no project source or tests changed.

Likely fault locations (lib/ansible/galaxy/collection.py):
- `_build_files_manifest._walk` (~942): `os.path.isdir` follows symlinks, appends linked directory and recurses into it; external directory links use raw `startswith` containment and are skipped. Internal directory links therefore expand in FILES.json.
- `_build_collection_tar` (~1021): `tar_file.add(os.path.realpath(b_src_path), ...)` explicitly dereferences every symlink, making file/directory links regular members. It must retain internal links, with linkname relative to each link, and copy external file targets as regular content.
- `_tarfile_extract` (~773) and `_get_tar_file_member` (~1394) expose only streams, discarding TarInfo. Callers: `from_tar` (~437), `install_artifact` (~258), `_extract_tar_file` (~1363), `_get_json_from_tar_file` (~1406), `_get_tar_file_hash` (~1420).
- `install_artifact` (~253) creates all manifest dirs with `os.makedirs` and sends all files to `_extract_tar_file`; no member-type branch. `_extract_tar_dir` and `_is_child_path` do not exist. `_extract_tar_file` checks only lexical destination parent prefix, then writes bytes and chmods; linked parents can invalidate that containment check. Symlink target validation needs to resolve against the link location and destination root before creating a link.
- `_build_collection_dir` (~1069) also materializes symlinks for SCM install; scope of intended behavior there is uncertain because requirements name tar build and `install_artifact`.

Existing tests: `test_build_copy_symlink_target_inside_collection` (~492) and `test_build_with_symlink_inside_collection` (~520) assert old expansion; `test_build_ignore_symlink_target_outside_collection` (~474) expects skip for an external directory link; `test_get_tar_file_member` (~956) expects stream only; extraction tests (~714-757) cover hash, missing member, missing parent, and lexical `../` but no symlink members. These assertions will conflict with the requested behavior.

No test execution: diagnosis is directly supported by code and tests; no source changes permitted in this specialist role.
