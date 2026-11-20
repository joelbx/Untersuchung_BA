Added `parse_duration` and updated `:later` to accept hours, minutes, and seconds, including decimal values and combined expressions such as `2m30s`. Bare integers still mean milliseconds; invalid durations raise `ValueError`.

The 16 focused tests passed. The broader run reported 180 passed, then exited with an X11 shutdown error.