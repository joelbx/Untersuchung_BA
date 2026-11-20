# Phase 3: Dauerhafte Spezifikation

**Eingang:** Geklärte Anforderungen, Entscheidungen, Quellen und offene Punkte.
**Ausgang:** Versionierte Spezifikation und ausdrückliche Nutzerfreigabe.

Nutze `assets/specification.md`. Gib Anforderungen stabile IDs (`FR-001`, `NFR-001`)
und Akzeptanzkriterien IDs (`AC-001`). Beschreibe beobachtbares Verhalten mit
konkreten Beispielen, nicht durch Implementierung allein.

Enthalten sein müssen Ziel, Umfang/Nicht-Ziele, funktionale und relevante
nichtfunktionale Anforderungen, Regeln/Randfälle, technische Rahmenbedingungen,
Mockup-Bezüge, Akzeptanzkriterien, Entscheidungen und offene Fragen.

Trenne verbindliche Anforderungen, bereits beschlossene technische Randbedingungen
und unverbindliche Implementierungsvorschläge. Ein Architekturvorschlag wird erst
durch eine dokumentierte Entscheidung verbindlich. Erzeuge keine überlange Liste
zusätzlicher User Stories als Ersatz für tatsächlich vereinbarten Umfang.

Verknüpfe relevante Bildversionen, Zustände/Viewport und Anforderungs-IDs. Für
Performance, Sicherheit, Accessibility usw. nur begründete Anforderungen aufnehmen;
keine erfundenen Grenzwerte oder pauschalen Zertifizierungsversprechen.

Prüfe die Rückverfolgbarkeit: Jede Anforderung hat eine Quelle/Nutzerentscheidung,
jedes Kriterium eine Anforderung, jeder offene Punkt einen erkennbaren Einfluss.
Setze `specified` und lege genau diese Revision mit offenen Punkten zur Prüfung vor.

Frage ausdrücklich nach Freigabe der konkret verlinkten Revision. Warte auf die
Nutzerentscheidung. Bei Zustimmung Beleg und Hash in `approvals.jsonl` erfassen,
ID im Zustand verknüpfen, Feature auf `approved` setzen. Änderungen vor Zustimmung
einpflegen und die endgültige Revision vorlegen.

**Gate:** Ohne gültige Spec-Freigabe keine Ticketimplementierung. Die Erstellung
dieses Skills oder ein pauschales „mach weiter“ ohne eindeutigen Bezug ist keine
Spec-Freigabe für ein späteres Softwarefeature.
