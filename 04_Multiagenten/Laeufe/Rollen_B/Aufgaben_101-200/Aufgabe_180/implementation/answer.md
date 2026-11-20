Updated the EOL data in [config/os.go](/app/config/os.go): corrected Fedora 37 and 38, added Fedora 40 and macOS 15, marked macOS 11 ended, and added the requested SUSE Enterprise 13/14 dates. The cited old 13/14 dates were in the FreeBSD map, so I corrected those too.

Extended the Windows 10 19045, Windows 11 22621/22631, and Server 2022 20348 KB lists in [scanner/windows.go](/app/scanner/windows.go). Existing entries remain in place, and the additions use named literals in ascending revision order. Updated tests cover the EOL boundaries and whether recent KBs are applied or unapplied.

The focused lifecycle and scanner tests passed; `git diff --check` passed.