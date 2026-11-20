Added `ImportItem.find_staged_or_pending` with fixed `amazon` and `idb` source prefixes. It returns matching `import_item` rows with `staged` or `pending` status. ISBN resolution now uses that local lookup for both ISBN-10 and ISBN-13 and checks both forms after import.

Verification: 17 relevant tests passed; Ruff and `git diff --check` passed. No delegation was used.