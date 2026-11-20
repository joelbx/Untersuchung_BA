---
name: ticket-planning
description: >-
  Erstellt einen konkreten Implementierungsplan für ein Ticket aus einer
  freigegebenen Spezifikation im guided-software-development-Workflow und legt
  Prüfstrategie und Änderungen zur menschlichen Freigabe vor. Verwenden für diesen
  geführten Planungs- und Freigabeschritt, nicht zur sofortigen Implementierung.
metadata:
  version: "1.3.0"
  workflow-bundle: "guided-software-development-1.3.0"
---

# Ticket Planning

Lies die [gemeinsamen Regeln](../guided-software-development/references/workflow-rules.md)
und [Persistenz/Gates](../guided-software-development/references/persistence.md).
Diese Voraussetzungen gelten auch beim direkten Aufruf; fehlt der gemeinsame Kern,
vollständige Installation benennen statt eigene Gates zu definieren.

Eingang: Projekt, Feature-Artefaktordner, Ticket-ID, freigegebene Spec und relevante
Entscheidungen. Lies den Zustand und tatsächliche Belege. Fehlende Spec-Freigabe,
offene fachliche Blocker oder unerledigte Abhängigkeiten benennen, nicht umgehen.

Beginne im frischen Planungskontext. Lies die gespeicherten Ergebnisse der
separaten Ticketklärung. Sind dort wesentliche Punkte offen oder entdeckst du
neue fachliche Fragen, gib diese an den Koordinator zur erneuten Klärungsphase
zurück; erfinde keine Antwort und starte kein zweites vollständiges Interview.

Lade [Planung](references/05-planning.md), bei Bedarf die
[Planvorlage](assets/implementation-plan.md). Analysiere betroffene Komponenten
lesend, sichere Code-Ausgangspunkt und fremde Vorarbeiten. Definiere konkrete
Änderungen, Schnittstellen, Prüfgrenzen, Teststrategie, Alternativen zu TDD und Risiken.
Keine neuen Fachanforderungen aus technischen Vorlieben ableiten. Fehlt eine
geeignete menschliche Prüfmöglichkeit, plane eine
[temporäre Prüfhilfe samt Rückbau](../guided-software-development/references/temporary-test-aids.md)
und lege sie zusammen mit dem Plan zur Freigabe vor.

Speichere Ticket und Plan in ihrer vorgelegten Revision, Status `planned`.
Fordere die ausdrückliche Nutzerfreigabe genau dieser Artefakte an. **Warte auf die
Antwort; `planned` bedeutet nicht genehmigt.** Erfasse die tatsächliche Entscheidung
nach dem gemeinsamen Freigabemodell. Kein eigener Code und keine neuen
Implementierungstests vor diesem Gate.

Rückgabe: Ticket-/Planpfade, Revisionen, gültige Spec-/Planbelege, noch offene
Entscheidungen und nächster erlaubter Schritt. Ereignisse und verfügbare Messdaten
nach der [Erfassungsregel](../guided-software-development/references/09-evaluation.md)
aktualisieren. Danach an die zentrale Steuerung zurückgeben; Implementierungs-Skill
nicht automatisch starten.
