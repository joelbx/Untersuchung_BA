# Kontextmanagement

Sol 6/medium; Standard versus aufgabenfremder Sachtext A und aufgabenfremde Sitzungshistorie B. Die verwendeten Materialien liegen unter Konfiguration/Kontextmaterialien. context_pilot.py ist, soweit unter Hilfsmodule enthalten, eine von den finalen Skripten importierte Codeabhängigkeit; es enthält keine Pilot-Ergebnisse.

## Wo steht was?

- **Start-/Ausführungsrunner:** [Runner/run_context_main.py](Runner/run_context_main.py)
- **Gesamtauswertung:** [Auswertung/report_context_all.py](Auswertung/report_context_all.py)
- **Finaler Bericht:** [Ergebnisse/report.md](Ergebnisse/report.md)
- **Konkrete Endversuche:** [Laeufe](Laeufe/)
- **Parameter und historische Quellen:** [Konfiguration](Konfiguration/)

## Varianten

- [A](Laeufe/A/)
- [B](Laeufe/B/)
- [Standard](Laeufe/Standard/)

Jeder Aufgabenordner enthält das unveränderte result.json, die vorhandene offizielle Evaluation, den Patch und die zugehörigen Modellstufen. Bei ausgewiesenen Ausschlüssen gibt es nur die tatsächlich vorhandenen Statusartefakte. Ein im Original fehlendes Ergebnis wird nicht erfunden.

Die Quelldateien unter Runner und Auswertung sind unverändert; Hilfsmodule sind ausdrücklich keine zusätzlichen Versuchsreihen. Für historische Änderungen sind die eingefrorenen Quellen unter Konfiguration/Batchnachweise maßgeblich. Die neue Gliederung dient dem Nachlesen, nicht dem direkten Start mit alten Pfadannahmen.
