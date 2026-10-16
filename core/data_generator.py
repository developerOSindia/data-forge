"""
Core business logic for Data Forge synthetic dataset generator.
Zero Streamlit or UI dependencies.
"""

import random
from typing import List, Dict, Any


def generate_synthetic_records(count: int, seed: int = 42) -> List[Dict[str, Any]]:
    """Generates synthetic tabular developer records deterministically."""
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
