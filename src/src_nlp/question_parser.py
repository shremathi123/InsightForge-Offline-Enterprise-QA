def parse_question(question):
    question = question.lower()

    # default values
    intent = "unknown"
    filters = {}
    logic = "AND"
    limit = None

    # ---- intent detection ----
    if "company" in question or "companies" in question:
        intent = "filter_companies"
    if "how many" in question:
        intent = "count_companies"

    # ---- logic detection ----
    if " or " in question:
        logic = "OR"
    elif " and " in question:
        logic = "AND"

    # ---- sector detection ----
    if "technology" in question or "tech" in question:
        filters["sector"] = "Technology"

    # ---- involvement conditions ----
    if "no alcohol" in question or "without alcohol" in question:
        filters["involvement.Alcoholic Beverages"] = "No"

    if "no gambling" in question or "without gambling" in question:
        filters["involvement.Gambling"] = "No"

    if "no tobacco" in question or "without tobacco" in question:
        filters["involvement.Tobacco Products"] = "No"

    if "no weapons" in question:
        filters["involvement.Controversial Weapons"] = "No"

    # ---- limit detection (top N) ----
    if "top" in question:
        for word in question.split():
            if word.isdigit():
                limit = int(word)

    return {
        "intent": intent,
        "filters": filters,
        "logic": logic,
        "limit": limit
    }
