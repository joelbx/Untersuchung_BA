Task: clean up locally uploaded group covers and user cover/avatar files on explicit removal and account deletion.
Status: implementation complete. Centralized user image deletion validates local URLs and removes legacy/timestamped cover and avatar variants; account deletion uses it. Group cover removal unlinks local cover/thumbnail variants. Socket handlers delegate and await action hooks.
Verification: eslint and git diff --check passed; 334 existing user/group tests passed; 5 image-cleanup regression tests passed.
