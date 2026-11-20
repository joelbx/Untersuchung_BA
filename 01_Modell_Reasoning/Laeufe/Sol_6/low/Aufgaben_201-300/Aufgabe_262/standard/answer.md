Updated book import to check cover URL hosts against `ALLOWED_COVER_HOSTS` before uploading. The new `process_cover_url` function accepts HTTP and HTTPS URLs, compares hostnames without regard to case, and removes the `cover` key whether the URL is allowed or rejected. Both import cover paths use it.

The existing add-book test file passes: **85 tests passed**.