def classify(issue):
    t =issue.lower()

    if len(t.strip())<5:
         return "invalid"

    invalid_terms = [
         "ignore previous", "joke", "weather", "recipe", "unrelated",
         "not support", "write a poem"
    ]

    if any(x in t for x in invalid_terms):
         return "invalid"

    bug_terms = [
         "error", "bug", "crash", "broken", "not loading",
         "can't login", "cannot login", "failed", "failure",
         "does not work", "isn't working", "not working"
    ]

    feature_terms = [
         "feature", "add", "request", "enhancement", "support for",
         "can you add", "would like", "i want", "please build"
    ]

    if any(x in t for x in bug_terms):
          return "bug"
    if any(x in t for x in feature_terms):
         return "feature_request"
    return "product_issue"
