---
title: "SAINT: Improved Neural Networks for Tabular Data via Row Attention and Contrastive Pre-Training"
authors: ["Somepalli, G.", "Goldblum, M.", "Schwarzschild, A.", "Bruss, C. B.", "Goldstein, T."]
year: 2021
doi: "10.48550/arXiv.2106.01342"
journal: "arXiv preprint"
open_access_url: "https://arxiv.org/pdf/2106.01342"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, transformer, tabular-data, inter-sample-attention, contrastive-learning, classificatie]
---

# SAINT: Improved Neural Networks for Tabular Data via Row Attention and Contrastive Pre-Training

## Samenvatting
SAINT introduceert twee innovaties voor transformers op tabulaire data. Ten eerste combineert het self-attention over kolommen (features binnen een datapunt) met een nieuw "intersample attention" mechanisme dat rij-attention toepast (vergelijking tussen datapunten). Dit stelt het model in staat om een datapunt te classificeren door het te relateren aan andere rijen in de tabel. Ten tweede introduceren de auteurs een contrastieve self-supervised pre-trainingsmethode voor situaties met weinig gelabelde data. SAINT presteert consistent beter dan eerdere deep learning-methoden en overtreft gemiddeld ook gradient boosting-methoden (XGBoost, CatBoost, LightGBM) op diverse benchmarks.

## Sleutelconclusies
- Intersample attention (rij-attention) is een krachtig mechanisme dat datapunten in context van andere samples plaatst, vergelijkbaar met hoe k-NN werkt maar dan leerbaar
- Contrastieve pre-training verbetert prestaties bij schaarse labels significant
- SAINT is een van de eerste deep learning-modellen dat consistent gradient boosting overtreft op tabulaire data

## Methodologie
Evaluatie op meerdere publieke benchmark-datasets voor tabulaire classificatie. Vergelijking met MLP, TabNet, TabTransformer, NODE, XGBoost, CatBoost, LightGBM. Ablatiestudies voor de bijdrage van intersample attention en contrastieve pre-training afzonderlijk.

## Data & Techniek

### Gebruikte technieken
Self-attention (intra-sample, over features), intersample attention (over datapunten), contrastieve self-supervised pre-training (CutMix-gebaseerde data-augmentatie), embedding-laag voor zowel numerieke als categorische features. PyTorch-implementatie.

### Inputdata
Meerdere publieke tabulaire datasets van UCI Machine Learning Repository en andere bronnen. Mix van categorische en numerieke features. Classificatietaken.

### Preprocessing
Categorische features: leerbare embeddings. Numerieke features: leerbare lineaire projectie naar embedding-ruimte. Data-augmentatie via CutMix (mix van features tussen samples) voor contrastieve pre-training.

### Preprocessing-problemen & oplossingen
Schaarse labels — opgelost via contrastieve pre-training. Heterogene feature-types — opgelost via uniforme embedding-laag voor zowel numerieke als categorische features. Geen standaard data-augmentatie voor tabulaire data — opgelost via CutMix-strategie.

### Datapipeline & modelinput
Elke feature -> embedding -> intra-sample self-attention (kolom-attention) -> intersample attention (rij-attention, vergelijking met batch-genoten) -> classificatie-head. Pre-training: CutMix augmentatie -> contrastieve loss om originele van geaugmenteerde samples te onderscheiden.

## Beperkingen
- Intersample attention is afhankelijk van de batch-samenstelling tijdens training en inferentie
- Geen temporele component; puur voor statische tabulaire data
- Rekenkosten zijn hoger dan TabTransformer door de dubbele attention (kolom + rij)
- Niet gepubliceerd in een top-venue (arXiv preprint)

## Gerelateerde bronnen
- [[huang_2020_tabtransformer]] — voorganger met alleen kolom-attention op categorische features
- [[gorishniy_2021_ft_transformer]] — alternatieve tabular transformer die numerieke features ook als tokens verwerkt
- [[min_2021_explainable_fraud_clustering]] — toepassing van attention-gebaseerde methoden op fraudedetectie

## Bronvermelding (APA 7e editie)
Somepalli, G., Goldblum, M., Schwarzschild, A., Bruss, C. B., & Goldstein, T. (2021). SAINT: Improved neural networks for tabular data via row attention and contrastive pre-training. *arXiv preprint arXiv:2106.01342*. https://arxiv.org/abs/2106.01342
