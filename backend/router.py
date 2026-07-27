def detect_intent(question: str):

    q = question.lower()

    if any(word in q for word in ["revenue", "collection", "receivable", "billed"]):
        return "revenue"

    if any(word in q for word in ["pipeline", "deal"]):
        return "pipeline"

    if any(word in q for word in ["sector", "industry"]):
        return "sector"

    if any(word in q for word in ["project", "work order", "execution"]):
        return "workorders"

    if any(word in q for word in ["leadership", "summary", "report"]):
        return "leadership"

    return "dashboard"