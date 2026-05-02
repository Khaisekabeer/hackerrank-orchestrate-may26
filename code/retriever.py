from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def build_index(docs):
    chunks =[]
    meta =[]
    for doc in docs:
        words = doc["text"].split()

        for i in range(0,len(words),200):
            chunk = " ".join(words[i:i+200])

            chunks.append(chunk)
            meta.append(doc)

    embeddings = model.encode(chunks,convert_to_tensor=True)

    return chunks,meta,embeddings

def search(query,chunks,meta,embeddings,k=3,company=None):
    q_emb=model.encode(query,convert_to_tensor =True)
    scores = util.cos_sim(q_emb,embeddings)[0]

    company = (company or "").strip().lower()
    candidate_indices = list(range(len(chunks)))

    if company and company != "none":
        filtered = [i for i, m in enumerate(meta) if m["company"].lower() == company]
        if filtered:
            candidate_indices = filtered

    candidate_scores = scores[candidate_indices]
    top = candidate_scores.topk(min(k, len(candidate_indices)))

    results =[]

    for idx in top.indices:
        i = candidate_indices[int(idx)]
        results.append({
            "text":chunks[i],
            "meta":meta[i],
            "score":float(scores[i])
        })
    return results
