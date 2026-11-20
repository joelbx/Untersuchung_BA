---
name: verification-and-review
description: >-
  Verifiziert und reviewt Änderungen eines geführten Entwicklungstickets gegen
  Akzeptanzkriterien, Projektstandards und relevante Mockups. Verwenden im
  guided-software-development-Workflow oder für dessen ausdrücklich angeforderten
  Review-Schritt; bereitet menschliche Abnahme vor, erteilt sie aber nicht.
metadata:
  version: "1.3.0"
  workflow-bundle: "guided-software-development-1.3.0"
---

# Verification and Review

Lies die [gemeinsamen Regeln](../guided-software-development/references/workflow-rules.md)
und [Persistenz/Gates](../guided-software-development/references/persistence.md),
auch bei direktem Aufruf. Fehlt der gemeinsame Kern, die vollständige Installation
benennen. Ermittle Projekt, Feature-Artefaktordner, Ticket und tatsächlichen Code-Diff.

Lies Spec, Plan, Kriterien, Mockups, Standards und Freigabebelege. Bei Änderungen
ohne erforderliche Freigaben darfst du den Verstoß lesend dokumentieren; eine
nachträgliche technische Prüfung macht ihn nicht genehmigt. Produktive Korrekturen
sind erst innerhalb eines gültig freigegebenen Umfangs erlaubt.

Lade [Verifikation/Review](references/07-verification-review.md) und bei Bedarf die
[Reviewvorlage](assets/review.md). Prüfe Spec und Standards getrennt, benenne den
tatsächlichen Prüfstand einschließlich unversionierter Änderungen und sichere
ausgeführte Prüfungen, Ergebnisse und visuelle Belege. Ohne echte Sichtprüfung
keine behauptete Mockup-Übereinstimmung.

Im geführten Workflow startest du mit frischem Kontext gegenüber der
Implementierung. Du darfst Befunde innerhalb des freigegebenen Plans selbst
korrigieren und musst die betroffenen Prüfungen danach erneut ausführen. Kennzeichne
diese eigenen Änderungen als Selbstreview; die Kontexttrennung macht sie nicht
unabhängig geprüft. Keine fachlichen Erweiterungen ohne entsprechende Freigabe.
Im Modus `final_verification` nach Rückbau zusätzlich die
[Prüfhilfenregeln](../guided-software-development/references/temporary-test-aids.md)
lesen und den endgültigen Stand samt Entfernung nachweisen. Wird erneut eine
Prüfhilfe nötig, neuen Prüf-/Rückbauzyklus dokumentieren, nicht endgültig abnehmen.

Gib Befunde, Korrekturen, Nachprüfungen, Grenzen und Bereitschaft zur Abnahme zurück.
Aktualisiere Ereignisse nach der [Erfassungsregel](../guided-software-development/references/09-evaluation.md).
Bei offenem wesentlichem Korrekturbedarf weiter `reviewing`/blockiert; sonst darf
der Stand `acceptance` werden. **Niemals selbst menschlich abnehmen oder `done`
setzen.** Die zentrale Steuerung legt den Stand dem Menschen vor.
