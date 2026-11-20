#!/usr/bin/env python3
"""Aggregate the completed fresh Medium/Ultra cohorts, without changing run data."""
import ast
from collections import Counter
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import statistics

import compare_sol_ultra
from compare_reasoning import paired_comparison
from control_reuse import CORE

LAB=Path(__file__).resolve().parent
EXCLUDED=[40,65,127,184,186,217,218,258,261,285]
KEYS=('input_tokens','cached_input_tokens','output_tokens')


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def build():
    evidence={};cohorts=[];rows={a:{} for a in ('medium','ultra')}
    missing_usage=[];agents=[];seen=set();exclusions=[];archives=[]
    archive_errors=set();first=None;signatures=None
    audit=Counter();observed_models=Counter();observed_efforts=Counter()
    master=json.loads((LAB/'selection-extended.json').read_text())
    def remember(p):
        p=Path(p);evidence[str(p.relative_to(LAB))]=sha(p)
    for batch in ('batch-01','batch-02','batch-03'):
        root=LAB/'experiment-sol6-medium-ultra'/batch
        m=json.loads((root/'manifest.json').read_text());d=compare_sol_ultra.build(root)
        assert m['status']=='completed' and d['final'] and not m.get('active_trials')
        assert m['baseline']=='fresh' and m['model']=='gpt-6-sol' and m['model_workers']==5
        assert not seen & set(m['tasks']);seen.update(m['tasks']);exclusions+=m['control_exclusions']
        remember(root/'manifest.json')
        driver=root/'source-snapshot/run_sol_ultra.py'
        assert sha(driver)==m['source_hashes'][str(LAB/'run_sol_ultra.py')]
        funcs={f.name:ast.dump(f,include_attributes=False) for f in ast.parse(driver.read_text()).body
               if isinstance(f,(ast.FunctionDef,ast.AsyncFunctionDef))}
        critical={name:hashlib.sha256(funcs[name].encode()).hexdigest()
                  for name in ('models','resume','validate','capsule')}
        if first is None:first=m;signatures=critical
        else:
            assert signatures==critical and m['protocol']==first['protocol']
            for name in (*CORE,'native_ultra.py','compare_sol_ultra.py'):
                assert m['source_hashes'][str(LAB/name)]==first['source_hashes'][str(LAB/name)],name
            for suffix in ('/bin/codex','/bin/codex-code-mode-host'):
                assert {v for k,v in m['source_hashes'].items() if k.endswith(suffix)}=={
                    v for k,v in first['source_hashes'].items() if k.endswith(suffix)}
        remember(driver)
        for n in m['tasks']:
            case=m['cases'][str(n)];assert case['case']==master['scored_tasks'][n-1]
            if n in m['control_exclusions']:continue
            task=root/f'task-{n:02d}';control=json.loads((task/'controls.json').read_text())
            assert control['passed'] and control['original_completed'] and not control['original_resolved'] and control['reference_resolved']
            audit['controls_checked']+=1;remember(task/'controls.json');remember(task/'preparation/snapshot.json')
            for arm in rows:
                row=d['variants'][arm]['rows'][n];rows[arm][n]=row
                result=row['result'];assert result['status']=='completed' and result['patch_applicable']
                assert result.get('comparison_arm')==arm and result.get('reasoning')==arm
                directory=task/arm;remember(directory/'result.json')
                remember(directory/'evaluation/evaluation.json');audit['evaluations_checked']+=1
                for stage in result['stages']:
                    assert stage['exit_code']==0 and not stage['timed_out'] and not stage['unexpected_web_tools']
                    audit['model_stages_checked']+=1
                inv=json.loads((directory/'standard/invocation.json').read_text())
                argv=inv['argv'];assert argv[argv.index('--model')+1]=='gpt-6-sol'
                assert f'model_reasoning_effort="{arm}"' in argv and inv['auth_mode']=='chatgpt'
                assert ('agents.enabled=true' in argv)==(arm=='ultra')
                c=json.loads((directory/'standard/container.json').read_text())
                assert c['image']==case['snapshot']['prepared_image_id']
                e=json.loads((directory/'evaluation/container.json').read_text())
                assert e['image']==case['snapshot']['original_image_id']
                for p in ('standard/invocation.json','standard/container.json','standard/stage.json','evaluation/container.json'):
                    remember(directory/p)
        for item in d['native_agents']:
            p=Path(item['audit']);remember(p);a=json.loads(p.read_text())
            if not a['usage_complete']:
                missing_usage.append({'task':item['task'],'batch':batch,'reason':a.get('capture_error'),
                                      'source':str(p.relative_to(LAB))})
            audit['tasks_with_observed_children']+=bool(a['child_thread_ids'])
            for t in a['threads']:
                if not t.get('rollout'):continue
                rollout=p.parent/t['rollout'];h=hashlib.sha256();models=set();efforts=set();first_usage=None
                with rollout.open('rb') as stream:
                    for line in stream:
                        h.update(line)
                        if not line.strip():continue
                        event=json.loads(line);payload=event.get('payload') or {}
                        if event.get('type')=='turn_context':
                            if payload.get('model'):models.add(payload['model'])
                            effort=payload.get('effort') or payload.get('reasoning_effort')
                            if effort:efforts.add(effort)
                        if first_usage is None and event.get('type')=='event_msg' and payload.get('type')=='token_count' and payload.get('info'):
                            first_usage=payload['info']
                evidence[str(rollout.relative_to(LAB))]=h.hexdigest()
                observed_models.update(models);observed_efforts.update(efforts)
                audit['rollouts_checked']+=1
                if first_usage:
                    total=first_usage.get('total_token_usage',{});last=first_usage.get('last_token_usage',{})
                    audit['thread_counters_start_at_first_call']+=all(total.get(k)==last.get(k) for k in KEYS)
                if t['thread_id']==a['root_thread_id']:continue
                meta=t['metadata'];source=meta.get('source') or {}
                spawn=((source.get('subagent') or {}).get('thread_spawn') or {}) if isinstance(source,dict) else {}
                agents.append({'task':item['task'],'batch':batch,'thread_id':t['thread_id'],
                    'parent_thread_id':meta.get('parent_thread_id') or spawn.get('parent_thread_id'),
                    'agent_path':meta.get('agent_path') or spawn.get('agent_path'),
                    'agent_role':meta.get('agent_role') or spawn.get('agent_role'),
                    'depth':spawn.get('depth'),'observed_models':','.join(sorted(models)),
                    'observed_efforts':','.join(sorted(efforts)),
                    'known_input_tokens':(t.get('usage') or {}).get('input_tokens'),
                    'known_output_tokens':(t.get('usage') or {}).get('output_tokens'),
                    'source':str(rollout.relative_to(LAB))})
        for p in root.glob('technical-interruptions/*/manifest.json'):
            am=json.loads(p.read_text());remember(p)
            archives.append(str(p.parent.relative_to(LAB)))
            for e in am.get('technical_errors',[]):
                archive_errors.add((e.get('task'),e.get('setup'),e.get('error'),e.get('interrupted_at')))
        cohorts.append({'batch':batch,'source':str(root.relative_to(LAB)),
            'eligible':len(d['tasks']),'excluded':d['control_exclusions'],
            'summaries':{a:v['summary'] for a,v in d['variants'].items()},
            'driver_sha256':sha(driver),'execution_function_signatures':critical})
    assert seen==set(range(1,301)) and sorted(exclusions)==EXCLUDED
    numbers=sorted(rows['medium']);assert len(numbers)==290 and set(numbers)==set(rows['ultra'])
    summaries={}
    for arm,values in rows.items():
        results=[v['result'] for v in values.values()];stages=[s for r in results for s in r['stages']]
        known={k:sum(int((s.get('usage') or {}).get(k) or 0) for s in stages) for k in KEYS}
        known['input_plus_output_tokens']=known['input_tokens']+known['output_tokens']
        known['uncached_input_tokens']=known['input_tokens']-known['cached_input_tokens']
        times=[r['elapsed_codex_seconds'] for r in results]
        summaries[arm]={'tasks':290,'solved':sum(r['resolved'] is True for r in results),
            'known_usage':known,'complete_usage_trials':sum(all(s.get('usage_complete') for s in r['stages']) for r in results),
            'usage_complete':all(s.get('usage_complete') for s in stages),
            'mean_codex_seconds':statistics.mean(times),'median_codex_seconds':statistics.median(times),
            'sum_codex_seconds':sum(times)}
    pair=paired_comparison(rows['medium'],rows['ultra'],numbers)
    return {'created_at':datetime.now(timezone.utc).isoformat(),'model':'gpt-6-sol',
        'cohorts':cohorts,'exclusions':EXCLUDED,'eligible_tasks':numbers,'summaries':summaries,
        'paired_test':pair,'audit':dict(audit),'observed_rollout_models':dict(observed_models),
        'observed_rollout_efforts':dict(observed_efforts),'incomplete_ultra_usage':sorted(missing_usage,key=lambda x:x['task']),
        'agents':agents,'rows':rows,'interruption_archives':archives,
        'unique_archived_errors':[{'task':x[0],'arm':x[1],'error':x[2],'at':x[3]} for x in sorted(archive_errors)],
        'source_evidence_sha256':evidence,'analysis_sha256':{n:sha(LAB/n) for n in
            ['compare_sol_ultra_all.py','compare_sol_ultra.py','compare_reasoning.py']}}


