# Multiagenten: Rollen B und Organizer

Drei frische Varianten mit Sol 6/medium: Standard, Rollen B und Organizer. Rollen B: Diagnose → Implementierung → Review → optional einmal Korrektur. Organizer: frei formulierte Rollen, maximal drei Delegationen, maximal ein Kind gleichzeitig. Die tatsächlichen Rollenprompts, Requests, Antworten und Übernahmeentscheidungen liegen beim jeweiligen Endversuch.

## Wo steht was?

- **Start-/Ausführungsrunner:** [Runner/run_mas.py](Runner/run_mas.py)
- **Gesamtauswertung:** [Auswertung/compare_mas_300.py](Auswertung/compare_mas_300.py)
- **Finaler Bericht:** [Ergebnisse/summary.md](Ergebnisse/summary.md)
- **Konkrete Endversuche:** [Laeufe](Laeufe/)
- **Parameter und historische Quellen:** [Konfiguration](Konfiguration/)

## Varianten

- [Organizer](Laeufe/Organizer/)
- [Rollen_B](Laeufe/Rollen_B/)
- [Standard](Laeufe/Standard/)

Jeder Aufgabenordner enthält das unveränderte result.json, die vorhandene offizielle Evaluation, den Patch und die zugehörigen Modellstufen. Bei ausgewiesenen Ausschlüssen gibt es nur die tatsächlich vorhandenen Statusartefakte. Ein im Original fehlendes Ergebnis wird nicht erfunden.

Die Quelldateien unter Runner und Auswertung sind unverändert; Hilfsmodule sind ausdrücklich keine zusätzlichen Versuchsreihen. Für historische Änderungen sind die eingefrorenen Quellen unter Konfiguration/Batchnachweise maßgeblich. Die neue Gliederung dient dem Nachlesen, nicht dem direkten Start mit alten Pfadannahmen.
