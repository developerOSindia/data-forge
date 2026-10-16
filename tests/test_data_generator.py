"""
Unit tests for data-forge business logic.
"""

import sys
import unittest
from pathlib import Path

APP_ROOT = Path(__file__).resolve().parent.parent
if str(APP_ROOT) not in sys.path:
    sys.path.insert(0, str(APP_ROOT))

from core.data_generator import generate_synthetic_records


class TestDataGenerator(unittest.TestCase):
    def test_record_generation_count(self):
        records = generate_synthetic_records(10, seed=123)
        self.assertEqual(len(records), 10)
        self.assertEqual(records[0]["id"], 1)
        self.assertIn("@", records[0]["email"])

    def test_determinism_with_seed(self):
        run1 = generate_synthetic_records(5, seed=99)
        run2 = generate_synthetic_records(5, seed=99)
        self.assertEqual(run1, run2)


if __name__ == "__main__":
    unittest.main()
