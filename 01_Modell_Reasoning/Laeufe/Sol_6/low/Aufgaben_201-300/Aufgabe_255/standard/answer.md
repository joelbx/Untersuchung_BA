Updated the password lookup plugin to parse key=value term parameters through `LookupModule`, apply term values before plugin defaults, and accept `chars` as either a list or a comma separated string. A fixed `seed` in the term now produces the same password on repeated `/dev/null` lookups.

All 31 password lookup unit tests pass.