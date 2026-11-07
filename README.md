# MAP@K for RAG retrieval

A small experiment to score the retrieval step of a RAG system with average precision at K (AP@K) and its mean over queries (MAP@K). It loads a set of queries, the chunks that are relevant to each one and the ranked chunks a retriever returned, and measures how high the relevant chunks landed.

Early stage: `main.py` builds the relevance sets and computes AP for one query. The cutoff at K and the mean over all queries come next.

## The metric

For one query with R relevant chunks, walk down the ranked list. Every time a relevant chunk shows up at rank i, take the precision at that rank (relevant chunks seen so far divided by i). AP@K is the sum of those precisions over the first K results, divided by R. A relevant chunk that never shows up adds nothing to the sum, so the score drops when the retriever misses a chunk, not only when it ranks one low.

MAP@K is the mean of AP@K over all queries. Hit@K, which only asks whether any relevant chunk made the top K, ignores order; MAP@K rewards putting it first.

## Data

`exemplos/` has a toy set in Portuguese about a digital bank account:

| File | Columns |
| --- | --- |
| `chunks.csv` | `chunk_id`, `doc_id`, `text` (11 chunks) |
| `queries.csv` | `query_id`, `query_text` (10 queries) |
| `qrels.csv` | `query_id`, `chunk_id`, `relevance` |
| `retrieval_results.csv` | `query_id`, `rank`, `chunk_id`, `score` (5 results per query) |

## Run it

```bash
pip install pandas
python main.py
```

I later used the same definition, scored over distinct articles, to evaluate the retrieval of a [support agent](https://github.com/ewerside/support-agent-rag).
