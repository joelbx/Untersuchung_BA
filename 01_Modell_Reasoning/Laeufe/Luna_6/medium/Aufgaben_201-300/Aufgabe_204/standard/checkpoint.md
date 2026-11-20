Issue: contact import does not consistently parse text dates.

Plan: inspect the shared contact property and CSV date helpers plus existing tests; implement a reusable text parser, preserve valid Date instances and calendar values through vCard serialization; run existing relevant tests.
