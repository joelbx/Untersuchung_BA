#!/usr/bin/env python3
"""Read-only V2 report; never blends old experiment scores or calls a model."""
import json
import argparse
import re
from pathlib import Path

parser = argparse.ArgumentParser(description="Generate local benchmark reports without model calls")
parser.add_argument("--experiment", required=True, help="Experiment directory inside the lab")
parser.add_argument("--batch", default="batch-01", help="Batch directory, default: batch-01")
args = parser.parse_args()
if not args.batch.startswith("batch-") or "/" in args.batch or "\\" in args.batch:
    parser.error("Use a batch directory name such as batch-02")
LAB = Path(__file__).resolve().parent
if not re.fullmatch(r"experiment-[A-Za-z0-9][A-Za-z0-9_-]*", args.experiment):
    parser.error("Use an experiment directory such as experiment-luna-01")
experiment = (LAB / args.experiment).resolve()
if experiment.parent != LAB:
    parser.error("Experiment must be inside the laboratory")
ROOT = experiment / args.batch
manifest_path = ROOT / "manifest.json"
manifest = json.loads(manifest_path.read_text())
rows = []
for number in manifest["tasks"]:
    for setup in manifest["setups"]:
        path = ROOT / f"task-{number:02d}" / setup / "result.json"
        if path.exists():
            result = json.loads(path.read_text())
            stages = result.get("stages", [])
            usage_complete = bool(stages) and all(stage.get("usage_complete") for stage in stages)
            usage = {key: sum((stage.get("usage") or {}).get(key, 0) for stage in stages)
                     for key in ("input_tokens", "cached_input_tokens", "output_tokens")}
            rows.append({"task": number, "setup": setup, "status": result["status"],
                         "resolved": result.get("resolved", False), "usage": usage,
                         "usage_complete": usage_complete,
                         "elapsed_codex_seconds": result.get("elapsed_codex_seconds"),
                         "correction_started": result.get("correction_started", False),
                         "result_path": str(path),
                         "model_timeout_seconds": stages[0].get("timeout_seconds", 900) if stages else None,
                         "reported_error_count": sum(stage.get("reported_error_count", 0) for stage in stages)})
summary = {"version": manifest["version"], "status": manifest["status"], "model": manifest["model"], "reasoning": manifest["reasoning"], "execution_mode": manifest.get("execution_mode"), "rows": rows,
           "replacements": manifest.get("replacements", []),
           "model_timeout_policy": manifest.get("model_timeout_policy")}
expected = len(manifest["tasks"]) * len(manifest["setups"])
lines = [f"# SWE-bench Pro Verified – {args.batch}", "",
         f"Aufgaben {manifest['tasks']}; Setups {manifest['setups']}.",
         f"Modell: {manifest['model']}, {manifest['reasoning']}; ChatGPT-Abo; keine externe Recherche.", "",
         f"Status: **{manifest['status']}**. Vorliegende Ergebnisse: {len(rows)}/{expected}.",
         "Modellfrist: " + (manifest.get("model_timeout_policy") or
                            ("keine" if manifest.get("model_timeout_seconds", 900) is None else "900 Sekunden pro Rolle")) + ".", "",
         "## Ergebnisse", "",
         "| Aufgabe | Setup | Status | Gelöst | Codex-Zeit (s) | Korrektur |",
         "| --- | --- | --- | --- | ---: | --- |"]
for row in rows:
    duration = row["elapsed_codex_seconds"]
    duration = f"{duration:.2f}" if duration is not None else "–"
    lines.append(f"| {row['task']} | {row['setup']} | {row['status']} | "
                 f"{'Unbestimmt' if row['resolved'] is None else ('Ja' if row['resolved'] else 'Nein')} | {duration} | "
                 f"{'Ja' if row['correction_started'] else 'Nein'} |")
lines.extend(["", "Zeiten werden für beide Setups monoton gemessen. Vorbereitung, Kontrollen und offizielle",
              "Bewertung sind nicht in der Codex-Zeit enthalten. Cached input ist Teil des Input-Verbrauchs.",
              "Unvollständige Tokenangaben werden ausdrücklich markiert; Abo-Prozente lassen sich daraus nicht ableiten.",
              "Technische Bewertungsprobleme werden nicht als nachgewiesene funktionale Fehler interpretiert.", "",
              "## Kontrollen und Nachweise", ""])
for number in manifest["tasks"]:
    controls = ROOT / f"task-{number:02d}" / "controls.json"
    if controls.exists():
        result = json.loads(controls.read_text())
        lines.append(f"- Aufgabe {number}: Kontrollen {'bestanden' if result['passed'] else 'fehlgeschlagen'}; "
                     f"[Kontrollbericht]({controls}). Modellverbrauch: 0 Tokens.")
if manifest.get("replacements"):
    lines.extend(["", "## Zusammenführung und Wiederholung", "",
                  "Die aktive Standard-Abgabe von Aufgabe 3 ist die erfolgreiche Wiederholung ohne Modell-Zeitlimit.",
                  "Die anderen fünf Abgaben wurden mit 900 Sekunden pro Rolle ausgeführt und bleiben unverändert.",
                  "Der durch Verbindungsprobleme beeinträchtigte ursprüngliche Versuch ist aus der aktiven",
                  "Ergebnisliste entfernt und unverändert im technischen Archiv erhalten. Seine Laufzeit und",
                  "sein teilweise unbekannter Tokenverbrauch sind nicht im Aufwand der sechs aktiven Abgaben enthalten.",
                  "Diese Zusammenstellung enthält unterschiedliche Zeitlimit-Konfigurationen und eine Wiederholung;",
                  "sie ist kein neuer einheitlicher Durchlauf. Ein kausaler Effekt des entfernten Limits ist nicht belegt.", "",
                  f"- [Archivierter Originalversuch]({ROOT / 'technical-interruptions/task-03-standard-attempt-01/result.json'})",
                  f"- [Zusammenführungsnachweis]({ROOT / 'consolidation-audit.json'})",
                  f"- [Konfiguration der Wiederholung]({ROOT.parent / 'provenance/no-timeout/batch-01/manifest.json'})"])
lines.extend(["", f"- [Manifest und Versionshashes]({manifest_path})",
              f"- [Bestätigte ursprüngliche Entscheidungen]({ROOT.parent.parent / 'experiment-v2/DECISIONS.md'})", "",
              "Je Rolle: prompt.txt, developer-instructions.txt, events.jsonl, stderr.log, commands.jsonl,",
              "network.jsonl, network-checks.json, container.json, checkpoint.md, answer.md, repository.patch, stage.json.",
              "Je Abgabe: submission.patch, Patchprüfungen, offizielle evaluation/evaluation.json, result.json.",
              "Alle Protokolle liegen auf dem Host und sind für die Lösungsagenten nicht eingebunden.", ""])
(ROOT / "results.json").write_text(json.dumps(summary, indent=2) + "\n")
(ROOT / "report.md").write_text("\n".join(lines))
print(json.dumps({"status": summary["status"], "completed_submissions": len(rows),
                  "resolved": sum(row["resolved"] is True for row in rows)}))
