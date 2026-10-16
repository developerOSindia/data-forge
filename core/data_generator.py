"""
Core business logic for Data Forge synthetic dataset generator.
Zero Streamlit or UI dependencies.
"""

import random
import csv
import io
import json
from typing import List, Dict, Any, Optional


def generate_synthetic_records(count: int, seed: int = 42) -> List[Dict[str, Any]]:
    """Generates synthetic tabular developer records deterministically."""
    if count <= 0:
        return []

    random.seed(seed)
    first_names = ["Aarav", "Priya", "Rohan", "Ananya", "Vikram", "Neha", "Aditya", "Ishaan", "Kavya", "Rahul"]
    domains = ["developeros.in", "example.com", "techcorp.io", "cloudscale.dev"]
    roles = ["Frontend Engineer", "Backend Engineer", "Platform Architect", "DevOps Specialist", "Security Analyst"]

    records = []
    for idx in range(1, count + 1):
        fn = random.choice(first_names)
        dom = random.choice(domains)
        email = f"{fn.lower()}{idx}@{dom}"
        role = random.choice(roles)
        records.append({
            "id": idx,
            "name": f"{fn} Dev",
            "email": email,
            "role": role,
            "is_active": random.random() > 0.15,
        })

    return records


def export_records_to_csv(records: List[Dict[str, Any]]) -> str:
    """Exports records into RFC 4180 standard CSV format."""
    if not records:
        return ""
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=list(records[0].keys()))
    writer.writeheader()
    writer.writerows(records)
    return output.getvalue()


def export_records_to_json(records: List[Dict[str, Any]], indent: int = 2) -> str:
    """Exports records into formatted JSON string."""
    return json.dumps(records, indent=indent)


def filter_records(
    records: List[Dict[str, Any]],
    role: Optional[str] = None,
    active_only: bool = False,
) -> List[Dict[str, Any]]:
    """Filters records by role and active status."""
    filtered = records
    if role:
        filtered = [r for r in filtered if r.get("role") == role]
    if active_only:
        filtered = [r for r in filtered if r.get("is_active") is True]
    return filtered
