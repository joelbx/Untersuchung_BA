Issue: atomic_move default file permissions and omitted-mode warning.
Status: complete. _DEFAULT_PERM is 0o0600; atomic_move applies DEFAULT_PERM & ~umask, tracks newly created paths when mode is accepted but omitted; set_mode_if_different clears tracked paths; _return_formatted emits the required warning.
Verification: 67 focused unit tests passed; git diff --check passed.
