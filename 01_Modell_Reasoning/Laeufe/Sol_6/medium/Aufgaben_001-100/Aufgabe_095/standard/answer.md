Added the importable `make_date_string` function with zero-padded partial dates, and added `patron_check_ins` validation so updates require an event ID and either a year or data. The update handler also checks that the event belongs to the requesting user.

All 19 relevant tests pass when run together.