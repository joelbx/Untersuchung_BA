Updated `Roles.Check` to reject duplicate roles while preserving rejection of unknown roles. Updated `Roles.Equals` to compare distinct-role sets, regardless of order or duplicates, and to treat nil and empty lists as equal.

The targeted role tests pass. The full `lib/utils` suite has one unrelated failure: a certificate fixture expired in 2021.