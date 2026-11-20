---
name: requirements-clarification
description: >-
  Erfasst Anforderungen, Mockups und Projektkontext und klärt fachliche Entscheidungen
  durch gezielte Rückfragen. Verwenden für die Aufnahme oder Klärung im
  guided-software-development-Workflow oder wenn dieser geführte Klärungsprozess
  ausdrücklich direkt angefordert wird; implementiert keinen Produktivcode.
metadata:
  version: "1.3.0"
  workflow-bundle: "guided-software-development-1.3.0"
---

# Requirements Clarification

## Vertrag und direkte Nutzung

Lies vor Beginn die [gemeinsamen Regeln](../guided-software-development/references/workflow-rules.md)
und [Persistenz/Gates](../guided-software-development/references/persistence.md).
Sie gelten auch ohne vorherigen Aufruf des Oberskills. Fehlt der gemeinsame Kern,
nicht improvisieren; die vollständige Bundle-Installation benennen.

Eingang: Zielprojekt, Anforderungen/Mockups, vorhandene Feature-Artefakte und ggf.
übergebener Modus. Lies zuständige Projektanweisungen. Bei direktem Aufruf den
Projekt- und Feature-Bezug klären und vorhandenen Zustand wiederverwenden.
Der übergebene Kontext ist ein Hinweis, kein Ersatz für tatsächliche Quellen.

## Nur den aktuellen Modus laden

- `intake`: [Aufnahme](references/01-intake.md) lesen. Ergebnis sind Quelleninventar,
  geprüfte Mockup-Bezüge, Projektgrenzen und offene Fragen.
- `clarification`: [Klärung](references/02-clarification.md) lesen. Jeweils die nächste
  tatsächlich offene Entscheidung erfragen, Antworten dauerhaft festhalten.
- `ticket`: [Ticket-Grilling](references/ticket-grilling.md) lesen. Genau ein Ticket
  mit Spec-Freigabe, Mockups und Abhängigkeiten prüfen. Fragen einzeln stellen;
  wenn nichts offen ist, dies dokumentieren und ohne künstliche Rückfragen übergeben.
  Entscheidungen als `clarifications/<ticket>-C<revision>.md` mit Quellen speichern.
  Kein Implementierungsplan: Ein neuer Planungsagent übernimmt diese Ergebnisse.
- Ohne Modus zuerst vorhandene Artefakte prüfen: fehlende Aufnahme nachholen,
  sonst die Klärung fortsetzen. Nicht beide Referenzen routinemäßig vorladen.

Vorlage bei Bedarf: [Fragen/Entscheidungen](assets/decisions.md).
Neue zentrale Statusdatei nur nach dem [Workflow-Muster](../guided-software-development/assets/workflow.json)
anlegen, keine zweite unabhängige Statusführung.

## Rückgabe und Grenzen

Liefere geklärte Punkte, explizite offene Fragen mit betroffenen Tickets, Belege,
aktuellen Zustand und nächsten vorgeschlagenen Schritt. Übernimm Messereignisse
nach den [gemeinsamen Erfassungsregeln](../guided-software-development/references/09-evaluation.md),
soweit Daten vorhanden sind. Keine Messwerte erfinden.

Keine Produktivänderungen, keine Spec-/Planfreigabe oder Abnahme durch den Agenten.
Keine zusätzlichen Unteragenten voraussetzen. Bei abgeschlossenem Klärungsumfang
an die zentrale Steuerung zurückgeben; den nächsten Skill nicht selbst laden.
