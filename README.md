# MAP@K para avaliação de RAG

Este repositório guarda um experimento simples para calcular métricas de MAP@K em um fluxo de Retrieval-Augmented Generation (RAG). A ideia é carregar consultas, relevâncias e resultados de busca para medir rapidamente a qualidade do ranking.

Estado atual: começo do desenvolvimento. O script `main.py` faz a leitura dos CSVs em `exemplos/` e calcula métricas básicas para inspecionar o desempenho inicial.

Uso rápido:
- Prepare os CSVs em `exemplos/` (queries, qrels e retrieval_results).
- Execute `python main.py` para rodar os cálculos preliminares.

Mais ajustes e melhorias virão conforme o experimento evolui.
