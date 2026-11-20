Updated Meraki requests to retry HTTP 429, 500, and 502 up to three times. The request now raises the new public exception classes when an error persists, warns when rate limiting caused retries, and exposes the final HTTP code through `status`.

The Meraki unit tests pass: **9 passed**.