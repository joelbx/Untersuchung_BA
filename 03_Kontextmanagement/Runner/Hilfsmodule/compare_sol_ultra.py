"""Read-only scoring/usage comparison for the fresh native Ultra experiment."""
import csv
import hashlib
import json
from pathlib import Path

from compare_reasoning import paired_comparison

FINAL = {'completed','empty_submission','invalid_submission'}


def build(root):
    root=Path(root)
    m=json.loads((root/'manifest.json').read_text())
    if m.get('version')!='sol-native-ultra-v1' or m.get('model')!='gpt-6-sol' or m.get('baseline')!='fresh':
        raise ValueError('Unexpected comparison protocol')
    eligible=[n for n in m['tasks'] if n not in m['control_exclusions']]
    variants={};delegations=[]
    for arm in m['arms']:
        rows={};known={k:0 for k in ('input_tokens','cached_input_tokens','output_tokens')}
        stages=[];seconds=0
        for n in eligible:
            directory=root/f'task-{n:02d}'/arm;p=directory/'result.json'
            result=json.loads(p.read_text()) if p.exists() else {'status':'missing'}
            rows[n]={'result':result,'source':str(p),
                     'sha256':hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None}
            stages.extend(result.get('stages',[]))
            seconds+=result.get('elapsed_codex_seconds',0)
            if result.get('status')=='completed':
                e=json.loads((directory/'evaluation/evaluation.json').read_text())
                if not e.get('completed') or e.get('resolved')!=result.get('resolved'):
                    raise ValueError(f'Task {n}/{arm}: evaluation and result differ')
            audit=directory/'standard/native-agents.json'
            if audit.exists():
                a=json.loads(audit.read_text())
                delegations.append({'task':n,'arm':arm,'child_thread_ids':a['child_thread_ids'],
                                    'usage_complete':a['usage_complete'],'audit':str(audit)})
        for stage in stages:
            for key in known:known[key]+=int((stage.get('usage') or {}).get(key) or 0)
        finished=sum(v['result'].get('status') in FINAL for v in rows.values())
        complete_usage=finished==len(eligible) and bool(stages) and all(s.get('usage_complete') for s in stages)
        variants[arm]={'rows':rows,'summary':{'tasks':len(eligible),'finished':finished,
            'solved':sum(v['result'].get('resolved') is True for v in rows.values()),
            'known_usage':known,'usage_complete':complete_usage,'codex_process_seconds':seconds,
            'complete_usage_stages':sum(bool(s.get('usage_complete')) for s in stages),
            'stages':len(stages)}}
    final=all(v['summary']['finished']==len(eligible) for v in variants.values())
    test=paired_comparison(variants['medium']['rows'],variants['ultra']['rows'],eligible) if final else None
    return {'manifest_source':str(root/'manifest.json'),
            'manifest_sha256':hashlib.sha256((root/'manifest.json').read_bytes()).hexdigest(),
            'batch_status':m['status'],'tasks':eligible,'control_exclusions':m['control_exclusions'],
            'final':final,'variants':variants,'paired_test':test,'native_agents':delegations,
            'analysis_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


def write(root):
    root=Path(root);d=build(root)
    (root/'sol-medium-ultra.json').write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
    lines=['# Sol 6 medium versus native Ultra','',
           f"Status: {d['batch_status']}; endgültig auswertbar: {d['final']}.",
           f"Gemeinsamer Nenner: {len(d['tasks'])} Aufgaben. Ausschlüsse: {d['control_exclusions']}.",'',
           '| Variante | Fertig | Gelöst | Bekannte Eingabe + Ausgabe, Mio. | Tokenverbrauch vollständig? |',
           '|---|---:|---:|---:|---|']
    for arm,v in d['variants'].items():
        s=v['summary'];u=s['known_usage'];total=u['input_tokens']+u['output_tokens']
        lines.append(f"| {arm} | {s['finished']}/{s['tasks']} | {s['solved']}/{s['tasks']} | {total/1e6:.2f} | {s['usage_complete']} |")
    lines+=['','Beide Varianten werden frisch gestartet. Nur passende Kontrollnachweise und identische vorbereitete Images werden wiederverwendet.',
            'Medium verwendet das bisherige Standard-Setup ohne native Agenten. Ultra kombiniert Reasoning ultra mit nativen Codex-Unteragenten.',
            'Damit wird die Kombination aus Reasoning und Orchestrierung untersucht, nicht der isolierte Effekt nur eines Faktors.',
            'Native Unteragenten gehören zu demselben Container; sie sind keine separat isolierten Rollen-B/C-Container.',
            'Modell/Reasoning-Defaults der Unteragenten sind Sol 6 / ultra. Tatsächliche Aufrufe und Metadaten bleiben in den Rollouts erhalten.',
            'Es gelten Codex-Standardgrenzen für native Delegation, keine benutzerdefinierte Pflicht oder Gesamtzahl von Unteragenten.','',
            'Tokenwerte summieren eindeutige Thread-Zähler. Root-CLI-Nutzung dient nur als Fallback für denselben Root-Thread.',
            'Bei fehlenden oder unvollständigen Thread-Protokollen sind die Werte nur bekannte Mindestwerte; keine vollständigen Kostenvergleiche ableiten.',
            'Cache-Tokens sind Teil der Eingabe, Reasoning-Tokens Teil der Ausgabe. Keine direkten Abo-Prozente oder API-Kosten.',
            'Archivierte Unterbrechungen können zusätzlichen Verbrauch verursacht haben und sind nicht in Endversuchen enthalten.',
            'Prozesszeiten enthalten bei Ultra Wartezeiten auf native Unteragenten; parallele Agentenzeiten werden nicht zusätzlich addiert.','']
    if d['paired_test']:
        t=d['paired_test'];lines += [f"Nur Medium gelöst: {t['a_only_solved']}; nur Ultra: {t['b_only_solved']}.",
            f"Exakter zweiseitiger McNemar-Test: p = {t['mcnemar_exact_two_sided_p']:.6f}.",
            'Ein Endversuch je Aufgabe/Variante; explorativer gepaarter Vergleich ohne Repository-Clusterkorrektur.','']
    lines += [f"Beobachtete native Kind-Threads: {sum(len(a['child_thread_ids']) for a in d['native_agents'])}.",
              '[Daten und Quell-Prüfsummen](sol-medium-ultra.json) · [Aufgaben](sol-medium-ultra.csv)','']
    output=root/'sol-medium-ultra.md';output.write_text('\n'.join(lines)+'\n')
    with (root/'sol-medium-ultra.csv').open('w',newline='') as stream:
        writer=csv.writer(stream);writer.writerow(['task','medium_status','medium_resolved','ultra_status','ultra_resolved'])
        for n in d['tasks']:
            a=d['variants']['medium']['rows'][n]['result'];b=d['variants']['ultra']['rows'][n]['result']
            writer.writerow([n,a['status'],a.get('resolved'),b['status'],b.get('resolved')])
    return output
