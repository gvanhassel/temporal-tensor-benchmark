---
title: "Informer: Beyond Efficient Transformer for Long Sequence Time-Series Forecasting"
authors: ["Zhou, H.", "Zhang, S.", "Peng, J.", "Zhang, S.", "Li, J.", "Xiong, H.", "Zhang, W."]
year: 2021
doi: "10.1609/aaai.v35i12.17325"
journal: "Proceedings of the AAAI Conference on Artificial Intelligence"
open_access_url: "https://arxiv.org/pdf/2012.07436"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, transformer, tijdreeksen, attention, efficiëntie]
---

# Informer: Beyond Efficient Transformer for Long Sequence Time-Series Forecasting

## Samenvatting
De auteurs adresseren het probleem dat standaard Transformers niet direct toepasbaar zijn op lange tijdreeksvoorspellingen (LSTF) vanwege kwadratische tijdcomplexiteit, hoog geheugengebruik en trage decoder-inferentie. Ze introduceren Informer, een efficiënt Transformer-model met drie innovaties: (1) een ProbSparse self-attention mechanisme dat de complexiteit reduceert naar O(L log L), (2) een self-attention distillatietechniek die de invoerlengte halveert per laag en zo extreem lange sequenties aankan, en (3) een generatieve decoder die de volledige voorspellingshorizon in één forward pass produceert in plaats van autoregressief stap-voor-stap. Experimenten op vier datasets (elektriciteitsverbruik, temperatuur, weer) tonen aan dat Informer aanzienlijk beter presteert dan bestaande methoden voor LSTF-taken, met name bij lange voorspellingshorizons.

## Sleutelconclusies
- ProbSparse self-attention selecteert alleen de meest informatieve queries, waardoor de complexiteit daalt van O(L²) naar O(L log L) zonder significant informatieverlies
- De distillatie-operatie in opeenvolgende encoder-lagen halveert de invoerlengte progressief, waardoor het model geheugenefficiënt omgaat met zeer lange sequenties
- De generatieve decoder voorspelt de hele outputsequentie in één keer, wat de cumulatieve fouten van autoregressieve decodering elimineert en de inferentiesnelheid sterk verbetert

## Methodologie
De auteurs evalueren Informer op vier reële datasets: ETTh1, ETTh2, ETTm1 (elektriciteitsverbruik) en een weerdataset. Ze vergelijken met ARIMA, Prophet, LSTMa, LSTnet, en de standaard Transformer. De evaluatie gebruikt MSE en MAE als metrics over diverse voorspellingshorizons (24, 48, 168, 336, 720 stappen). Er wordt gebruik gemaakt van een encoder-decoder architectuur met multi-head ProbSparse attention.

## Data & Techniek

### Gebruikte technieken
ProbSparse Self-Attention, Self-Attention Distilling, Generative Style Decoder, Multi-head Attention, Transformer encoder-decoder architectuur, PyTorch

### Inputdata
Tijdreeksdata in tabelvorm: ETT-datasets (Electricity Transformer Temperature) met uurlijkse en 15-minuten granulariteit, meerdere variabelen per tijdstip. Univariate en multivariate settings.

### Preprocessing
Standaard normalisatie van de tijdreeksen. Sliding window benadering voor het creëren van invoer-uitvoer paren. Train/validatie/test splits op temporele basis (chronologisch).

### Preprocessing-problemen & oplossingen
Het kernprobleem is de lengte van invoersequenties: standaard self-attention schaalt kwadratisch. Opgelost via ProbSparse selectie (alleen top-u queries) en cascading distillation (halving per laag). Autoregressieve foutaccumulatie opgelost door generatieve decoder.

### Datapipeline & modelinput
Invoer is een tensor van vorm (batch, sequentielengte, features). De encoder verwerkt een lange look-back window; de decoder ontvangt een starttoken (deel van de invoer) en genereert de volledige voorspellingshorizon in één pass. Positional encoding wordt toegevoegd aan de invoer-embeddings.

## Beperkingen
- De ProbSparse benadering kan bij bepaalde datapatronen relevante queries missen
- Het model is primair geëvalueerd op energiedata; generaliseerbaarheid naar andere domeinen is beperkt aangetoond
- De keuze van hyperparameters (zoals de sampling factor c) beïnvloedt de prestaties maar wordt niet uitvoerig geanalyseerd

## Gerelateerde bronnen
- [[wu_2021_autoformer]] — bouwt voort op Informer maar vervangt attention door auto-correlatie
- [[zhou_2022_fedformer]] — zelfde eerste auteur; combineert frequentiedomein met decompositie als verbetering op Informer
- [[nie_2023_patchtst]] — alternatieve efficiënte aanpak via patching in plaats van sparse attention
- [[zeng_2023_dlinear]] — kritische paper die betoogt dat simpele lineaire modellen Informer overtreffen

## Bronvermelding (APA 7e editie)
Zhou, H., Zhang, S., Peng, J., Zhang, S., Li, J., Xiong, H., & Zhang, W. (2021). Informer: Beyond Efficient Transformer for Long Sequence Time-Series Forecasting. *Proceedings of the AAAI Conference on Artificial Intelligence*, *35*(12), 11106-11115. https://doi.org/10.1609/aaai.v35i12.17325
