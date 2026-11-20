The checked-out invitation patch satisfies the requested token-based registration flow. I found no code defect to change in this correction round.

I reran the reviewer’s exact checks: invitation tests (31 passing), authentication tests (30 passing), and ESLint (passed). Redis was initially stopped; I started the installed server for the tests and stopped it afterward. No failures remain.