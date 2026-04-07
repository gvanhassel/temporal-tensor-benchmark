---
title: "Deep Transformer Models for Time Series Forecasting: The Influenza Prevalence Case"
authors: ["Wu, N.", "Green, B.", "Ben, X.", "O'Banion, S."]
year: 2020
doi: "10.48550/arXiv.2001.08317"
journal: "arXiv preprint"
open_access_url: "https://arxiv.org/pdf/2001.08317"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, transformer, tijdreeksen, time-series, influenza, forecasting]
---

# Deep Transformer Models for Time Series Forecasting: The Influenza Prevalence Case

## Samenvatting
Dit paper presenteert een raamwerk voor tijdreeksvoorspelling gebaseerd op de Transformer-architectuur, met influenza-achtige ziekte (ILI) als casestudie. De auteurs passen de self-attention mechanismen van de Transformer aan voor het leren van complexe patronen en dynamieken in tijdreeksdata. Het raamwerk ondersteunt zowel univariate als multivariate tijdreeksen, evenals tijdreeks-embeddings. Het model wordt gevalideerd op influenza-prevalentiedata en behaalt resultaten die vergelijkbaar zijn met of beter dan bestaande state-of-the-art methoden. De bijdrage ligt vooral in het demonstreren dat Transformers een generiek en effectief raamwerk bieden voor tijdreeksvoorspelling, buiten het oorspronkelijke NLP-domein.

## Sleutelconclusies
- De Transformer-architectuur is generiek toepasbaar op tijdreeksvoorspelling en beperkt zich niet tot NLP
- Self-attention kan effectief temporele afhankelijkheden op lange termijn vastleggen in epidemiologische data
- Het raamwerk is flexibel genoeg om zowel univariate, multivariate als embedded tijdreeksen te verwerken

## Methodologie
Toepassing van een aangepaste Transformer op influenza-prevalentiedata (ILI-percentages). Het model gebruikt een encoder-decoder architectuur met self-attention voor het vastleggen van temporele patronen. Vergelijking met traditionele tijdreeksmodellen (ARIMA) en recurrente neurale netwerken (LSTM). Evaluatie op basis van voorspellingsfout over meerdere horizonnen.

## Data & Techniek

### Gebruikte technieken
Transformer encoder-decoder architectuur, multi-head self-attention, positional encoding voor temporele positie, fully connected lagen voor output-projectie.

### Inputdata
Influenza-achtige ziekte (ILI) surveillance data van het CDC (Centers for Disease Control and Prevention). Wekelijkse ILI-percentages over meerdere regio's in de Verenigde Staten. Multivariate variant bevat meerdere regio's als parallelle kanalen.

### Preprocessing
Temporele normalisatie van ILI-percentages. Sliding window-aanpak voor het creeren van invoer-uitvoer paren. Chronologische train/test-split om datalekkage te voorkomen. Positional encoding toegevoegd om de temporele volgorde te behouden.

### Preprocessing-problemen & oplossingen
Seizoensgebondenheid in influenzadata wordt impliciet geleerd door het self-attention mechanisme, dat patronen over lange afstanden kan detecteren. Ruis in surveillancedata wordt afgevlakt door het model te trainen op voldoende historische data.

### Datapipeline & modelinput
Input: tijdreeks van vorm (batch_size x vensterlengte x features). Positional encoding wordt toegevoegd aan de invoer-embeddings. De encoder verwerkt het historische venster en de decoder genereert voorspellingen. Het model kan zowel single-step als multi-step voorspellingen produceren.

## Beperkingen
- Alleen gevalideerd op een enkel toepassingsdomein (influenza), waardoor generaliseerbaarheid beperkt is aangetoond
- Geen vergelijking met andere Transformer-varianten voor tijdreeksen (zoals Li et al., 2019)
- Het paper is een arXiv preprint en is niet gepubliceerd in een peer-reviewed tijdschrift of conferentieproceedings
- Beperkte ablatiestudies over de invloed van hyperparameters

## Gerelateerde bronnen
- [[vaswani_2017_attention_is_all_you_need]] — de oorspronkelijke Transformer-architectuur waarop dit werk is gebaseerd
- [[li_2019_logsparse_transformer_time_series]] — eerder werk over Transformers voor tijdreeksen, met oplossingen voor schaalbaarheid
- [[devlin_2019_bert]] — demonstreert de kracht van pre-training met Transformers, potentieel toepasbaar op tijdreeksrepresentaties
- [[dosovitskiy_2020_vision_transformer]] — vergelijkbare aanpak van Transformer-toepassing buiten NLP

## Bronvermelding (APA 7e editie)
Wu, N., Green, B., Ben, X., & O'Banion, S. (2020). Deep Transformer models for time series forecasting: The influenza prevalence case. *arXiv preprint arXiv:2001.08317*. https://doi.org/10.48550/arXiv.2001.08317
