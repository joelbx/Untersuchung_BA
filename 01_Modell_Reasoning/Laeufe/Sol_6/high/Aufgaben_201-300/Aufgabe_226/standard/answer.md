MIME mappings and lossless formats now load at startup from [mime_types.yaml](/app/resources/mime_types.yaml). Operators can override it at `<DataFolder>/resources/mime_types.yaml`. The server UI uses the loaded lossless list, and explicit `.js` and `.css` registrations remain in place.

The relevant MIME, model, server, Subsonic, scanner, core, and command package tests passed.