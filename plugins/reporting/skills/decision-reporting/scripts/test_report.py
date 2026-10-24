import copy
import json
from pathlib import Path
import unittest
from report import generate

class ReportTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((Path(__file__).parents[1]/'references/synthetic-input.json').read_text())

    def test_linked_notification_not_second_case(self):
        result = generate(self.data)
        self.assertEqual(result['feedback']['total'], 1)
        self.assertEqual(result['feedback']['exclusions']['linked_notifications'], 1)
        self.assertEqual(result['skill_revision'], 'reporting/0.1.1')

    def test_legacy_missing_context_and_identity_stay_unknown(self):
        feedback = generate(self.data)['feedback']
        self.assertEqual(feedback['by_usage_context'], {'unknown': 1})
        self.assertEqual(feedback['by_edition'], {'unknown': 1})
        self.assertEqual(feedback['by_build'], {'unknown': 1})
        self.assertEqual(feedback['actual_use'], {'free_used': 0, 'paid_used': 0})
        self.assertEqual(feedback['actual_use_by_product'], {})
        self.assertEqual(feedback['actual_use_by_edition'], {})

    def test_free_and_paid_reported_use_are_separate(self):
        self.data['config']['editions'] = ['three-room', 'recorded-echoes']
        self.data['config']['builds'] = ['web-1', 'ios-1_0-3']
        records = self.data['sources']['tally']['records']
        records[0].update(usage_context='free_used', edition='three-room', build='web-1')
        records.append(dict(records[0], id='synthetic-paid', usage_context='paid_used',
                            edition='recorded-echoes', build='ios-1_0-3'))
        records.append(dict(records[0], id='synthetic-before-use', usage_context='pre_use',
                            edition=None, build=None))
        feedback = generate(self.data)['feedback']
        self.assertEqual(feedback['total'], 3)
        self.assertEqual(feedback['by_usage_context'],
                         {'free_used': 1, 'paid_used': 1, 'pre_use': 1})
        self.assertEqual(feedback['actual_use'], {'free_used': 1, 'paid_used': 1})
        self.assertEqual(feedback['actual_use_by_product'],
                         {'puzzle': {'free_used': 1, 'paid_used': 1}})
        self.assertEqual(feedback['actual_use_by_edition'],
                         {'recorded-echoes': {'free_used': 0, 'paid_used': 1},
                          'three-room': {'free_used': 1, 'paid_used': 0}})
        self.assertEqual(feedback['actual_use_by_build'],
                         {'ios-1_0-3': {'free_used': 0, 'paid_used': 1},
                          'web-1': {'free_used': 1, 'paid_used': 0}})
        self.assertEqual(feedback['by_edition'],
                         {'recorded-echoes': 1, 'three-room': 1, 'unknown': 1})
        self.assertEqual(feedback['by_build'], {'ios-1_0-3': 1, 'unknown': 1, 'web-1': 1})
        self.assertIn('not purchase validation', ' '.join(generate(self.data)['limitations']))

    def test_context_qa_and_owner_test_are_excluded(self):
        records = self.data['sources']['tally']['records']
        records[0]['usage_context'] = 'qa'
        records.append(dict(records[0], id='synthetic-owner', usage_context='owner_test'))
        records.append(dict(records[0], id='synthetic-explicit-qa',
                            usage_context='paid_used', is_qa=True))
        feedback = generate(self.data)['feedback']
        self.assertEqual(feedback['total'], 0)
        self.assertEqual(feedback['exclusions']['qa_records'], 2)
        self.assertEqual(feedback['exclusions']['owner_test_records'], 1)
        self.assertEqual(feedback['actual_use'], {'free_used': 0, 'paid_used': 0})

    def test_invalid_context_invalidates_source(self):
        self.data['sources']['tally']['records'][0]['usage_context'] = 'purchased'
        result = generate(self.data)
        self.assertEqual(result['sources']['tally']['status'], 'invalid')
        self.assertIsNone(result['feedback']['total'])

    def test_unapproved_edition_and_build_do_not_leak(self):
        row = self.data['sources']['tally']['records'][0]
        row.update(usage_context='free_used', edition='private@example.com',
                   build='customer-id-123')
        result = generate(self.data)
        self.assertEqual(result['feedback']['by_edition'], {'unclassified': 1})
        self.assertEqual(result['feedback']['by_build'], {'unclassified': 1})
        self.assertNotIn('private@example.com', json.dumps(result))
        self.assertNotIn('customer-id-123', json.dumps(result))

    def test_duplicate_and_qa_exclusion(self):
        records = self.data['sources']['tally']['records']
        records.append(copy.deepcopy(records[0]))
        records.append(dict(records[0], id='qa', is_qa=True))
        result = generate(self.data)['feedback']
        self.assertEqual(result['total'], 1)
        self.assertEqual(result['exclusions']['duplicate_records'], 1)
        self.assertEqual(result['exclusions']['qa_records'], 1)

    def test_missing_is_not_zero_and_unmatched_mail_not_feedback(self):
        del self.data['sources']['tally']
        result = generate(self.data)
        self.assertIsNone(result['feedback']['total'])
        self.assertEqual(result['feedback']['observed_records'], 0)
        self.assertEqual(result['feedback']['exclusions']['unmatched_notifications'], 1)
        self.assertEqual(result['status'], 'incomplete')

    def test_conflicting_duplicates_invalidate_source(self):
        records=self.data["sources"]["tally"]["records"]
        records.append(dict(records[0],is_qa=True))
        result=generate(self.data)
        self.assertEqual(result["sources"]["tally"]["status"],"invalid")
        self.assertIsNone(result["feedback"]["total"])

    def test_qa_notification_and_duplicates_never_enter_counts(self):
        records=self.data["sources"]["tally"]["records"]
        records[0]["is_qa"]=True
        records.append(copy.deepcopy(records[0]))
        result=generate(self.data)["feedback"]
        self.assertEqual(result["total"],0)
        self.assertEqual(result["exclusions"],{"qa_records":1,"duplicate_records":1,"linked_notifications":1})

    def test_all_sources_unavailable_keeps_observed_counts_null(self):
        self.data["sources"]={}
        result=generate(self.data)
        self.assertIsNone(result["feedback"]["total"])
        self.assertIsNone(result["feedback"]["observed_records"])
        self.assertIsNone(result["feedback"]["by_product"])
        self.assertIsNone(result["feedback"]["actual_use"])
        self.assertIsNone(result["feedback"]["actual_use_by_edition"])
        self.assertIsNone(result["analytics"])

    def test_fetch_before_window_end_cannot_attest_full_coverage(self):
        self.data["sources"]["tally"]["fetched_at"]="2026-01-11T23:00:00Z"
        result=generate(self.data)
        self.assertEqual(result["sources"]["tally"]["status"],"partial")
        self.assertIsNone(result["feedback"]["total"])

    def test_empty_complete_is_zero(self):
        for name in ('tally','gmail'):
            self.data['sources'][name]['records'] = []
        self.assertEqual(generate(self.data)['feedback']['total'], 0)

    def test_stale_and_partial(self):
        self.data['sources']['tally']['fetched_at']='2025-01-01T00:00:00Z'
        self.data['sources']['analytics']['coverage']['start']='2026-01-06T00:00:00Z'
        result=generate(self.data)
        self.assertEqual(result['sources']['tally']['status'], 'stale')
        self.assertEqual(result['sources']['analytics']['status'], 'partial')
        self.assertIsNone(result['analytics'])

    def test_sensitive_text_and_ids_not_emitted(self):
        row=self.data['sources']['tally']['records'][0]
        row.update(id='SECRET-ID', body='private@example.com private text', product='private@example.com', theme='private text')
        result=json.dumps(generate(self.data))
        for secret in ('SECRET-ID','private@example.com','private text','synthetic-mail-1'):
            self.assertNotIn(secret,result)
        self.assertIn('unclassified',result)

    def test_invalid_record_invalidates_source(self):
        self.data['sources']['tally']['records'].append({'id':'broken'})
        result=generate(self.data)
        self.assertEqual(result['sources']['tally']['status'], 'invalid')
        self.assertIsNone(result['feedback']['total'])

    def test_older_open_case_has_age_but_not_new_count(self):
        self.data['sources']['tally']['records'][0]['created_at']='2026-01-01T00:00:00Z'
        result=generate(self.data)['feedback']
        self.assertEqual(result['total'],0)
        self.assertEqual(result['oldest_open_days'],11)

    def test_allowlisted_dimensions_exclude_raw_urls(self):
        self.data["config"]["pages"]=["home"]
        self.data["sources"]["analytics"]["dimensions"]={"pages":{"home":5,"https://example.com/?email=secret":2},"devices":{}}
        result=generate(self.data)
        self.assertEqual(result["analytics"]["dimensions"]["pages"],{"home":5,"unclassified":2})
        self.assertEqual(result["analytics"]["dimensions"]["devices"],{})
        self.assertIsNone(result["analytics"]["dimensions"]["referrers"])
        self.assertNotIn("email=secret",json.dumps(result))

    def test_boundaries_and_numeric_validation(self):
        self.data['sources']['tally']['records'][0]['created_at']=self.data['window']['end']
        self.data['sources']['analytics']['metrics']['visits']=-1
        result=generate(self.data)
        self.assertEqual(result['feedback']['total'],0)
        self.assertEqual(result['sources']['analytics']['status'],'invalid')

    def test_repeated_theme_is_prompt_not_demand_claim(self):
        records=self.data['sources']['tally']['records']
        records.append(dict(records[0],id='another'))
        result=generate(self.data)
        self.assertEqual(result['findings'][0]['code'],'repeated_theme')
        self.assertEqual(result['findings'][0]['records'],2)

if __name__ == '__main__':
    unittest.main()
