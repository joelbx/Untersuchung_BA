---
name: guided-software-development
description: >-
  Organisiert einen nachvollziehbaren Mensch-KI-Entwicklungsworkflow aus Anforderungen
  und Mockups: Klärung, freigegebene Spezifikation, Tickets, freigegebene Ticketpläne,
  TDD, Verifikation, Review und menschliche Abnahme. Verwenden, wenn der Nutzer
  Softwareentwicklung ausdrücklich geführt, spezifikationsbasiert oder mit
  dokumentierten menschlichen Kontrollpunkten durchführen oder wiederaufnehmen will.
metadata:
  version: "1.3.0"
  language: "de"
---

# Guided Software Development

Organisiere die Arbeit; der Mensch entscheidet über fachlichen Umfang, Freigaben
und Abnahme. Steuere die Tickets sequenziell und starte für jede Entwicklungsphase einen
frischen Agenten ohne geerbten Chatverlauf.

## Start und Wiederaufnahme

1. Identifiziere das vom Nutzer gemeinte Projekt bzw. die Repository-Grenzen.
   Lies die geltenden Projektanweisungen und die Dokumentationskonventionen.
   Bei unklarer Projektzuordnung zunächst den Zielbereich klären, nicht beliebige
   Repositories durchsuchen oder verändern.
2. Lies [Persistenz und Freigaben](references/persistence.md). Suche den bestehenden
   Feature-Artefaktordner. Standard für neue Features ist
   `docs/guided-development/<feature-id>/`, sofern Projektkonventionen nichts anderes
   vorsehen. Bestehende Artefakte fortführen, niemals ungeprüft überschreiben.
3. Bei Wiederaufnahme: `workflow.json`, die referenzierten Freigaben und die für den
   nächsten Schritt relevanten Artefakte lesen. Berichte aktuellen Zustand,
   gültige Freigaben, Blocker und nächsten erlaubten Schritt.
4. Lies die [gemeinsamen Regeln](references/workflow-rules.md). Lade danach nur
   den Unter-Skill der aktuellen Phase und die konkret benötigten Ressourcen.
   Nicht alle fünf Unter-Skills oder deren Referenzen vorsorglich laden.

## Zentrale Steuerung

Du behältst Zustand, fachlichen Umfang, Freigabebelege, Abnahme und Evaluation.
Die verbindlichen gemeinsamen Regeln stehen nur in der oben verlinkten zentralen
Datei. Kein Unter-Skill darf sie durch eigene Freigaberegeln ersetzen.

Vor Implementierung müssen gültige Spec- **und** konkrete Ticketplan-Freigaben
vorliegen. Nur eine ausdrückliche menschliche Ticketabnahme erlaubt `done`.
Bewahre diese Gates auch beim Übergang zwischen Skills und nach Sitzungswechseln.

## Phasenschleife mit frischem Kontext

Lies die [Phasen- und Ticketschleife](references/ticket-loop.md), bevor du die erste
Phase delegierst. Jede Phase erhält einen neuen Agenten ohne geerbten Chatverlauf,
auch Aufnahme, Anforderungsklärung, Spezifikation und Ticketzerlegung. Innerhalb
einer Phase bleibt derselbe Agent für Rückfragen und Iterationen zuständig.
Der Koordinator verwaltet Übergaben, Zustand und menschliche Kontrollpunkte.

Pro Ticket: **Klärung → Planung → menschliche Planfreigabe → Implementierung
→ Verifikation/Review → menschliche Abnahme**. Klärung und Planung sind getrennte
Kontexte. TDD-Schritte bleiben zusammen in der Implementierungsphase. Der frische
Reviewer darf im genehmigten Umfang selbst korrigieren und muss erneut prüfen.
Bei temporärer Prüfhilfe zusätzlich: menschliche Funktionsprüfung → frischer
Rückbau-Agent → frische Abschlussverifikation → endgültige menschliche Abnahme.
Lies dann auch [temporäre Prüfhilfen](references/temporary-test-aids.md).

Nutze die [Phasenübergabe](assets/phase-agent-handoff.json). Fehlt die tatsächliche
Funktion für neue Kontexte, vor Phasenbeginn anhalten und eine neue Sitzung mit der
Übergabe anfordern. Skillwechsel und Kompaktierung sind kein Kontextwechsel.

## Unter-Skills laden und übergeben

