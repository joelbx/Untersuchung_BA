# Ticketbezogenes Grill-me vor der Umsetzung

Lies Ticket, freigegebene Spec, relevante Entscheidungen, Mockups und Projektcode.
Prüfe den tatsächlichen Inhalt von `grill-me` beziehungsweise dessen `grilling`-
Abhängigkeit, wenn verfügbar. Hier ist `grill-me` nur ein Wrapper für `grilling`.
Nutze dessen Entscheidungsbaum-Prinzip mit folgenden bewussten Anpassungen:

- Grenze die Klärung auf dieses Ticket und seine Umsetzung ein. Kein erneutes
  Interview zur gesamten freigegebenen Spezifikation.
- Kläre Fakten selbst durch Lesen und bestehende Checks. Keine zusätzlichen
  Recherche-Agenten als implizite Folge des Fremd-Skills starten.
- Stelle jeweils eine entscheidbare Frage mit Empfehlung und Begründung. Warte
  auf die echte Antwort, bevor davon abhängige Entscheidungen geklärt werden.
- Prüfe Schnittstellen, fachliche Randfälle, Fehlerbehandlung, Testgrenzen,
  Architekturentscheidungen und Mockup-Konflikte. Stelle keine bereits beantworteten
  Fragen. Sind keine Entscheidungen offen, dokumentiere das statt Fragen zu erfinden.
- Halte Fragen, Antworten, Quelle und Entscheidung in den Feature-Artefakten fest;
  die konkrete Planfreigabe bestätigt anschließend das gemeinsame Verständnis.
- Berührt eine Antwort neue Anforderungen oder widerspricht sie der Spec, stoppe
  die betroffene Umsetzung und lasse die Spec samt Freigaben aktualisieren.

Diese Anleitung ist auch ohne installierten Fremd-Skill eigenständig ausführbar.
Dann „angepasstes Grill-me-Prinzip“ protokollieren, nicht behaupten, der originale
Skill sei geladen worden. Das Original stellt ganze Fragerunden und verlangt
Recherche-Subagenten; hier gelten die Einzelfragenpräferenz und die vereinbarte
sequenzielle Agentenkonfiguration. Kein Produktivcode und keine neuen Tickettests
vor der Planfreigabe.
