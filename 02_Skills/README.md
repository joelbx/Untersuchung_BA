# Skills

Vier frische Varianten mit Sol 6/medium: Standard, TDD, Debugging und Verification. Die tatsächlich injizierten Skillfassungen samt Herkunft und Anpassungen liegen unter Konfiguration/Skills. Protokoll.md dokumentiert das Untersuchungsprotokoll.

## Wo steht was?

- **Start-/Ausführungsrunner:** [Runner/run_skills.py](Runner/run_skills.py)
- **Gesamtauswertung:** [Auswertung/compare_skills.py](Auswertung/compare_skills.py)
- **Finaler Bericht:** [Ergebnisse/summary.md](Ergebnisse/summary.md)
- **Konkrete Endversuche:** [Laeufe](Laeufe/)
- **Parameter und historische Quellen:** [Konfiguration](Konfiguration/)

## Varianten

- [Standard](Laeufe/Standard/)
- [debugging](Laeufe/debugging/)
- [tdd](Laeufe/tdd/)
- [verification](Laeufe/verification/)

Jeder Aufgabenordner enthält das unveränderte result.json, die vorhandene offizielle Evaluation, den Patch und die zugehörigen Modellstufen. Bei ausgewiesenen Ausschlüssen gibt es nur die tatsächlich vorhandenen Statusartefakte. Ein im Original fehlendes Ergebnis wird nicht erfunden.

Die Quelldateien unter Runner und Auswertung sind unverändert; Hilfsmodule sind ausdrücklich keine zusätzlichen Versuchsreihen. Für historische Änderungen sind die eingefrorenen Quellen unter Konfiguration/Batchnachweise maßgeblich. Die neue Gliederung dient dem Nachlesen, nicht dem direkten Start mit alten Pfadannahmen.
