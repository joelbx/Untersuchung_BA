# Phase 9: Dokumentation und wissenschaftliche Erfassung

Diese Phase begleitet alle anderen Phasen; fehlende Zeitmessung lässt sich am Ende
nicht zuverlässig aus einer Chatlänge rekonstruieren. Verwende ein Ereignisjournal
und eine Messwertdatei je Ticket. Erfinde keine Zahlen und keine Metadaten des Hosts.

## Erfassung

Nutze `assets/event.json` als Schema für einen Eintrag in `events.jsonl` und
`assets/measurements.json` für `metrics/<ticket-id>.json`. Platzhalter `null` mit
Grund beibehalten, wenn Daten fehlen. Null bedeutet unbekannt; 0 bedeutet tatsächlich
beobachtete Null. Zahlen benötigen Einheit, Quelle und Erfassungsumfang.

Erfasse soweit zuverlässig beobachtbar:
- tatsächlich geladene eigene Bundle-Komponenten mit Version/Hash getrennt von
  optionalen Fremd-Skills; bloße Installation/Discovery zählt nicht als Verwendung;
- Modell-ID, Reasoning, Skill-Versionen/Hashes, tatsächlich verwendete Zusatzskills,
  Agentenrollen und Einzel-/Multi-Agent-Konfiguration; unbekannte Hostwerte als solche;
- Beginn/Ende der Phasen und Arbeitssegmente in ISO 8601 mit Zeitzone;
- Input/Output/Cache-Tokens nur aus zuverlässigen Nutzungsdaten, mit Session-/Thread-
  Bezug und Angabe, ob Einzelaufruf oder kumulativer Zähler;
- Agentenlaufzeit, aktive menschliche Arbeitszeit, menschliche Fragen/Antworten,
  Freigaben, ungeplante Eingriffe, Korrekturschleifen, Ergebnisqualität und Abweichungen.

Ein Ereignis erhält eine eindeutige ID und `kind`, z.B. `phase_started`,
`phase_finished`, `clarification_question`, `human_answer`, `approval_requested`,
`approval_granted`, `acceptance_requested`, `acceptance_granted`,
`unplanned_human_intervention`, `correction_cycle`, `technical_interruption`.
Mehrere echte Fragen in einer Nachricht erhalten einzelne Frage-IDs; eine gezielte
Nachfrage zählt als neue Frage, eine unveränderte Wiederholung wegen Übertragungsfehler
nicht als neue fachliche Frage. Antworten und Freigaben nicht doppelt zählen.

**Geplante Kontrollpunkte:** Anforderungsklärung, Spec-/Planfreigabe, gegebenenfalls Funktionsprüfung mit temporärer Prüfhilfe und Endabnahme.
**Ungeplante Eingriffe:** Mensch muss z.B. einen Hänger stoppen, eine falsche Agenten-
Annahme außerhalb eines Kontrollpunkts korrigieren oder die Umgebung reparieren.
Gleiche Handlung nicht in beide Klassen rechnen. Herkunft und Zeitpunkt festhalten.

Eine Korrekturschleife ist ein dokumentierter Rücksprung nach fehlgeschlagenem Test,
Reviewbefund oder abgelehnter Abnahme zu erneuter Änderung/Prüfung. Mehrere Befunde,
die in einer gemeinsamen Überarbeitung bearbeitet werden, sind eine Schleife;
ein unveränderter erneuter Testlauf allein ist keine neue Implementierungsschleife.

## Messgrenzen

Agenten-Walltime ist der beobachtete Zeitraum aktiver Arbeit einschließlich Tools;
Wartezeit auf menschliche Antworten getrennt erfassen. Tokenzahlen messen keine
reine Rechenzeit. Bei parallelen Agenten Gesamt-Walltime und summierte Agentenzeit
trennen; überlappende Laufzeiten nicht als verstrichene Zeit ausgeben. Menschliche
aktive Zeit nur mit realem Timer/Selbstbericht erfassen, niemals aus Antwortlatenz.

Kumulative Tokenzähler innerhalb desselben Threads differenzieren statt jede
Zwischensumme erneut zu addieren. Cache ist Teil von Input, Reasoning ggf. Teil von
Output; nicht doppelt zählen. Bei unbekannter Zählersemantik keine Gesamtsumme
erfinden. Unterbrochene Versuche/Tools und Reviewer-Aufwand mit erfassen oder
bekannte Untergrenzen ausdrücklich kennzeichnen. Keine Ableitung von Abo-Prozenten.

Ergebnisqualität als Matrix pro Akzeptanzkriterium dokumentieren: bestanden,
fehlgeschlagen, ungeprüft; dazu Belege und getrennt die menschliche Abnahme.
Keine unbegründete Gesamtnote und keine Wirksamkeitsbehauptung aus einem Einzelfall.

Bei jeder Pause offene Messlücken benennen; zum Ticketabschluss tatsächlichen Stand
und Quellen sichern. Änderungen am Workflow als Abweichung mit Grund protokollieren,
die Skill-Version für eine Untersuchungsphase festhalten. Für reproduzierbare
Untersuchungen nicht nur SKILL.md hashen: eine Git-Revision oder ein Hashmanifest
aller tatsächlich eingesetzten Bundle-Komponenten einschließlich ihrer Referenzen/Vorlagen
erfassen. Ein Versionswechsel während eines Tickets ist eine dokumentierte Abweichung.

## Phasenübergaben und Rückbau

Erfasse jeden frischen Phasenversuch und Kontextnachweis; Skillwechsel nicht als
Agentenstart zählen. Übergebene Artefakte/Hashes statt Chatvererbung dokumentieren.
Koordinatoraufwand und gemeinsame Feature-Phasen getrennt von Ticketphasen zuordnen,
ohne mehrfaches Addieren. Rückbau und finale Verifikation als eigene Phasen messen.
Menschliche Funktionsprüfung und endgültige Abnahme sind verschiedene geplante
Kontrollpunkte. Messführung ist begleitende Koordinatorarbeit, kein Agentenwechsel
pro Logeintrag. Fehlende Laufzeitdaten ausdrücklich als unbekannt ausweisen.
