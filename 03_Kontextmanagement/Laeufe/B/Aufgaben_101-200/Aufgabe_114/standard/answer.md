Implemented the artist image lookup in `/app`. Albums now retain their unique media directories, and artist artwork checks the inferred artist folder for `artist.*` before using the existing fallbacks. Each source attempt logs its duration.

Relevant tests passed for the model, artwork, scanner, migration, database, and persistence packages. The repository work item is complete.