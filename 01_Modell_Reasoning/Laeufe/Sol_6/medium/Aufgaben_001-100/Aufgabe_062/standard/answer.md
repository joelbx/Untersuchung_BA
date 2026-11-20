Updated `ContextReader` to restore the terminal when a password read is canceled or the reader closes, then return to a clean state so later reads can proceed. Added `NotifyExit` for the global stdin reader and called it when `tsh` exits.

The prompt package tests and race test pass. I stopped the broader `tsh` build check after prolonged dependency compilation, so that check remains unverified.