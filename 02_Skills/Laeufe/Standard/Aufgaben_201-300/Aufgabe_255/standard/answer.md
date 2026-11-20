Fixed the password lookup plugin so inline key=value options, including `seed`, are applied. `chars` now accepts either a comma-separated string or a list, and repeated lookups with the same seed produce the same password.

The password lookup tests pass: **33 passed**.