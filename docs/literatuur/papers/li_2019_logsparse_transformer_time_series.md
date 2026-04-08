---
title: "Enhancing the Locality and Breaking the Memory Bottleneck of Transformer on Time Series Forecasting"
authors: ["Li, S.", "Jin, X.", "Xuan, Y.", "Zhou, X.", "Chen, W.", "Wang, Y.-X.", "Yan, X."]
year: 2019
doi: "10.48550/arXiv.1907.00235"
journal: "Advances in Neural Information Processing Systems (NeurIPS 2019)"
open_access_url: "https://arxiv.org/pdf/1907.00235"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, transformer, tijdreeksen, time-series, logsparse, convolutional-attention]
---

# Enhancing the Locality and Breaking the Memory Bottleneck of Transformer on Time Series Forecasting

## Samenvatting
Dit paper is een van de eerste werken die de Transformer-architectuur specifiek aanpast voor tijdreeksvoorspelling. De auteurs identificeren twee fundamentele beperkingen van de standaard Transformer voor tijdreeksen: (1) de punt-voor-punt dot-product self-attention is niet gevoelig voor lokale temporele patronen (locality-agnostisch), en (2) het geheugenverbruik groeit kwadratisch met de sequentielengte, waardoor lange tijdreeksen niet direct gemodelleerd kunnen worden. Als oplossing introduceren zij twee innovaties: convolutional self-attention, waarbij queries en keys worden gegenereerd via causale convolutie om lokale context te integreren, en de LogSparse Transformer, die het geheugenverbruik reduceert tot O(L(log L)^2). Het model wordt gevalideerd op synthetische en echte datasets, waaronder zonne-energie, elektriciteitsverbruik en verkeersdata, en presteert beter dan bestaande methoden zoals ARIMA, LSTNet en standaard Transformers.

## Sleutelconclusies
- Standaard Transformers zijn niet optimaal voor tijdreeksen vanwege gebrek aan lokaliteitsbewustzijn en kwadratisch geheugenverbruik
- Causale convolutie in de attention-laag verbetert de gevoeligheid voor lokale temporele patronen aanzienlijk
- LogSparse attention maakt het mogelijk om lange tijdreeksen te verwerken met beheersbaar geheugenverbruik, zonder significant prestatieverlies

## Methodologie
Experimenten op zowel synthetische data (om causale relaties gecontroleerd te testen) als echte datasets: Solar Energy (zonnepaneel-output, 137 stations), Electricity (elektriciteitsverbruik, 321 klanten), Traffic (bezettingspercentage, 862 sensoren). Vergelijking met ARIMA, VAR-MLP, GP, LSTNet-Skip, LSTNet-Attn, MTGNN en standaard Transformer. Evaluatiemetrieken: RSE (Relative Squared Error) en CORR (correlatie).

## Data & Techniek

### Gebruikte technieken
Convolutional self-attention (queries/keys via causale convolutie), LogSparse Transformer (sparse attention met logaritmische stap), standaard multi-head attention als basis, encoder-decoder Transformer-architectuur.

### Inputdata
Multivariate tijdreeksen: Solar Energy (137 variabelen, 52.560 tijdstappen), Electricity (321 variabelen, 26.304 tijdstappen), Traffic (862 variabelen, 17.544 tijdstappen). Invoervensters van variabele lengte, voorspellingshorizon van 3 tot 24 stappen.

### Preprocessing
Standaard normalisatie van de tijdreeksdata. Train/validatie/test-split op temporele basis (geen shuffling om datalekkage te voorkomen). Sliding window-benadering voor het creeren van invoer-uitvoer paren.

### Preprocessing-problemen & oplossingen
Het kwadratische geheugenprobleem van standaard attention wordt opgelost door LogSparse attention: in plaats van alle posities te attenderen, selecteert het model posities op exponentieel toenemende afstand. Het lokaliteitsprobleem wordt opgelost door causale convolutie in de query/key-generatie, zodat elke positie informatie van aangrenzende tijdstappen meekrijgt.

### Datapipeline & modelinput
Input: een multivariate tijdreeks van vorm (batch_size x vensterlengte x aantal_variabelen). De encoder verwerkt het historische venster; de decoder genereert autoregressief de voorspelling. Convolutional self-attention vervangt standaard dot-product attention: queries en keys worden gegenereerd door een causale 1D-convolutie over de tijdsdimensie.

## Beperkingen
- LogSparse attention verliest potentieel informatie door niet alle posities te attenderen
- De benadering is primair getest op univariate en laaggecorreleerde multivariate data; complexe afhankelijkheden tussen variabelen worden beperkt gemodelleerd
- Causale convolutie voegt hyperparameters toe (kernelgrootte) die per dataset getuned moeten worden
- Niet getest op zeer hoogdimensionale data of 3D-tensorstructuren

## Gerelateerde bronnen
- [[vaswani_2017_attention_is_all_you_need]] — de oorspronkelijke Transformer-architectuur die hier wordt aangepast
- [[wu_2020_deep_transformer_influenza]] — vergelijkbare toepassing van Transformers op tijdreeksen, gepubliceerd kort na dit werk
- [[devlin_2019_bert]] — pre-training paradigma dat potentieel toepasbaar is op tijdreeksrepresentaties
- [[dosovitskiy_2020_vision_transformer]] — vergelijkbare aanpak van het opdelen van data in "patches" (hier: tijdvensters)

## Bronvermelding (APA 7e editie)
Li, S., Jin, X., Xuan, Y., Zhou, X., Chen, W., Wang, Y.-X., & Yan, X. (2019). Enhancing the locality and breaking the memory bottleneck of Transformer on time series forecasting. *Advances in Neural Information Processing Systems*, *32*, 5243-5253. https://doi.org/10.48550/arXiv.1907.00235
