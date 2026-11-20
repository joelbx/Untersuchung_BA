# Checkpoint

Task: add first-class KEV data to vulnerability model, populate from CISA and VulnCheck, sort and summarize.
Status: complete.
Changed: KEV model and nested source details; cached go-kev upgrade; CISA/VulnCheck mapping; due-date normalization; summary and sorting; focused tests.
Validation: GOPROXY=off GOSUMDB=off go test ./models ./detector ./reporter passed; git diff --check passed.
