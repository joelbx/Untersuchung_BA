Updated the promise-item import flow to augment incomplete JSON records before validation. It uses ISBN-10 first, then a B* ASIN, and fills only empty fields from staged metadata. I also added strong-identifier validation, limited batch staging to incomplete records, added gauges, and removed placeholder publisher values.

The relevant import API, batch, and `add_book` suites passed: **98 tests**.