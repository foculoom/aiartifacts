import unittest
from zoneinfo import ZoneInfoNotFoundError
from weekly_window import bounds


class WeeklyWindowTests(unittest.TestCase):
    def test_fall_daylight_saving_transition(self):
        window = bounds('2026-11-02', 'America/Los_Angeles')
        self.assertEqual((window['start'], window['end'], window['elapsed_hours']),
                         ('2026-10-26T07:00:00Z', '2026-11-02T08:00:00Z', 169))

    def test_ordinary_week(self):
        window = bounds('2026-11-09', 'America/Los_Angeles')
        self.assertEqual((window['start'], window['end'], window['elapsed_hours']),
                         ('2026-11-02T08:00:00Z', '2026-11-09T08:00:00Z', 168))

    def test_spring_daylight_saving_transition(self):
        window = bounds('2026-03-09', 'America/Los_Angeles')
        self.assertEqual((window['start'], window['end'], window['elapsed_hours']),
                         ('2026-03-02T08:00:00Z', '2026-03-09T07:00:00Z', 167))

    def test_first_activation_truncates_first_week(self):
        window = bounds('2026-10-26', 'America/Los_Angeles', '2026-10-24T04:17:31Z')
        self.assertEqual((window['start'], window['end']),
                         ('2026-10-24T04:17:31Z', '2026-10-26T07:00:00Z'))

    def test_first_activation_preserves_fractional_seconds(self):
        window = bounds('2026-10-26', 'America/Los_Angeles', '2026-10-24T04:17:31.900Z')
        self.assertEqual(window['start'], '2026-10-24T04:17:31.900000Z')

    def test_invalid_activation_and_timezone(self):
        with self.assertRaises(ValueError):
            bounds('2026-11-09', 'America/Los_Angeles', '2026-11-02T08:00:00')
        with self.assertRaises(ValueError):
            bounds('2026-11-09', 'America/Los_Angeles', '2026-11-09T08:00:00Z')
        with self.assertRaises(ZoneInfoNotFoundError):
            bounds('2026-11-09', 'Not/AZone')


if __name__ == '__main__':
    unittest.main()
