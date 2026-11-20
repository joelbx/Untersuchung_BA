"""Temporary artifact fixtures; no real project changes or model calls."""
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

MODULE = Path(__file__).resolve().parents[1] / 'scripts/check_workflow.py'
spec = importlib.util.spec_from_file_location('checker', MODULE)
checker = importlib.util.module_from_spec(spec);spec.loader.exec_module(checker)


class Gates(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.state = {'schema_version': 1, 'feature_id': 'F1', 'project_roots': ['repo'],
                      'status': 'approved', 'spec_revision': 'S1', 'spec_approval': 'S',
                      'artifacts': {'specification': 'spec/S1.md'}, 'tickets': []}
        self.receipts = []
        for path in ('spec/S1.md','tickets/T1.md','plans/P1.md','review/R1.md','acceptance/A1.md'):
            p=self.root/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(path)
        self.approval('S','specification','F1','S1',['spec/S1.md'])

    def approval(self, identifier, kind, subject, revision, paths):
        self.receipts.append({'id':identifier,'kind':kind,'subject':subject,'revision':revision,
            'actor':'human','decision':'approved','evidence':{'source':'fixture user message','quote':'Approved the presented revision'},
            'artifacts':{p:hashlib.sha256((self.root/p).read_bytes()).hexdigest() for p in paths}})

    def ticket(self, status='implementing'):
        t={'id':'T1','status':status,'spec_revision':'S1','spec_approval':'S','plan_revision':'P1',
           'plan_approval':'P','acceptance_revision':'A1','acceptance_approval':None,
           'artifacts':{'specification':'spec/S1.md','ticket':'tickets/T1.md','plan':'plans/P1.md','review':'review/R1.md','acceptance':'acceptance/A1.md'}}
        self.state['tickets']=[t]
        return t

    def check(self):
        (self.root/'workflow.json').write_text(json.dumps(self.state))
        (self.root/'approvals.jsonl').write_text('\n'.join(json.dumps(x) for x in self.receipts))
        return checker.validate(self.root)

    def test_plan_without_approval_cannot_implement(self):
        self.ticket()
        self.assertTrue(any('implementation_plan' in e for e in self.check()))

    def test_valid_plan_can_implement_and_changed_artifact_invalidates_it(self):
        self.ticket();self.approval('P','implementation_plan','T1','P1',['tickets/T1.md','plans/P1.md'])
        self.assertEqual(self.check(),[])
        (self.root/'plans/P1.md').write_text('changed scope')
        self.assertTrue(any('stale' in e for e in self.check()))

    def test_done_needs_actual_scoped_human_acceptance_record(self):
        t=self.ticket('done');self.state['status']='done'
        self.approval('P','implementation_plan','T1','P1',['tickets/T1.md','plans/P1.md'])
        self.assertTrue(any('acceptance approval' in e for e in self.check()))
        self.approval('A','acceptance','T1','A1',['review/R1.md','acceptance/A1.md']);t['acceptance_approval']='A'
        self.assertEqual(self.check(),[])
        self.receipts[-1]['actor']='agent'
        self.assertTrue(any('human evidence' in e for e in self.check()))

    def test_no_approval_by_an_empty_yes_without_source(self):
        self.receipts[0]['evidence']={}
        self.assertTrue(any('human evidence' in e for e in self.check()))

    def test_approval_paths_cannot_escape_feature_directory(self):
        self.receipts[0]['artifacts']['../outside.md']='0'*64
        self.assertTrue(any('escapes' in e for e in self.check()))

    def test_dependency_cycle_and_unaccepted_blocker_are_reported(self):
        t=self.ticket('planned');t['plan_approval']=None;t['depends_on']=['T1']
        self.assertTrue(any('dependencies' in e for e in self.check()))

    def test_older_approved_spec_can_remain_valid_for_unaffected_ticket(self):
        self.ticket();self.approval('P','implementation_plan','T1','P1',['tickets/T1.md','plans/P1.md'])
        (self.root/'spec/S2.md').write_text('new scope for another ticket')
        self.approval('S2','specification','F1','S2',['spec/S2.md'])
        self.state.update(spec_revision='S2',spec_approval='S2',artifacts={'specification':'spec/S2.md'})
        self.assertEqual(self.check(),[])

    def test_wrong_revision_does_not_authorize_implementation(self):
        self.ticket();self.approval('P','implementation_plan','T1','P0',['tickets/T1.md','plans/P1.md'])
        self.assertTrue(any('revision' in e for e in self.check()))

    def test_accepted_review_cannot_change_silently(self):
        t=self.ticket('done')
        self.approval('P','implementation_plan','T1','P1',['tickets/T1.md','plans/P1.md'])
        self.approval('A','acceptance','T1','A1',['review/R1.md','acceptance/A1.md'])
        t['acceptance_approval']='A'
        self.assertEqual(self.check(),[])
        (self.root/'review/R1.md').write_text('different code reviewed')
        self.assertTrue(any('stale' in e for e in self.check()))

    def test_checker_is_read_only_and_malformed_state_has_clear_error(self):
        self.check()
        before={str(p.relative_to(self.root)):p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        checker.validate(self.root)
        after={str(p.relative_to(self.root)):p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual(before,after)
        self.state['status']=[]
        self.assertTrue(any('Invalid feature status' in e for e in self.check()))

    def completed_ticket_with_aid(self):
        t = self.ticket('done')
        self.approval('P', 'implementation_plan', 'T1', 'P1', ['tickets/T1.md', 'plans/P1.md'])
        for path in ('evidence/removal.md', 'evidence/final-verification.md'):
            f = self.root / path
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_text('Fixture evidence for the final code revision')
        aid = {'id': 'AID1', 'status': 'removed',
               'human_check': {'source': 'fixture human message', 'quote': 'Function tested successfully'},
               'removal_evidence': 'evidence/removal.md',
               'verification_evidence': 'evidence/final-verification.md'}
        t['temporary_test_aids'] = [aid]
        self.approval('A', 'acceptance', 'T1', 'A1',
                      ['review/R1.md', 'acceptance/A1.md', 'evidence/removal.md',
                       'evidence/final-verification.md'])
        t['acceptance_approval'] = 'A'
        return aid

    def test_human_acceptance_cannot_finish_ticket_with_present_test_aid(self):
        aid = self.completed_ticket_with_aid()
        aid['status'] = 'present'
        self.assertTrue(any('not removed' in e for e in self.check()))

    def test_test_aid_needs_actual_human_check_before_done(self):
        aid = self.completed_ticket_with_aid()
        aid['human_check'] = {'source': None, 'quote': None}
        self.assertTrue(any('human functional check' in e for e in self.check()))

    def test_completed_cleanup_with_fingerprinted_evidence_can_finish(self):
        self.completed_ticket_with_aid()
        self.assertEqual(self.check(), [])
        (self.root / 'evidence/removal.md').write_text('Modified after acceptance')
        self.assertTrue(any('stale' in e for e in self.check()))

    def test_missing_or_uncovered_cleanup_evidence_blocks_done(self):
        aid = self.completed_ticket_with_aid()
        self.receipts[-1]['artifacts'].pop('evidence/final-verification.md')
        self.assertTrue(any('does not cover' in e for e in self.check()))
        aid['removal_evidence'] = '../outside.md'
        self.assertTrue(any('escapes' in e for e in self.check()))

    def test_malformed_test_aid_inventory_has_clear_error(self):
        self.completed_ticket_with_aid()
        self.state['tickets'][0]['temporary_test_aids'] = {'status': 'removed'}
        self.assertTrue(any('list of objects' in e for e in self.check()))


if __name__ == '__main__':unittest.main()
