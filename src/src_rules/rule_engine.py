import json
from pathlib import Path


from pathlib import Path
import json

def load_data():
    # Get project root (offline_qa_project)
    BASE_DIR = Path(__file__).resolve().parents[2]

    data_path = BASE_DIR / "data" / "data_processed" / "enterprise_data.json"

    with open(data_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data



def apply_filters(data, filters, logic="AND"):
    results = []

    for record in data:
        matches = []

        for key, value in filters.items():
            record_value = record.get(key)

            if record_value is None:
                matches.append(False)
                continue

            if isinstance(record_value, str):
                record_value = record_value.strip()

            matches.append(record_value == value)

        if logic == "AND" and all(matches):
            results.append(record)

        elif logic == "OR" and any(matches):
            results.append(record)

    return results
