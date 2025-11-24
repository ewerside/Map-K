import pandas as pd

queries = pd.read_csv('exemplos/queries.csv')
qrels = pd.read_csv('exemplos/qrels.csv')
retrieval_results = pd.read_csv('exemplos/retrieval_results.csv')

print(f"QUERIES:\n{queries.head()}\n\nCHUNK RELEVANCE:\n{qrels.head(10)}")

query_chunks = {}

for query in queries.query_id.unique():
    query_chunks[query] = set()
    for chunk in qrels[qrels.query_id == query].chunk_id:
        query_chunks[query].add(chunk)


for key, value in query_chunks.items():
    print(f"Key: {key}\nValues:{value}\n")

retrieved_chunks = ['DOC001_CH_0001', 'DOC001_CH_0003', 'DOC002_CH_0002']

def avg_p(query, retrieved_chunks, k=1):
    precisions = []
    total_relevant_chunks = len(query_chunks[query])
    total_retrieved_chunks = len(retrieved_chunks) # will be relevant later for max k
    retrieved_relevant_chunks = 0
    n_chunks = 0
    for chunk in retrieved_chunks:
        n_chunks += 1
        if chunk in query_chunks[query]:
            retrieved_relevant_chunks += 1
            precisions.append(retrieved_relevant_chunks/n_chunks)
    ap_at_k = sum(precisions)/total_relevant_chunks
    return ap_at_k

retrieved_set = retrieval_results[retrieval_results["query_id"] == 'Q007']['chunk_id']
print(qrels[qrels["query_id"]=='Q007'])
print(retrieved_set)

print(avg_p('Q007', retrieved_set))






