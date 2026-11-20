# Email validation issue checkpoint

Implemented UID-to-code confirmation mapping, explicit millisecond expiry, pending and expiry helpers, ACP email status labels and fallback, and deletion cleanup. Fixed confirmation by code for actual email changes. Focused email, socket, and ACP status tests pass; lint and diff checks pass. Broader user suite stopped at an invitation group membership assertion after 173 passing tests, and full admin controller suite stopped at an unrelated edit/email 404 assertion after 11 passing tests.
