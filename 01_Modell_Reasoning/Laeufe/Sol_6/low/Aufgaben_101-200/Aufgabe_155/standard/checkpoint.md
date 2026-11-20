Task: support image digest references across config, scan, and reporting.
Status: implemented and verified with targeted tests; working tree ready for export.
Changes: digest fields, exclusive tag/digest validation, full image references for scan/log/report, and index@server naming during image OS detection.
Tests: go test -vet=off ./config ./models ./scan ./report -run '^(TestImageReference|TestImageReportNames)$' passed. Broad run hit existing models TestScan failure; standard go test also hit existing models/library.go vet errors.
