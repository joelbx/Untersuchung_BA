Fixed the YAML filters so an undefined value reports the missing variable instead of a PyYAML `RepresenterError`. Both filters now name the failing filter and preserve the underlying cause.

Verification: 16 focused tests passed, and a template using an undefined variable reported `MYSVC_ENV` by name.