Wähle genau einen Eintrag aus dem Router. Nutze eine verfügbare Skill-Aktivierung
oder lasse den frischen Phasenagenten die verlinkte SKILL.md vollständig lesen.
Beim direkten Unter-Skill-Aufruf ohne Koordinator gilt nur dessen Phasenauftrag;
keine abgeschlossene Phase im selben Kontext fortsetzen.
Ein spezielles `Skill`-Tool ist keine Voraussetzung. Das Laden startet **keinen**
neuen Agenten und erzeugt keinen leeren Kontext.

Übergabe: Projektwurzeln, Feature-Artefaktordner, Modus/Phase, aktuelles Ticket,
Artefaktrevisionen/Freigabe-IDs, Blocker und erwartetes Ergebnis. Der Unter-Skill
liest die Belege selbst; eine Aussage „ist schon genehmigt“ ersetzt sie nicht.

Nach dem Ergebnis den gespeicherten Stand und Blocker prüfen, Ereignisse/Messwerte
aktualisieren und erst den nächsten erlaubten Schritt wählen. Bei einer offenen
Freigabe/Abnahme den konkreten Stand vorlegen und auf den Menschen warten.
Die Unter-Skills starten keine nachfolgenden Phasen eigenmächtig. Der Koordinator
prüft Rückgaben und startet die nächste Phase mit einem neuen Agenten. Er selbst
übernimmt weder Planung noch Implementierung als Ersatz für einen Phasenagenten.
Fehlt eine Bundle-Datei, stoppen und ihre Wiederherstellung benennen.

## Phasenrouter

| Phase | Unter-Skill / zentraler Schritt | Ergebnis / Übergang |
|---|---|---|
| 1 | [requirements-clarification](../requirements-clarification/SKILL.md), Modus `intake` | Quelleninventar, Projektgrenzen; `draft → clarification` |
| 2 | [requirements-clarification](../requirements-clarification/SKILL.md), Modus `clarification` | Entscheidungen und explizite offene Punkte |
| 3 | [specification-and-ticketing](../specification-and-ticketing/SKILL.md), Modus `specification` | `specified`; auf Nutzerfreigabe warten |
| 4 | [specification-and-ticketing](../specification-and-ticketing/SKILL.md), Modus `tickets` | Erst nach gültiger Spec-Freigabe Tickets ableiten |
| 5a | [requirements-clarification](../requirements-clarification/SKILL.md), Modus `ticket` | Offene Umsetzungsentscheidungen einzeln klären |
| 5b | [ticket-planning](../ticket-planning/SKILL.md) | `planned`; auf konkrete Planfreigabe warten |
| 6 | [ticket-implementation](../ticket-implementation/SKILL.md) | Nur mit beiden Freigaben implementieren |
| 7 | [verification-and-review](../verification-and-review/SKILL.md) | `reviewing → acceptance`, Befunde und Nachweise |
| 8 | Frische Abnahmevorbereitung nach [Abnahmeregel](references/08-acceptance.md), Entscheidung durch den Menschen | erst nach ausdrücklicher Abnahme Ticket `done` |
| 9 | [Dokumentieren und evaluieren](references/09-evaluation.md) | Messwerte, Grenzen und Übergabe; läuft begleitend |

Ein blockiertes Ticket erhält einen dokumentierten Blocker, keinen erfundenen
Erfolg. Die Phasen dürfen für Korrekturen zurückspringen; vorhandene gültige
Freigaben nicht pauschal verwerfen oder erneut erfragen.

## Vorlagen und Hilfsmittel

Kopiere Vorlagen bei Bedarf in den Feature-Artefaktordner; bearbeite nicht die
installierten Skill-Vorlagen als Projektstatus.

- [Workflow-Zustand](assets/workflow.json), [Abnahme](assets/acceptance.md)
- [Freigabebeleg](assets/approval-record.json), [Prüfhilfe und Rückbau](assets/temporary-test-aid.json)
- [Messwerte je Ticket](assets/measurements.json), [Phasen-/Interaktionsereignis](assets/event.json)
- [Lesender Zustandsprüfer](scripts/check_workflow.py): prüft Artefaktbezüge und
  gespeicherte Gate-Belege, erteilt selbst keine Freigabe.

Fachliche Vorlagen liegen beim jeweiligen Unter-Skill. Gemeinsame Vorlagen und
Gate-Regeln werden nicht kopiert oder an mehreren Stellen unabhängig gepflegt.

Installation, Startbeispiel und Prüfkommandos: [README](README.md).
Herkunft, lokale Bestandsaufnahme und bewusste Anpassungen:
[Quellenvergleich](references/sources.md), [Quellrevisionen](references/sources.json).
