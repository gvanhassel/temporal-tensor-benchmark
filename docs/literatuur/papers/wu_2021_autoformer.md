---
title: "Autoformer: Decomposition Transformers with Auto-Correlation for Long-Term Series Forecasting"
authors: ["Wu, H.", "Xu, J.", "Wang, J.", "Long, M."]
year: 2021
doi: "10.48550/arXiv.2106.13008"
journal: "Advances in Neural Information Processing Systems (NeurIPS)"
open_access_url: "https://arxiv.org/pdf/2106.13008"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, transformer, tijdreeksen, decompositie, auto-correlatie]
---

# Autoformer: Decomposition Transformers with Auto-Correlation for Long-Term Series Forecasting

## Samenvatting
Wu et al. presenteren Autoformer, een Transformer-architectuur die tijdreeksdecompositie integreert als intern bouwblok in plaats van als preprocessingstap. Het model introduceert een Auto-Correlation mechanisme dat de standaard self-attention vervangt. Dit mechanisme is geïnspireerd door stochastische procestheorie en werkt op sub-serie niveau: het ontdekt periodiciteit in de data, vindt vergelijkbare sub-series over perioden heen, en aggregeert deze. De decompositie scheidt trend- en seizoenscomponenten in elke laag van het netwerk, waardoor het model progressief de globale structuur (trend) en gedetailleerde patronen (seizoen) kan extraheren. Op zes benchmarks (energie, verkeer, economie, weer, ziekte) behaalt Autoformer een relatieve verbetering van 38% ten opzichte van eerdere state-of-the-art methoden.

## Sleutelconclusies
- Series decompositie als intern architectuurblok (in elke encoder/decoder-laag) is effectiever dan als eenmalige preprocessingstap
- Het Auto-Correlation mechanisme ontdekt afhankelijkheden op sub-serie niveau via periodiciteitsdetectie, wat robuuster is dan punt-niveau attention
- O(L log L) complexiteit door het gebruik van Fast Fourier Transform (FFT) voor het berekenen van autocorrelaties

## Methodologie
Evaluatie op zes benchmarkdatasets: ETTh1, ETTh2, ETTm1, ETTm2, Weather, Electricity, Traffic, ILI (influenza-like illness). Vergelijking met Informer, LogTrans, Reformer, en andere baselines. MSE en MAE als evaluatiemetrics. Diverse voorspellingshorizons (96, 192, 336, 720).

## Data & Techniek

### Gebruikte technieken
Auto-Correlation mechanisme (vervangt self-attention), Series Decomposition Block (moving average voor trend, rest als seizoenscomponent), FFT voor periodiciteitsdetectie, Encoder-Decoder architectuur, PyTorch

### Inputdata
Multivariate tijdreeksdata in tabelvorm. Zes datasets variërend van uurlijks tot dagelijks. Variabelen omvatten temperatuur, elektriciteitsverbruik, verkeersstromen, economische indicatoren, en epidemiologische data.

### Preprocessing
Standaard normalisatie (zero-mean, unit-variance). Chronologische train/validatie/test splits. De interne decompositie (trend-seizoen scheiding via moving average) is onderdeel van het model zelf, niet van preprocessing.

### Preprocessing-problemen & oplossingen
Complexe temporele patronen met meerdere seizoenscomponenten worden aangepakt door de decompositie in elke laag te herhalen, waardoor het model progressief complexere patronen kan ontrafelen. De moving average kernelgrootte is een hyperparameter.

### Datapipeline & modelinput
Invoer: tensor (batch, sequentielengte, features). In elke encoder-laag wordt de invoer ontleed in trend en seizoen. Het Auto-Correlation mechanisme verwerkt de seizoenscomponent door vergelijkbare sub-series te aggregeren. De decoder combineert trend- en seizoensuitvoer voor de finale voorspelling.

## Beperkingen
- Het Auto-Correlation mechanisme veronderstelt periodiciteit in de data; bij niet-periodieke reeksen kan het minder effectief zijn
- De keuze van de moving average kernelgrootte voor decompositie is handmatig en kan de resultaten beïnvloeden
- Prestaties op zeer onregelmatige of niet-stationaire data zijn niet uitvoerig onderzocht

## Gerelateerde bronnen
- [[zhou_2021_informer]] — voorganger; Autoformer verbetert op Informer's attention-mechanisme
- [[zhou_2022_fedformer]] — bouwt voort op Autoformers decompositie-idee maar voegt frequentiedomein-aandacht toe
- [[nie_2023_patchtst]] — alternatieve benadering die channel-independence gebruikt
- [[zeng_2023_dlinear]] — gebruikt Autoformers decompositie-idee maar vervangt de Transformer door lineaire lagen

## Bronvermelding (APA 7e editie)
Wu, H., Xu, J., Wang, J., & Long, M. (2021). Autoformer: Decomposition Transformers with Auto-Correlation for Long-Term Series Forecasting. *Advances in Neural Information Processing Systems*, *34*, 22419-22430. https://arxiv.org/abs/2106.13008
