---
title: "Revisiting Deep Learning Models for Tabular Data"
authors: ["Gorishniy, Y.", "Rubachev, I.", "Khrulkov, V.", "Babenko, A."]
year: 2021
doi: "10.48550/arXiv.2106.11959"
journal: "Advances in Neural Information Processing Systems (NeurIPS)"
open_access_url: "https://arxiv.org/pdf/2106.11959"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, transformer, tabular-data, FT-Transformer, ResNet, benchmark, classificatie]
---

# Revisiting Deep Learning Models for Tabular Data

## Samenvatting
Dit paper voert een uitgebreide en gestandaardiseerde evaluatie uit van deep learning-modellen voor tabulaire data. De auteurs introduceren FT-Transformer (Feature Tokenizer + Transformer), dat zowel categorische als numerieke features omzet naar tokens die door een transformer worden verwerkt. Dit lost een kernbeperking van TabTransformer op, waar numerieke features buiten de transformer bleven. FT-Transformer presteert op de meeste taken het best onder de deep learning-modellen. Daarnaast tonen de auteurs aan dat een eenvoudige ResNet-achtige architectuur een sterke baseline vormt die in eerder werk vaak niet meegenomen werd. De conclusie is dat er nog geen universeel superieure oplossing is: gradient boosted decision trees (GBDT) presteren op sommige datasets beter.

## Sleutelconclusies
- FT-Transformer verwerkt zowel numerieke als categorische features als tokens door de transformer, wat significant beter presteert dan TabTransformer
- Een simpele ResNet-architectuur is een verrassend sterke baseline voor tabulaire data die eerder onderbelicht was
- Er is geen universeel beste model: FT-Transformer wint op de meeste taken, maar GBDT's winnen op sommige

## Methodologie
Systematische benchmark op 11 publieke datasets met gestandaardiseerde evaluatieprotocollen. Vergelijking van MLP, ResNet, SNN, NODE, TabNet, TabTransformer, FT-Transformer, XGBoost, CatBoost, LightGBM. Hyperparameter-tuning via Optuna. Evaluatie op accuracy/RMSE.

## Data & Techniek

### Gebruikte technieken
FT-Transformer: Feature Tokenizer die elke feature (numeriek of categorisch) omzet naar een token-embedding, gevolgd door een standaard transformer encoder. ResNet-achtige architectuur als baseline. Hyperparameter-optimalisatie via Optuna.

### Inputdata
11 publieke tabulaire datasets van diverse grootte (duizenden tot honderdduizenden rijen), met mix van numerieke en categorische features. Classificatie- en regressietaken.

### Preprocessing
Numerieke features: per-feature normalisatie. Categorische features: leerbare embeddings. Feature Tokenizer: lineaire projectie van numerieke waarden naar d-dimensionale vectoren, plus leerbare [CLS]-token.

### Preprocessing-problemen & oplossingen
Niet-gestandaardiseerde evaluatie in eerder werk — opgelost door uniforme evaluatieprotocollen en hyperparameter-tuning budgetten. Variabiliteit in datasetgrootte — consistente train/val/test splits.

### Datapipeline & modelinput
Elke feature (numeriek of categorisch) -> Feature Tokenizer -> d-dimensionaal token. Alle tokens + [CLS]-token -> transformer encoder. [CLS]-output -> lineaire classificatie/regressie-head.

## Beperkingen
- Geen temporele component; uitsluitend voor statische tabulaire data
- Transformer schaalt kwadratisch met het aantal features (kolommen), wat problematisch kan zijn bij zeer brede datasets
- Evaluatie op relatief kleine datasets; schaalbaarheid naar miljoenen rijen niet getest

## Gerelateerde bronnen
- [[huang_2020_tabtransformer]] — voorganger die alleen categorische features door de transformer verwerkt
- [[somepalli_2021_saint]] — alternatieve tabular transformer met inter-sample attention
- [[choi_2016_retain]] — attention voor sequentiele data; mogelijke combinatie met FT-Transformer voor temporele + tabulaire features

## Bronvermelding (APA 7e editie)
Gorishniy, Y., Rubachev, I., Khrulkov, V., & Babenko, A. (2021). Revisiting deep learning models for tabular data. In *Advances in Neural Information Processing Systems* (NeurIPS 2021, Vol. 34). https://arxiv.org/abs/2106.11959
