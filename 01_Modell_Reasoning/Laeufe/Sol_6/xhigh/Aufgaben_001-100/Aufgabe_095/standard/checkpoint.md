Task: Add a module-level date formatter and validate patron check-in update requests.
Initial findings: checkins.py has a method-based formatter and create-request validator; no patron_check_ins class is present there. Existing tests cover check_ins only.
Completed: added module-level make_date_string, kept check_ins method compatibility, and added patron_check_ins.is_valid for id plus year/data presence. No patron update handler or route exists in this checkout, so no request path could be wired to the validator without defining a new API.
Verification: existing check-in tests passed (5/5); direct checks of the new imports, date cases, and validation cases passed; git diff --check passed.
