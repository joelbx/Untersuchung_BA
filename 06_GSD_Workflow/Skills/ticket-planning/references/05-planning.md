# Phase 5: Ticketplan und Freigabe

**Eingang:** Ticket, gültige Spec-Freigabe, erledigte Abhängigkeiten.
**Ausgang:** Kurzer konkreter Plan und menschliche Freigabe.

Lies die betroffenen Komponenten, Schnittstellen, vorhandenen Tests und geltenden
Projektregeln. Erfasse den Ist-Zustand einschließlich vorhandener Arbeitsänderungen;
überschreibe oder verwerfe keine fremden Änderungen.

Nutze `assets/implementation-plan.md`. Nenne betroffene Dateien/Komponenten,
vorgesehene Änderungen, Schnittstellen, Prüfstrategie und relevante Risiken.
Dateipfade gehören in diesen aktuellen Plan, nicht als dauerhaftes fachliches
Versprechen in die Spezifikation.

Lege die Prüfgrenzen fest: welche öffentliche Schnittstelle wird mit welchen
Kriterien getestet, was wird nicht erfasst? Relevante Tests, Build, Regression,
visuelle Checks und benötigte Dienste benennen. Bei nicht sinnvoller TDD-Anwendung
die Alternative jetzt begründen. Eine neue Schnittstelle oder Abhängigkeit als
Vorschlag sichtbar machen, statt sie unbemerkt einzuführen.

Dokumentiere Planrevision, betroffene Ticketrevision, Spec-Revision sowie Code-
Ausgangspunkt je Repository. Setze Ticket `planned`. Lege Ticket und Plan zusammen
vor, frage nach Freigabe der konkreten Revision und warte.

Bei Zustimmung Beleg für **Ticket und Plan** erfassen und IDs verknüpfen. Wenn
der Nutzer korrigiert, Plan überarbeiten und erst die endgültige Fassung freigeben
lassen. Keine erneute Bestätigung unveränderter bereits freigegebener Inhalte.

**Gate:** Erst mit gültiger Spec- und Planfreigabe darf Phase 6 beginnen.
Freigabe der Planung ersetzt weder Review noch menschliche Endabnahme.
