# Checkpoint

Implemented album image path persistence in the model and scanner refresh flow; directory image names now travel through scan stats, and MediaFiles exposes sorted unique directories. The scan now collects the complete directory map before processing changed folders, so album refresh can see artwork in every associated folder. Added a migration that creates `album.image_files` and forces a full rescan. Focused tests pass.
