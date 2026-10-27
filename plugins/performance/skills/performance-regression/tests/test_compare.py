import copy
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('compare', Path(__file__).resolve().parents[1]/'scripts/compare.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def report(values=None):
    return {'schema_version':1,'source_revision':'synthetic-a','source_dirty':False,
            'toolkit_revision':'synthetic-toolkit','scenario':'synthetic-action','captured_at':'2026-10-24T12:00:00Z',
            'fixture':{'records':100},'environment':dict.fromkeys(m.ENV,'synthetic'),
            'conditions':dict(dict.fromkeys(m.CONDITIONS,'synthetic'),samples=5),
            'metrics':{'settle':{'unit':'ms','direction':'lower','samples':values or [10,11,12,11,10]}}}


class Comparisons(unittest.TestCase):
    def test_slowdown_and_recovery(self):
        baseline=report()
        self.assertEqual(m.compare(baseline,report([80,81,82,83,80]))['metrics']['settle']['signal'],'slower_sample_range')
        self.assertEqual(m.compare(baseline,report())['metrics']['settle']['signal'],'overlapping_or_faster')

    def test_environment_and_fixture_changes(self):
        for key in ('environment','fixture','conditions'):
            value=report(); value[key]['changed']=True
            self.assertEqual(m.compare(report(),value)['status'],'incomparable')

    def test_missing_baseline(self):
        self.assertEqual(m.compare(None,report())['status'],'incomplete')

    def test_invalid_samples(self):
        for samples in ([1], [1,2,3,4,float('nan')], [1,2,3,4,-1], [1,2,3,4,True], [1,2,3,4,float('inf')]):
            self.assertEqual(m.compare(report(),report(samples))['status'],'incomplete')

    def test_missing_metric(self):
        value=report(); value['metrics']['other']=copy.deepcopy(value['metrics']['settle'])
        self.assertEqual(m.compare(report(),value)['status'],'incomplete')

    def test_source_changes_allowed_toolkit_changes_not(self):
        value=report();value['source_revision']='synthetic-b'
        self.assertEqual(m.compare(report(),value)['status'],'comparable')
        value['toolkit_revision']='changed'
        self.assertEqual(m.compare(report(),value)['status'],'incomparable')

    def test_zero_and_variability(self):
        row=m.compare(report([0]*5),report([1]*5))['metrics']['settle']
        self.assertIsNone(row['median_change_percent'])
        self.assertEqual(row['candidate']['stdev'],0)

    def test_dirty_or_unidentified(self):
        for field,value in [('source_dirty',True),('source_revision','')]:
            candidate=report();candidate[field]=value
            self.assertEqual(m.compare(report(),candidate)['status'],'incomplete')

    def test_metric_units(self):
        value=report();value['metrics']['settle']['unit']='bytes'
        self.assertEqual(m.compare(report(),value)['status'],'incomparable')

    def test_overlapping_noise_is_not_separated(self):
        row=m.compare(report([1,2,3,4,100]),report([2,3,4,5,99]))['metrics']['settle']
        self.assertEqual(row['signal'],'overlapping_or_faster')
        self.assertGreater(row['median_delta'],0)


if __name__=='__main__': unittest.main()
