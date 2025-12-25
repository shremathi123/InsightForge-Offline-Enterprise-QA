def calculate_confidence(count):
    if count == 0:
        return "None ❌"
    elif count <= 3:
        return "Low 🔴"
    elif count <= 8:
        return "Medium 🟡"
    else:
        return "High 🟢"


def format_answer(intent, results, filters):
    count = len(results)
    confidence = calculate_confidence(count)

    if count == 0:
        return (
            "❌ No companies match your criteria.\n"
            f"Confidence: {confidence}"
        )

    company_names = [c.get("name") for c in results[:5]]

    answer = (
        f"✅ {count} companies match your criteria.\n"
        f"Confidence: {confidence}\n"
        f"Some of them are: {', '.join(company_names)}"
    )

    return answer
