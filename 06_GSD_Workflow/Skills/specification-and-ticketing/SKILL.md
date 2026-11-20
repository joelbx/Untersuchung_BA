---
name: specification-and-ticketing
description: >-
  Erstellt im guided-software-development-Workflow eine versionierte Spezifikation
  aus geklärten Anforderungen oder zerlegt eine ausdrücklich freigegebene Spec in
  rückverfolgbare Tickets. Verwenden für diese beiden geführten Aufgaben;
  erzeugt weder Implementierung noch automatische Tracker-Veröffentlichungen.
metadata:
  version: "1.3.0"
  workflow-bundle: "guided-software-development-1.3.0"
---

# Specification and Ticketing

## Voraussetzungen

Lies die [gemeinsamen Regeln](../guided-software-development/references/workflow-rules.md)
und [Persistenz/Gates](../guided-software-development/references/persistence.md),
auch bei direktem Aufruf. Ermittle Projekt, Feature-Artefaktordner, Quellen und
aktuellen Zustand. Fehlt der gemeinsame Kern, dessen Installation verlangen;
keine eigenen Ersatz-Freigaberegeln erfinden.

## Modus `specification`

Lade nur [Spezifikation](references/03-specification.md) und bei Bedarf die
[Spec-Vorlage](assets/specification.md). Arbeite aus belegter Klärung. Ungelöste
Fragen benennen und blockierenden Klärungsbedarf zurückgeben; Antworten nicht erfinden.

Erstelle eine konkrete versionierte Spec mit Quellen, Kriterien und Mockup-Bezügen.
Lege sie mit dem Status `specified` dem Menschen vor. **Hier warten**, wenn keine
eindeutige Freigabe dieser Revision vorliegt. Keine Tickets oder Implementierung
allein aus der Erstellung der Spec ableiten. Eine tatsächliche Freigabe nach dem
zentralen Modell erfassen; die Entscheidung trifft ausschließlich der Mensch.

## Modus `tickets`

Prüfe selbst, dass die referenzierte Spec-Version einen gültigen menschlichen
Freigabebeleg hat. Das Wort `approved` oder eine mündliche Zusammenfassung des
Oberskills genügt nicht. Fehlt der Beleg, Spec vorlegen und warten.

Erst danach [Ticketzerlegung](references/04-tickets.md) und bei Bedarf die
[Ticketvorlage](assets/ticket.md) laden. IDs, Kriterien, Mockups, Blocking-Kanten,
Testabsicht und Definition of Done festhalten. Keine zusätzlichen Anforderungen
einführen. Nicht automatisch ein zusätzliches pauschales Ticket-Freigabe-Gate erzeugen.

Ohne Modus anhand des Zustands wählen: unfertige/ungeklärte Spec → Spezifikation;
gültig freigegebene Spec plus Auftrag zur Zerlegung → Tickets. Bei unklarem Auftrag
eine gezielte Frage stellen, nicht beide Aufgaben stillschweigend verbinden.

## Rückgabe

Gib Artefaktpfade/Revisionen, Kriterienzuordnung, Freigabestatus, Blocker und nächstes
freies Ticket zurück. Dokumentiere verfügbare Ereignisse nach der
[Erfassungsregel](../guided-software-development/references/09-evaluation.md).
Keine Implementierung, kein automatisches `done`, keine externen Publikationen.
Die zentrale Steuerung wählt den nächsten Skill.
