Updated lockfile scanning and vulnerability reports so each library finding retains its source path. Reports now look up versions by path and name, duplicate CVEs keep findings from each lockfile, and unknown lockfile types return an error.

The affected package tests passed, including a new two-lockfile regression test.