def write(d):
    out=LAB/'reports/sol6-medium-ultra-300';out.mkdir(parents=True,exist_ok=True)
    (out/'summary.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
    with (out/'tasks.csv').open('w',newline='') as stream:
        writer=csv.writer(stream);writer.writerow(['task','excluded','medium_resolved','ultra_resolved','medium_process_seconds','ultra_process_seconds','ultra_usage_complete','observed_child_threads'])
        counts=Counter(a['task'] for a in d['agents'])
        for n in range(1,301):
            if n in EXCLUDED:writer.writerow([n,True,'','','','','','']);continue
            a=d['rows']['medium'][n]['result'];b=d['rows']['ultra'][n]['result']
            writer.writerow([n,False,a['resolved'],b['resolved'],a['elapsed_codex_seconds'],b['elapsed_codex_seconds'],
                             all(s.get('usage_complete') for s in b['stages']),counts[n]])
    with (out/'agents.csv').open('w',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=list(d['agents'][0]));writer.writeheader();writer.writerows(d['agents'])
    a=d['summaries']['medium'];b=d['summaries']['ultra'];t=d['paired_test']
    ratio=b['known_usage']['input_plus_output_tokens']/a['known_usage']['input_plus_output_tokens']
    time_ratio=b['sum_codex_seconds']/a['sum_codex_seconds']
    delta=100*(b['solved']-a['solved'])/290
    lines=['# Gesamtbericht: Sol 6 medium versus natives Ultra','',
        '## Ergebnis','',
        f"Medium löst **{a['solved']}/290**, Ultra **{b['solved']}/290** Aufgaben. Die Differenz Ultra minus Medium beträgt **{delta:+.2f} Prozentpunkte**.",
        f"Der gepaarte exakte zweiseitige McNemar-Test ergibt **p = {t['mcnemar_exact_two_sided_p']:.4f}**.",
        'Es zeigt sich kein statistisch signifikanter Lösungsvorteil von Ultra. Das ist kein Nachweis einer Gleichwertigkeit.',
        f"Ultra benötigt etwa **{time_ratio:.2f}-mal so viel Modellprozesszeit**. Der protokollierte Tokenverbrauch beträgt **mindestens {ratio:.2f}-mal** den Medium-Verbrauch; bei Ultra ist er unvollständig.",'',
        '## Umfang und Aufbau','',
        'Alle drei Batches sind abgeschlossen: 300 ausgewählte Aufgaben, zehn gemeinsame genehmigte Kontrollausschlüsse,',
        '**290 bewertbare Aufgaben und 580 abgeschlossene Endversuche**. Die Ausschlüsse sind '+', '.join(map(str,EXCLUDED))+'.',
        'Es werden ausschließlich die neuen Medium- und Ultra-Ergebnisse dieser Reihe verglichen. Frühere Reasoning- oder MAS-Ergebnisse werden nicht beigemischt.',
        'Beide Arme starten je Aufgabe mit einem frischen Hauptkontext und Container. Nur kontrollvalidierte Umgebungen werden wiederverwendet.',
        'Pro Aufgabe verwenden beide Arme identische vorbereitete Modell-Images und identische offizielle Evaluations-Images.',
        'Medium nutzt Reasoning medium ohne native Agenten. Ultra kombiniert Reasoning ultra mit nativer Orchestrierung und einem entsprechenden Delegationsprompt.',
        'Der Vergleich isoliert deshalb weder den Reasoning-Effekt noch den Multiagenten-Effekt.',
        'Fünf Worker laufen für beide Arme zusammen. Pro Versuch gelten 4 CPUs und 8 GiB RAM; native Kinder teilen diesen Container.',
        'Unteragenten können Elternkontext übernehmen; dies entspricht nicht dem frischen, separat isolierten Rollenkontext des früheren Rollen-B/C-Aufbaus.',
        'Authentifizierung erfolgt über das Abo, externe Recherche ist gesperrt. Es gibt keine Modellzeitgrenze und kein angeglichenes Tokenbudget.','',
        '## Ergebnisse je Aufgabenblock','',
        '| Aufgaben | Bewertbar | Medium gelöst | Ultra gelöst |','|---|---:|---:|---:|']
    for c in d['cohorts']:
        start={'batch-01':'1–100','batch-02':'101–200','batch-03':'201–300'}[c['batch']]
        lines.append(f"| {start} | {c['eligible']} | {c['summaries']['medium']['solved']} | {c['summaries']['ultra']['solved']} |")
    lines+=['','## Lösungsquote, Verbrauch und Dauer','',
        '| Variante | Gelöst | Quote | Bekannte Eingabe + Ausgabe, Mio. | Ø Modellprozesszeit | Median | Vollständige Nutzung |',
        '|---|---:|---:|---:|---:|---:|---:|']
    for arm,s in d['summaries'].items():
        lines.append(f"| {arm} | {s['solved']}/290 | {s['solved']/290:.1%} | {s['known_usage']['input_plus_output_tokens']/1e6:.2f} | {s['mean_codex_seconds']/60:.2f} min | {s['median_codex_seconds']/60:.2f} min | {s['complete_usage_trials']}/290 |")
    lines+=['','| Variante | Eingabe, Mio. | Davon Cache, Mio. | Ungecachte Eingabe, Mio. | Ausgabe, Mio. | Summierte Prozesszeit |',
        '|---|---:|---:|---:|---:|---:|']
    for arm,s in d['summaries'].items():
        u=s['known_usage'];lines.append(f"| {arm} | {u['input_tokens']/1e6:.2f} | {u['cached_input_tokens']/1e6:.2f} | {u['uncached_input_tokens']/1e6:.2f} | {u['output_tokens']/1e6:.2f} | {s['sum_codex_seconds']/3600:.2f} h |")
    lines+=['','Cache-Tokens sind bereits in der Eingabe enthalten und werden nicht nochmals addiert. Reasoning-Ausgaben sind Teil der Ausgabe.',
        'Die Tokenwerte stammen aus eindeutigen Thread-Zählern; Eltern-CLI-Nutzung wird nicht zusätzlich zum gleichen Rollout-Thread addiert.',
        'Dies sind keine Abo-Prozente oder API-Kosten. Bei Ultra handelt es sich um bekannte Mindestwerte, nicht um eine vollständige Abrechnung.',
        'Prozesszeiten enthalten das Warten des Hauptagenten auf Kinder. Parallele Kinderzeiten werden nicht nochmals addiert.',
        'Die Summe ist keine Kalenderlaufzeit bei fünf Workern. Containeraufbau, nachträglicher Protokollexport und offizielle Bewertung sind darin nicht enthalten.',
        'Archivierte technische Fehlstarts sind nicht Bestandteil der Endversuchs-Tabelle.','',
        '## Gepaarte Aufgabenergebnisse','',
        f"Nur Medium gelöst: **{len(t['a_only_solved'])} Aufgaben** – {t['a_only_solved']}.",
        f"Nur Ultra gelöst: **{len(t['b_only_solved'])} Aufgaben** – {t['b_only_solved']}.",
        f"Bei {290-len(t['a_only_solved'])-len(t['b_only_solved'])} Aufgaben stimmen die binären Lösungsergebnisse überein.",
        'Der primäre Test verwendet diese gepaarten Unterschiede, nicht einen ungepaarten Vergleich zweier Quoten.',
        'Es gibt einen primären Gesamtvergleich. Die Blocktabelle ist deskriptiv; einzelne Blöcke sind keine unabhängigen Bestätigungsstudien.','',
        '## Tatsächliche native Delegation','',
        f"Nachgewiesen sind **mindestens {len(d['agents'])} Kind-Threads bei mindestens {d['audit']['tasks_with_observed_children']} von 290 Ultra-Aufgaben**.",
        'Die Kennzeichnung „mindestens“ berücksichtigt die 15 Aufgaben mit fehlendem Rollout-Export. Null beobachtete Kinder bei diesen Aufgaben bedeutet unbekannt, nicht keine Delegation.',
        'Thread-IDs, Rollenpfade, Elternbeziehungen, Tiefe, beobachtete Modelle/Reasoning-Stufen und Protokollquellen stehen in `agents.csv`.',
        'Die frei benannten Rollenpfade sind keine standardisierte Rollentaxonomie. Eine Häufigkeit von Delegation weist allein keinen kausalen Nutzen nach.',
        'Anders als beim früheren freiwilligen Organizer wurden native Unteragenten in dieser Reihe auf einem großen Teil der Aufgaben tatsächlich genutzt.','',
        '## Einschränkung der Token- und Delegationsprotokolle','',
        f"Bei **{len(d['incomplete_ultra_usage'])} Ultra-Aufgaben** konnte der Hilfsprozess die Sitzungsdateien nicht exportieren:",
        '`AttributeError: PosixPath object has no attribute is_relative_to`.',
        'Der Exportcode verwendete eine Methode, die der ältere Python-Interpreter dieser Images nicht anbietet. Dies ist ein Fehler im Protokollierungshelfer.',
        'Betroffene Aufgaben: '+', '.join(str(x['task']) for x in d['incomplete_ultra_usage'])+'.',
        'Der Fehler trat nach dem Modellprozess beim Einsammeln der Logs auf. Die offiziellen Auswertungen und finalen Patches liegen vor;',
        'der Lösungsvergleich verwendet weiterhin alle 290 Aufgaben. Für diese 15 Aufgaben ist nur die Eltern-CLI-Nutzung erfasst;',
        'möglicher zusätzlicher Unteragentenverbrauch und deren vollständige Rollenprotokolle fehlen. Es wurden keine Aufgaben deswegen nachträglich ausgeschlossen.',
        'Für Folgeversuche sollte der Export kompatibel mit den älteren Python-Versionen umgesetzt werden; dieser Bericht verändert keine historischen Dateien.','',
        '## Technische Prüfung und Wiederaufnahmen','',
        f"Geprüft wurden {d['audit']['controls_checked']} bestandene Kontrollpaare, {d['audit']['evaluations_checked']} offizielle Endbewertungen und {d['audit']['model_stages_checked']} Modellstufen.",
        'Die Ergebniswerte stimmen mit den offiziellen Bewertungen überein. Alle Endversuche haben Status completed, alle geprüften Modellstufen Exitcode 0 und keine Modelltimeouts oder unerwarteten Webtools.',
        '„Gelöst“ bezieht sich auf die offiziellen Pflicht-Testmengen; es bedeutet nicht zwangsläufig, dass jeder zusätzliche Repository-Test besteht.',
        'Aufgabenidentitäten, angeforderte Modelle/Reasoning-Stufen, Authentifizierung und verwendete Image-IDs wurden geprüft.',
        'Shared-Runner, native Ultra-Implementierung, Runtime-Profil und Codex-Binärdateien stimmen über die Batches überein.',
        'Der Einstiegsrunner hat zwei eingefrorene Versionen: Für batch-01 wurden Routing auf Aufgaben 1–100 und validierte Kontrollspender ergänzt.',
        'Die ausführenden Funktionen models/resume/validate/capsule und die native Modellintegration sind identisch; Quellversionen bleiben dokumentiert.',
        f"Rollout-Prüfung: {d['audit']['rollouts_checked']} Dateien; beobachtete Modelle: {d['observed_rollout_models']}; beobachtetes Reasoning: {d['observed_rollout_efforts']}.",
        f"Bei {d['audit'].get('thread_counters_start_at_first_call',0)} Rollouts beginnt der kumulative Zähler beim ersten eigenen Modellaufruf.",
        f"Es gibt {len(d['interruption_archives'])} Wiederaufnahme-Archive und {len(d['unique_archived_errors'])} eindeutige archivierte Fehlermeldungen nach Deduplizierung.",
        'Die Unterbrechungsarchive werden nicht als zusätzliche unabhängige Versuche gezählt. Fertige Ergebnisse bleiben auch bei Nichtlösung erhalten;',
        'es erfolgt keine Best-of-Auswahl nach Benchmark-Score. Teilweise gelöschte Docker-Images verhindern eine sofortige exakte Wiederholung aller alten Umgebungen.','',
        '## Interpretation','',
        'Unter den untersuchten Bedingungen liefert Ultra trotz deutlich höherem protokolliertem Aufwand keinen beobachteten Lösungsvorteil gegenüber Medium.',
        'Das Ergebnis spricht für Medium als sparsamere Referenz in dieser Untersuchung. Es beweist weder allgemeine Wirkungslosigkeit von Multiagentensystemen',
        'noch einen generellen Nachteil von Ultra. Der kombinierte Eingriff aus höherem Reasoning, Delegation und zusätzlichem Prompt lässt die Einzelursachen offen.',
        'Es gibt einen Endversuch je Aufgabe/Variante. Aufgaben desselben Repositories können abhängig sein; der McNemar-Test berücksichtigt keine Repository-Cluster.',
        'Modellwahl und Setup entstanden nach früheren Experimenten mit überlappenden Aufgaben. Dies ist eine explorative Auswertung und kein unabhängiger Holdout-Test.','',
        '## Reproduktion und Daten','',
        'Aus dem Laborordner: `.venv/bin/python compare_sol_ultra_all.py`.',
        '[Maschinenlesbarer Bericht und Prüfsummen](summary.json) · [Alle 300 Aufgaben](tasks.csv) · [Beobachtete Unteragenten](agents.csv)','']
    for c in d['cohorts']:lines.append(f"- [{c['batch']}](../../{c['source']}/manifest.json)")
    (out/'summary.md').write_text('\n'.join(lines)+'\n')
    return out


if __name__=='__main__':
    d=build();out=write(d)
    print(out/'summary.md')
    print(json.dumps({'summaries':d['summaries'],'paired_test':d['paired_test'],'audit':d['audit'],
                     'models':d['observed_rollout_models'],'efforts':d['observed_rollout_efforts']},indent=2))
