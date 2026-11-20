# Gemeinsame Regeln des Guided-Workflows

- Erfinde keine fachlichen Anforderungen. Trenne belegte Fakten, offene Fragen,
  Nutzerentscheidungen und technische Vorschläge.
- Verwende Mockups als verbindliche visuelle Referenz innerhalb ihres vereinbarten
  Geltungsbereichs. Kläre Konflikte; dokumentiere ausdrücklich vereinbarte Abweichungen.
- Beginne keine produktive Implementierung und keine für das Ticket geschriebenen
  Implementierungstests vor Spezifikations- **und** Ticketplan-Freigabe.
  Lesende Analyse und bestehende Baseline-Checks sind vorher erlaubt.
- Drei menschliche Kontrollpunkte sind verbindlich: Spezifikation freigeben,
  Ticketplan freigeben, Ticket abnehmen. Schweigen, Zeitablauf, ein Reviewer-Urteil
  oder eine Agentenzusammenfassung ersetzen keine Nutzerentscheidung.
- Freigaben gelten nur für ihren dokumentierten Umfang und die vorgelegten
  Artefaktversionen. Bei inhaltlichen Änderungen betroffene Freigaben neu prüfen.
- Nutze vorhandene Konventionen und Testwerkzeuge. Keine fachfremden Änderungen,
  neuen Abhängigkeiten oder Architekturumbauten ohne Bezug zum freigegebenen Plan.
- Melde ausgeführte, fehlgeschlagene und nicht ausführbare Prüfungen getrennt.
  Ein Exitcode allein beweist keinen fachlichen Test-Erfolg.
- Arbeite lokal als Standard. Keine automatische Tracker-Veröffentlichung,
  Commits, Pushes oder Deployments aus diesem Skill ableiten; bestehende konkrete
  Nutzerautorisierungen und Projektregeln gelten weiterhin.
- Die eigenen Bundle-Unter-Skills verwenden diesen gemeinsamen Kern. Fremde
  Zusatzskills sind optional; prüfe ihre tatsächlichen Inhalte und Voraussetzungen.
  Sie dürfen die Kontrollpunkte nicht überspringen.
  Standard ist ein Koordinator mit genau einem aktiven Phasenagenten. Jede Phase
  startet ohne geerbten Chatverlauf, auch innerhalb desselben Tickets. Keine
  parallelen Tickets. Die TDD-Schritte bilden eine gemeinsame Implementierungsphase.
  Verifikation/Review startet frisch; eigene Reviewer-Korrekturen sind als Selbstreview
  dieser Änderungen zu kennzeichnen. Zusätzliche Agenten außerhalb dieser Phasen nur
  nach Vereinbarung; Faktenrecherche im angepassten Grill-me übernimmt derselbe Agent.
- Temporäre Prüfhilfen sind vor ihrer Erstellung im freizugebenden Plan zu erfassen.
  Die menschliche Funktionsprüfung mit Prüfhilfe ist keine endgültige Ticketabnahme.
  Vor `done` sind Rückbau und frische Abschlussverifikation verbindlich zu belegen.
  Dauerhafte automatisierte Tests bleiben erhalten; keine versteckte Produktoberfläche.


Diese Regeln gelten auch beim direkten Aufruf eines Unter-Skills. Die aktuelle
Version und geltende Projektanweisungen lesen; nicht aus einer früheren Sitzung
rekonstruieren. Freigaben und Status werden ausschließlich nach dem gemeinsamen
Persistenzmodell dokumentiert.
