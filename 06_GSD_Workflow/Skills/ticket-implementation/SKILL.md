---
name: ticket-implementation
description: >-
  Implementiert genau ein bereits freigegebenes Ticket im
  guided-software-development-Workflow mit kleinen TDD-Schritten oder einer
  begründeten Verifikationsalternative. Verwenden für diesen genehmigten
  Implementierungsschritt; kein Ersatz für vorgelagerte Spec- und Planfreigaben.
metadata:
  version: "1.3.0"
  workflow-bundle: "guided-software-development-1.3.0"
---

# Ticket Implementation

## Vor jeder Änderung, auch bei direktem Aufruf

Lies die [gemeinsamen Regeln](../guided-software-development/references/workflow-rules.md)
und [Persistenz/Gates](../guided-software-development/references/persistence.md).
Fehlt der gemeinsame Kern, stoppen und die vollständige Installation benennen.

Ermittle Projekt, Feature-Artefaktordner und genau eine Ticket-ID. Lies Ticket,
Spec, Plan, Revisionen und die zugehörigen tatsächlichen Freigabebelege. Prüfe,
dass **sowohl Spec als auch Ticketplan gültig menschlich freigegeben sind**, ihre
Hashes passen, Abhängigkeiten erledigt sind und keine fachlichen Blocker bestehen.

Der zentrale [Zustandsprüfer](../guided-software-development/scripts/check_workflow.py)
kann ergänzen, genügt allein aber nicht: Ein `planned`-Zustand ohne Planfreigabe ist
ein legitimer Wartezustand. Ein erfolgreicher Check dieses Zustands erlaubt noch
keine Implementierung. Fehlende Belege vorlegen und warten; niemals selbst erzeugen.

## Durchführung und Rückgabe

Erst nach erfüllten Gates [Implementierungsanweisung](references/06-implementation.md)
laden und auf `implementing` gehen. Arbeite mit den vereinbarten Prüfgrenzen an
einem Verhalten nach dem anderen; halte Red/Green, Regression und begründete
Abweichungen fest. Fachlich Neues zur Klärung zurückgeben, nicht eigenmächtig ergänzen.

Gib Code-Ausgangspunkt/Änderungsstand, betroffene Kriterien, Tests mit tatsächlichen
Ergebnissen, TDD-Nachweise, Abweichungen und Blocker zurück. Erfasse verfügbare Daten
nach der [gemeinsamen Messregel](../guided-software-development/references/09-evaluation.md).
Verlasse dich nicht auf ein altes grünes Ergebnis nach späteren Änderungen.

Du darfst innerhalb des gültigen Plans korrigieren. Review und Abnahme bleiben
gesonderte Schritte; setze kein Ticket auf `done` und starte weder einen Reviewer
noch einen nachfolgenden Skill automatisch. Die zentrale Steuerung übernimmt.
