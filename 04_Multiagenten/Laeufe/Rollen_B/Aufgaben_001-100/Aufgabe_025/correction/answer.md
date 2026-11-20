Fixed configuration loading so `${VAR}` references in YAML are resolved before `Load` reads values for defaults and experimental fields. The substitution hook remains first in `DecodeHooks`, and `FLIPT_` environment overrides retain precedence. Added a regression test for `storage.type: ${CONFIG_STORAGE_TYPE}` and its override.

Both reviewer test commands passed.