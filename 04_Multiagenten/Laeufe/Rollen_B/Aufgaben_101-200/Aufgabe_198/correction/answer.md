Fixed the reviewer’s finding: Red Hat, CentOS, Alma, and Rocky package scans now use OVAL without opening the Gost database.

The reviewer’s exact test commands passed (`./oval ./gost` and `./detector`), and `git diff --check` passed. No remaining failures or test environment problems.