import json
from datetime import datetime
from pathlib import Path

EXPORT_DIR = Path("outputs")
EXPORT_DIR.mkdir(exist_ok=True)


def export_answer(question, answer):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    data = {
        "timestamp": timestamp,
        "question": question,
        "answer": answer
    }

    file_path = EXPORT_DIR / f"answer_{timestamp}.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    return str(file_path)
