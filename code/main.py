import pandas as pd
from loader import load_docs
from retriever import build_index, search
from classifier import classify
from risk import risk_level
from decision import decide
from responder import respond

docs = load_docs()
chunks, meta, emb = build_index(docs)

df = pd.read_csv("support_tickets/support_tickets.csv")

output = []

def explain_decision(status, score, risk):
    lines = [
        f"The issue was matched with relevant support documentation (similarity score: {round(score,2)}).",
        f"Risk level was assessed as {risk}."
    ]
    if status == "escalated":
        lines.append("The issue was escalated because it is sensitive, high-risk, or not safe to answer directly from the retrieved documentation.")
    else:
        lines.append("The issue was answered directly because the retrieved documentation was relevant and the risk level was low.")
    return " ".join(lines)


for _, row in df.iterrows():
    issue = str(row["Issue"])
    subject = str(row.get("Subject", ""))
    company = str(row.get("Company", ""))

    query = " ".join(x for x in [company, subject, issue] if x and x.lower() != "nan")

    results = search(query, chunks, meta, emb, company=company)

    req = classify(query)
    risk = risk_level(query)

    status, score = decide(results, risk, query)

    if not results:
        product_area = f"{company.lower()} (general)"
        response = "I'm unable to find a reliable answer. Please contact support."
        status = "escalated"
    else:
        product_area = f"{results[0]['meta']['company']} ({results[0]['meta']['product_area']})"
        response = respond(results, status)

        if response.startswith("I couldn't find a clear solution") and status == "escalated":
            status = "escalated"
            response = "This issue requires review by our support team."

    justification = explain_decision(status, score, risk)

    output.append({
        "status": status,
        "product_area": product_area,
        "response": response,
        "justification": justification,
        "request_type": req
    })

pd.DataFrame(output).to_csv("support_tickets/output.csv", index=False)
print(f"Wrote {len(output)} rows to support_tickets/output.csv")
