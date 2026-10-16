"""
Unit tests for Data Forge synthetic generator and export routines.
"""

import sys
import unittest
from pathlib import Path

APP_ROOT = Path(__file__).resolve().parent.parent
if str(APP_ROOT) not in sys.path:
    sys.path.insert(0, str(APP_ROOT))

from core.data_generator import (
    generate_synthetic_records,
    export_records_to_csv,
    export_records_to_json,
    filter_records,
)


class TestDataGenerator(unittest.TestCase):
    def test_record_count_and_keys(self):
        records = generate_synthetic_records(10, seed=123)
        self.assertEqual(len(records), 10)
        expected_keys = {"id", "name", "email", "role", "is_active"}
        for rec in records:
            self.assertEqual(set(rec.keys()), expected_keys)
            self.assertIn("@", rec["email"])

    def test_zero_records(self):
        records = generate_synthetic_records(0)
        self.assertEqual(records, [])
        self.assertEqual(export_records_to_csv(records), "")

    def test_deterministic_seed(self):
        run1 = generate_synthetic_records(5, seed=42)
        run2 = generate_synthetic_records(5, seed=42)
        self.assertEqual(run1, run2)

    def test_export_to_csv(self):
        records = generate_synthetic_records(3, seed=99)
        csv_str = export_records_to_csv(records)
        self.assertIn("id,name,email,role,is_active", csv_str)
        self.assertEqual(len(csv_str.strip().splitlines()), 4)

    def test_export_to_json(self):
        records = generate_synthetic_records(2, seed=10)
        json_str = export_records_to_json(records)
        self.assertIn('"id": 1', json_str)
        self.assertIn('"email"', json_str)

    def test_filter_records(self):
        records = generate_synthetic_records(50, seed=77)
        frontend_devs = filter_records(records, role="Frontend Engineer")
        for dev in frontend_devs:
            self.assertEqual(dev["role"], "Frontend Engineer")

        active_devs = filter_records(records, active_only=True)
        for dev in active_devs:
            self.assertTrue(dev["is_active"])


if __name__ == "__main__":
    unittest.main()
