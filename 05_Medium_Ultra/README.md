# Medium und natives Ultra

Frisch ausgeführtes Sol 6/medium versus Sol 6/ultra mit nativen Unteragenten und Delegationsprompt. Ultra verändert mehrere Faktoren gemeinsam. Seine Token-/Delegationszahlen sind wegen 15 unvollständiger Rollout-Exporte Mindestwerte; die offiziellen Bewertungen bleiben vorhanden.

## Wo steht was?

- **Start-/Ausführungsrunner:** [Runner/run_sol_ultra.py](Runner/run_sol_ultra.py)
- **Gesamtauswertung:** [Auswertung/compare_sol_ultra_all.py](Auswertung/compare_sol_ultra_all.py)
- **Finaler Bericht:** [Ergebnisse/summary.md](Ergebnisse/summary.md)
- **Konkrete Endversuche:** [Laeufe](Laeufe/)
- **Parameter und historische Quellen:** [Konfiguration](Konfiguration/)

## Varianten

- [medium](Laeufe/medium/)
- [ultra](Laeufe/ultra/)

Jeder Aufgabenordner enthält das unveränderte result.json, die vorhandene offizielle Evaluation, den Patch und die zugehörigen Modellstufen. Bei ausgewiesenen Ausschlüssen gibt es nur die tatsächlich vorhandenen Statusartefakte. Ein im Original fehlendes Ergebnis wird nicht erfunden.

Die Quelldateien unter Runner und Auswertung sind unverändert; Hilfsmodule sind ausdrücklich keine zusätzlichen Versuchsreihen. Für historische Änderungen sind die eingefrorenen Quellen unter Konfiguration/Batchnachweise maßgeblich. Die neue Gliederung dient dem Nachlesen, nicht dem direkten Start mit alten Pfadannahmen.
