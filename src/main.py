from .src_nlp.question_parser import parse_question
from .src_rules.rule_engine import load_data, apply_filters
from .src_engine.answer_formatter import format_answer
from .src_engine.history_manager import save_history, load_history
from .src_engine.export_manager import export_answer


def main():
    print("🔹 InsightForge – Offline Enterprise QA System 🔹")
    print("Type your question or type 'exit' to quit.")
    print("Type 'history' to view previous questions.\n")

    # Load enterprise data once
    data = load_data()

    while True:
        question = input("❓ Ask: ").strip()

        # Exit condition
        if question.lower() in ["exit", "quit"]:
            print("👋 Exiting InsightForge. Goodbye!")
            break

        # Show history
        if question.lower() == "history":
            history = load_history()
            if not history:
                print("📭 No history available.\n")
                continue

            print(f"\n📜 Showing last {len(history)} questions:\n")
            for item in history:
                print(f"🕒 {item['timestamp']}")
                print(f"❓ {item['question']}")
                print(f"✅ {item['answer']}")
                print("-" * 50)
            continue

        # Parse the question
        parsed = parse_question(question)

        intent = parsed.get("intent")
        filters = parsed.get("filters")
        logic = parsed.get("logic", "AND")
        limit = parsed.get("limit", 5)

        # Apply rules
        results = apply_filters(data, filters, logic)

        # Format answer
        answer = format_answer(intent, results, filters)


        # Display answer
        print("\n✅ Answer:")
        print(answer)
        print("-" * 50)

        # Save history
        save_history(question, answer, intent, filters)


        # Export answer
        export_path = export_answer(question, answer)
        print(f"📁 Answer exported to: {export_path}\n")


if __name__ == "__main__":
    main()
