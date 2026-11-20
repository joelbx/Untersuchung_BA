Implemented alternate-script author names from linked MARC 880 fields for 100, 700, and 720 person entries. Added `name_from_list`, normalized names and dates, and deduplicated linked names in `alternate_names`. Updated the affected test expectations; the 110 and 111 parsing paths remain unchanged.

Verification: **124 MARC tests passed**.