# Checkpoint

Task: add -wp-ignore-inactive for WordPress scanning.
Status: implemented and verified.
Tests: go test ./wordpress ./commands ./config; go test ./wordpress -run TestRemoveInactives -count=1.
