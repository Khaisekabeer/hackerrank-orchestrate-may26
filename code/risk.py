def risk_level(issue):
    t = issue.lower()

    high_risk = [
        "fraud", "unauthorized", "stolen",
        "identity theft", "without permission",
        "not me", "someone used", "impersonation",
        "restore my access", "removed my seat",
        "not the owner", "not an admin", "admin removed",
        "delete my data", "personal information",
        "security vulnerability", "bug bounty",
        "rules internal", "documents retrieved",
        "logic exact", "logic you use"
    ]

    payment_risk = [
        "refund", "charged", "billing", "dispute",
        "chargeback", "wrong product", "ban the seller",
        "increase my score", "review my answers"
    ]

    if any(x in t for x in high_risk):
        return "high"

    if any(x in t for x in payment_risk):
        return "high"

    return "low"
