# Support Triage Agent

This agent reads `support_tickets/support_tickets.csv`, searches the local support corpus in `data/`, and writes predictions to `support_tickets/output.csv`.

## Install

From the repository root:

```bash
pip install -r requirements.txt
```

The first run may download the `sentence-transformers/all-MiniLM-L6-v2` model if it is not already cached.

## Run

From the repository root:

```bash
python code/main.py
```

## Approach

The solution uses a small local RAG pipeline:

1. Load Markdown support documents for Claude, HackerRank, and Visa.
2. Split documents into chunks.
3. Embed chunks with `sentence-transformers`.
4. Retrieve relevant chunks for each ticket using issue, subject, and company metadata.
5. Classify request type, assess risk, choose reply or escalation, and generate a grounded response.

High-risk, sensitive, or weakly supported cases are escalated instead of answered directly.
