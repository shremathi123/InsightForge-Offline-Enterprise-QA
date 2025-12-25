import json
from datetime import datetime
from pathlib import Path

HISTORY_PATH = Path("outputs/question_history.json")

def save_history(question, answer, intent, filters):
    record = {
        "timestamp": datetime.now().isoformat(),
        "question": question,
        "intent": intent,
        "filters": filters,
        "answer": answer
    }

    # Load existing history
    if HISTORY_PATH.exists():
        with open(HISTORY_PATH, "r", encoding="utf-8") as f:
            history = json.load(f)
    else:
        history = []

    history.append(record)

    # Save back
    with open(HISTORY_PATH, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4)

def load_history():
    if not HISTORY_PATH.exists():
        return []

    with open(HISTORY_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
