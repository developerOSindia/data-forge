"""
Data Forge - DeveloperOS Flagship Application
"""

import streamlit as st
import json
from core.data_generator import generate_synthetic_records
from ui.components import render_forge_header, render_forge_footer, render_main_promotional_banner

st.set_page_config(
    page_title="Data Forge — DeveloperOS Flagship",
    page_icon="🔨",
    layout="wide"
)


def main():
    render_forge_header()

    st.subheader("Generate Synthetic Developer Datasets")
    col_c, col_s = st.columns([1, 1])
    with col_c:
        record_count = st.slider("Record Count", min_value=5, max_value=250, value=25)
    with col_s:
        random_seed = st.number_input("Deterministic Random Seed", value=42)

    format_choice = st.radio("Export Format", ["JSON Array", "SQL INSERT Statements", "CSV Format"], horizontal=True)

    if st.button("Forge Dataset", type="primary"):
        records = generate_synthetic_records(count=record_count, seed=int(random_seed))

        if format_choice == "JSON Array":
            st.code(json.dumps(records, indent=2), language="json")
        elif format_choice == "SQL INSERT Statements":
            sql_rows = []
            for r in records:
                sql_rows.append(f"INSERT INTO users (id, name, email, role, is_active) VALUES ({r['id']}, '{r['name']}', '{r['email']}', '{r['role']}', {r['is_active']});")
            st.code("\n".join(sql_rows), language="sql")
        else:
            csv_lines = ["id,name,email,role,is_active"]
            for r in records:
                csv_lines.append(f"{r['id']},{r['name']},{r['email']},{r['role']},{r['is_active']}")
            st.code("\n".join(csv_lines), language="text")

    render_main_promotional_banner(tool_name="Data Forge")
    render_forge_footer()


if __name__ == "__main__":
    main()
