Task: implement local lookup of staged or pending import items by source-prefixed identifiers in openlibrary/core/imports.py.
Status: implemented ImportItem.find_staged_or_pending with default amazon/idb sources and empty-input handling. Added database coverage for matching statuses, custom sources, and empty identifiers. Relevant test file passes (6 tests).
