from cleaner import clean

def respond(results, status):
    if not results:
        return "I'm unable to find a reliable answer. Please contact support."

    if status == "escalated":
        return "This issue requires review by our support team."

    cleaned = ""
    for result in results:
        candidate = clean(result["text"])
        if len(candidate.strip()) >= 10:
            cleaned = candidate
            break

    if len(cleaned.strip()) < 10:
        return "I couldn't find a clear solution for this issue. Please contact support."

    return f"""
Here's what you can try:
{cleaned}

If this doesn't resolve your issue, please contact support.
""".strip()
