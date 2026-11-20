Implemented punycode conversion for URL hostnames and applied it to external links in `useLinkHandler`. The hook now shows an error notification when it cannot extract a link URL. I also added `getHostnameWithRegex`.

The relevant URL helper tests pass (13 tests), and `git diff --check` passes.