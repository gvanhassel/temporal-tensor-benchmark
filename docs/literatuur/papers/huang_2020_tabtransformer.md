---
title: "TabTransformer: Tabular Data Modeling Using Contextual Embeddings"
authors: ["Huang, X.", "Khetan, A.", "Cvitkovic, M.", "Karnin, Z."]
year: 2020
doi: "10.48550/arXiv.2012.06678"
journal: "arXiv preprint"
open_access_url: "https://arxiv.org/pdf/2012.06678"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, transformer, tabular-data, categorical-embeddings, semi-supervised, classificatie]
---

# TabTransformer: Tabular Data Modeling Using Contextual Embeddings

## Samenvatting
TabTransformer is de eerste transformer-architectuur specifiek ontworpen voor tabulaire data. Het kernidee is dat categorische features eerst worden omgezet naar embeddings, die vervolgens door meerdere transformer-lagen worden verwerkt tot contextuele embeddings. Deze contextuele embeddings vangen relaties tussen verschillende categorische features op. Op 15 publieke datasets presteert TabTransformer minstens 1.0% beter op gemiddelde AUC dan bestaande deep learning-methoden, en evenaart het de prestaties van tree-based ensemble-methoden. Een belangrijke beperking is dat numerieke features niet door de transformer-lagen worden verwerkt, maar pas later worden samengevoegd.

## Sleutelconclusies
- Contextuele embeddings van categorische features via transformers verbeteren de prestaties significant ten opzichte van standaard embeddings
- De contextuele embeddings zijn robuust tegen ontbrekende en ruizige data
- Semi-supervised pre-training (masked language modeling op categorische features) levert gemiddeld 2.1% AUC-verbetering

## Methodologie
Supervised en semi-supervised classificatie op 15 publieke benchmark-datasets. Vergelijking met MLP, tree-based methoden (XGBoost, LightGBM, CatBoost), en andere deep learning-modellen. Evaluatie op AUC, met ablatiestudies voor robuustheid en semi-supervised learning.

## Data & Techniek

### Gebruikte technieken
Transformer encoder (multi-head self-attention + feed-forward), column embeddings voor categorische features, semi-supervised pre-training via replaced token detection. Geimplementeerd in PyTorch.

### Inputdata
Tabulaire datasets met mix van categorische en numerieke features. 15 publieke datasets van diverse grootte en domeinen (o.a. financieel, healthcare, census-data).

### Preprocessing
Categorische features worden omgezet naar leerbare embeddings plus een unieke column embedding per feature. Numerieke features worden genormaliseerd en direct als scalaire waarden meegegeven (niet door de transformer verwerkt).

### Preprocessing-problemen & oplossingen
Ontbrekende waarden — TabTransformer is robuuster dan alternatieven dankzij contextuele embeddings. Ruizige features — idem, contextuele embeddings zijn minder gevoelig. Numerieke features worden niet contextueel verwerkt — dit is een erkende beperking.

### Datapipeline & modelinput
Categorische features -> embedding lookup + column embedding -> transformer encoder (meerdere lagen) -> contextuele embeddings. Numerieke features -> normalisatie -> scalaire waarden. Concatenatie van contextuele categorische embeddings + numerieke waarden -> MLP classificatie-head.

## Beperkingen
- Numerieke features worden niet door de transformer verwerkt, waardoor interacties tussen numerieke en categorische features niet volledig worden gevangen
- Geen temporele component; puur voor statische tabulaire data
- Presteert niet consistent beter dan gradient boosting op alle datasets

## Gerelateerde bronnen
- [[gorishniy_2021_ft_transformer]] — lost de beperking van TabTransformer op door ook numerieke features door de transformer te verwerken
- [[somepalli_2021_saint]] — voegt inter-sample attention toe naast intra-sample attention
- [[choi_2016_retain]] — attention voor sequentiele medische data; complementaire aanpak voor temporele data

## Bronvermelding (APA 7e editie)
Huang, X., Khetan, A., Cvitkovic, M., & Karnin, Z. (2020). TabTransformer: Tabular data modeling using contextual embeddings. *arXiv preprint arXiv:2012.06678*. https://arxiv.org/abs/2012.06678
