Task: restore terminal state after canceled/completed tsh password login.
Implemented: cancellation and close restoration, NotifyExit singleton cleanup, tsh exit integration, focused tests.
Verification: prompt package tests and race test pass; tsh package build check stopped after prolonged dependency compilation.
