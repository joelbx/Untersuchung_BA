# Modell und Reasoning

Luna 6 und Sol 6; low, medium, high, xhigh und max; Standardarchitektur. Die Ordner unter Laeufe sind nach Modell und Reasoning gegliedert. Die drei Aufgabenblöcke umfassen zusammen Aufgaben 1–300. Die 281er-Hauptauswertung ist die gemeinsame vollständig bewertete Schnittmenge, keine separate Aufgabenreihe.

## Wo steht was?

- **Start-/Ausführungsrunner:** [Runner/run_reasoning.py](Runner/run_reasoning.py)
- **Gesamtauswertung:** [Auswertung/compare_reasoning.py](Auswertung/compare_reasoning.py)
- **Finaler Bericht:** [Ergebnisse/reasoning-comparison.md](Ergebnisse/reasoning-comparison.md)
- **Konkrete Endversuche:** [Laeufe](Laeufe/)
- **Parameter und historische Quellen:** [Konfiguration](Konfiguration/)

## Varianten

- [Luna_6](Laeufe/Luna_6/)
- [Sol_6](Laeufe/Sol_6/)

Die historischen Luna-Medium-Dateien sind vollständig in diese Struktur einsortiert. Die alten Verzeichnisnamen stehen nur noch in Herkunftsangaben innerhalb der Originaldateien und der Pfadzuordnung.

Jeder Aufgabenordner enthält das unveränderte result.json, die vorhandene offizielle Evaluation, den Patch und die zugehörigen Modellstufen. Bei ausgewiesenen Ausschlüssen gibt es nur die tatsächlich vorhandenen Statusartefakte. Ein im Original fehlendes Ergebnis wird nicht erfunden.

Die Quelldateien unter Runner und Auswertung sind unverändert; Hilfsmodule sind ausdrücklich keine zusätzlichen Versuchsreihen. Für historische Änderungen sind die eingefrorenen Quellen unter Konfiguration/Batchnachweise maßgeblich. Die neue Gliederung dient dem Nachlesen, nicht dem direkten Start mit alten Pfadannahmen.
