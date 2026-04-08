---
title: "Crossformer: Transformer Utilizing Cross-Dimension Dependency for Multivariate Time Series Forecasting"
authors: ["Zhang, Y.", "Yan, J."]
year: 2023
doi: ""
journal: "Proceedings of the International Conference on Learning Representations (ICLR)"
open_access_url: "https://openreview.net/forum?id=vSVLM2j9eie"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, transformer, tijdreeksen, cross-dimensie, multivariaat, two-stage-attention]
---

# Crossformer: Transformer Utilizing Cross-Dimension Dependency for Multivariate Time Series Forecasting

## Samenvatting
Zhang en Yan stellen dat bestaande Transformer-modellen voor tijdreeksen zich primair richten op temporele afhankelijkheden (cross-time) maar de afhankelijkheden tussen variabelen (cross-dimension) verwaarlozen, terwijl deze cruciaal zijn voor multivariate voorspelling. Crossformer pakt dit aan met drie innovaties: (1) Dimension-Segment-Wise (DSW) embedding die de invoer omzet naar een 2D vector-array dat zowel tijd- als dimensie-informatie behoudt, (2) een Two-Stage Attention (TSA) laag die eerst cross-time en vervolgens cross-dimension afhankelijkheden modelleert, en (3) een Hierarchical Encoder-Decoder (HED) die informatie op meerdere schalen combineert. Het cross-dimension stadium gebruikt een router-mechanisme met een klein vast aantal "routers" die informatie verzamelen uit alle dimensies en herverdelen, waardoor de complexiteit daalt naar O(D) in het aantal dimensies. Experimenten op zes datasets tonen de effectiviteit aan.

## Sleutelconclusies
- Cross-dimensie afhankelijkheden zijn essentieel voor multivariate tijdreeksvoorspelling en worden door de meeste Transformer-modellen genegeerd
- De DSW embedding behoudt de 2D-structuur (tijd x dimensies) die verloren gaat bij standaard punt- of tijdstap-embeddings
- Het router-mechanisme in de cross-dimension attention-fase schaalt lineair met het aantal dimensies, waardoor het model toepasbaar is op hoog-dimensionale data

## Methodologie
Evaluatie op zes benchmarkdatasets: ETTh1, ETTh2, ETTm1, ETTm2, Weather, Electricity, Traffic. Vergelijking met Informer, Autoformer, FEDformer, PatchTST, en andere baselines. MSE en MAE als evaluatiemetrics. Voorspellingshorizons: 96, 192, 336, 720. Ablatiestudies voor DSW embedding, TSA, en het router-mechanisme.

## Data & Techniek

### Gebruikte technieken
Dimension-Segment-Wise (DSW) Embedding, Two-Stage Attention (TSA): Cross-Time Stage + Cross-Dimension Stage, Router Mechanism voor efficiënte cross-dimensie attention, Hierarchical Encoder-Decoder (HED), Multi-scale temporal representatie, PyTorch

### Inputdata
Multivariate tijdreeksdata in tabelvorm. De invoer wordt behandeld als een 2D-structuur: dimensies (variabelen) x tijd. Elke variabele wordt in segmenten opgedeeld voor de DSW embedding.

### Preprocessing
Standaard normalisatie. Segmentatie van elke variabele in tijdsegmenten (vergelijkbaar met patches). De segmenten worden per dimensie apart geëmbedded, resulterend in een 2D array van embeddings. Chronologische train/val/test splits.

### Preprocessing-problemen & oplossingen
Het verlies van dimensie-informatie bij standaard Transformer-embeddings wordt opgelost door de DSW embedding die expliciet de 2D-structuur behoudt. Schaalbaarheidsproblemen bij cross-dimensie attention (kwadratisch in aantal dimensies) worden opgelost door het router-mechanisme.

### Datapipeline & modelinput
Invoer: tensor (batch, dimensies, sequentielengte) -> DSW embedding -> 2D array (batch, dimensies, segmenten, embedding_dim) -> TSA lagen (eerst cross-time attention per dimensie, dan cross-dimension attention via routers) -> HED op meerdere schalen -> finale voorspelling (batch, dimensies, voorspellingshorizon).

## Beperkingen
- Het router-mechanisme introduceert een informatieknelpunt: alle cross-dimensie informatie moet via een beperkt aantal routers
- De twee-fase attention (eerst tijd, dan dimensie) modelleert geen directe tijd-dimensie interacties
- Bij datasets waar variabelen weinig onderling gerelateerd zijn, kan de cross-dimensie attention ruis toevoegen

## Gerelateerde bronnen
- [[zhou_2021_informer]] — Crossformer verbetert op Informer door cross-dimensie afhankelijkheden toe te voegen
- [[wu_2021_autoformer]] — Crossformer adresseert een beperking van Autoformer: het negeren van cross-variabele relaties
- [[nie_2023_patchtst]] — tegenovergestelde ontwerpfilosofie: PatchTST kiest voor channel-independence, Crossformer voor cross-dimensie modellering
- [[zhou_2022_fedformer]] — FEDformer focust op frequentiedomein maar negeert ook cross-dimensie relaties
- [[zeng_2023_dlinear]] — DLinear's channel-independence argument staat lijnrecht tegenover Crossformers cross-dimensie benadering

## Bronvermelding (APA 7e editie)
Zhang, Y., & Yan, J. (2023). Crossformer: Transformer Utilizing Cross-Dimension Dependency for Multivariate Time Series Forecasting. *Proceedings of the International Conference on Learning Representations (ICLR 2023)*. https://openreview.net/forum?id=vSVLM2j9eie
