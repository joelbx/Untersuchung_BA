# Phase 1: Anforderungen und Mockups erfassen

**Eingang:** Nutzerauftrag, Zielprojekt, Anforderungen, Bilder/Mockups und Rahmenbedingungen.
**Ausgang:** Quelleninventar, Projektgrenzen und dokumentierte Klärungspunkte.

1. Lies geltende AGENTS-/Repository-Anweisungen, vorhandene Spezifikationen,
   Architekturentscheidungen und die für den Auftrag nötigen Komponenten.
   Mehrere Git-Repositories getrennt erfassen; nicht vom übergeordneten Ordner auf
   eine gemeinsame Codebasis schließen. Keine Rechnungsregeln oder Frameworks voraussetzen.
2. Fasse den belegten Ist-Zustand knapp zusammen. Fehlende Projektinformationen
   zunächst lokal nachschlagen; fachliche Absicht entscheidet der Mensch.
3. Erfasse je Quelle ID, Ort, Version/Hash falls verfügbar, Geltungsbereich und
   Bezug auf Anforderungen. Markiere Dokumentkonflikte ausdrücklich.
4. Öffne die tatsächlich bereitgestellten Mockups mit verfügbaren Bild-/Browser-
   Werkzeugen. Halte sichtbare Zustände, Layout, Texte, Komponenten, Interaktionen
   und vorgegebene Viewports fest. Ein statisches Mockup erfindet keine unsichtbaren
   Fehler-, Lade-, Berechtigungs- oder Responsivzustände; solche Lücken klären.
5. Falls ein Bild nicht erreichbar oder lesbar ist, benenne die Grenze. Nicht
   behaupten, es geprüft zu haben. Wenn nötig den Nutzer um zugängliche Dateien bitten.
6. Erfasse bekannte Test-/Build-Befehle, Dienste und Baseline-Probleme. Vorhandene
   Checks dürfen lesend bzw. ohne Produktivänderungen ausgeführt werden; Ergebnisse
   gelten nur für die geprüfte Basis, nicht für die spätere Implementierung.

Lege den Feature-Artefaktordner nach Projektkonvention an. Kopiere Workflow- und
Entscheidungsvorlage bedarfsweise, setze Feature-ID/Projektbezüge/Quellen und
`status: clarification`. Dokumentiere Phase-Beginn/-Ende und Messwertverfügbarkeit.

**Rückgabe:** Aufnahmeergebnis und nächsten Modus `clarification` an die zentrale
Steuerung übergeben; keine Implementierung beginnen.
