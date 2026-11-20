Added the module-level [make_date_string](/app/openlibrary/plugins/upstream/checkins.py:17) function and a patron check-ins update handler that rejects requests without an event ID or updatable content and checks event ownership. I also fixed the event data update method so the handler can call it.

Verification: 20 relevant tests passed; `git diff --check` passed.