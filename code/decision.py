def decide(results, risk, issue):
    if not results or len(results) == 0:
        return "escalated", 0.0

    score = results[0]["score"]
    company = results[0]["meta"]["company"]
    t = issue.lower()

    if risk == "high":
        return "escalated", score

    if company == "visa" and any(x in t for x in [
        "refund", "wrong product",
        "charged", "dispute", "fraud", "unauthorized"
    ]):
        return "escalated", score

    if score < 0.40:
        return "escalated", score

    return "replied", score
