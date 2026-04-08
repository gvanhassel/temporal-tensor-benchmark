---
title: "FEDformer: Frequency Enhanced Decomposed Transformer for Long-term Series Forecasting"
authors: ["Zhou, T.", "Ma, Z.", "Wen, Q.", "Wang, X.", "Sun, L.", "Jin, R."]
year: 2022
doi: "10.48550/arXiv.2201.12740"
journal: "Proceedings of the 39th International Conference on Machine Learning (ICML)"
open_access_url: "https://arxiv.org/pdf/2201.12740"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, transformer, tijdreeksen, frequentiedomein, decompositie, Fourier]
---

# FEDformer: Frequency Enhanced Decomposed Transformer for Long-term Series Forecasting

## Samenvatting
Zhou et al. combineren de Transformer-architectuur met seizoen-trend decompositie en frequentiedomein-representaties. Het kernidee is dat de meeste tijdreeksen een sparse representatie hebben in bekende bases zoals de Fourier-transformatie. Door attention te berekenen in het frequentiedomein in plaats van het tijddomein, bereikt het model lineaire complexiteit O(L) in plaats van kwadratisch. FEDformer biedt twee varianten: FEB (Fourier Enhanced Block) die Fourier-transformatie gebruikt, en WEB (Wavelet Enhanced Block) die wavelet-transformatie toepast. Beide varianten combineren frequentie-aandacht met de decompositie-aanpak van Autoformer. Op zes benchmarkdatasets reduceert FEDformer de voorspelfout met 14,8% (multivariaat) en 22,6% (univariaat) vergeleken met de toenmalige state-of-the-art.

## Sleutelconclusies
- Frequentiedomein-attention bereikt lineaire complexiteit en vangt globale patronen effectiever dan tijddomein-attention
- De combinatie van Fourier/wavelet-representatie met seizoen-trend decompositie levert consistente verbeteringen over diverse datasets
- Sparse selectie van frequentiecomponenten voorkomt overfitting en verbetert generalisatie

## Methodologie
Evaluatie op zes datasets: ETTh1, ETTh2, ETTm1, ETTm2, Weather, Electricity, Traffic, ILI. Vergelijking met Informer, Autoformer, LogTrans, Reformer, FiLM, en andere baselines. MSE en MAE als metrics. Voorspellingshorizons: 96, 192, 336, 720. Ablatiestudies voor FEB vs. WEB en het effect van decompositie.

## Data & Techniek

### Gebruikte technieken
Frequency Enhanced Attention (Fourier en Wavelet varianten), Mixture of Experts decompositie, Discrete Fourier Transform (DFT), Discrete Wavelet Transform (DWT), Encoder-Decoder Transformer architectuur, PyTorch

### Inputdata
Multivariate tijdreeksdata, identiek aan de benchmarks van Informer en Autoformer. Tabelvorm met meerdere variabelen per tijdstip.

### Preprocessing
Standaard normalisatie. Chronologische train/val/test splits. De frequentietransformatie en decompositie zijn onderdeel van de modelarchitectuur.

### Preprocessing-problemen & oplossingen
Het probleem van kwadratische complexiteit bij lange sequenties wordt opgelost door over te schakelen naar het frequentiedomein waar slechts een beperkt aantal componenten nodig is. De keuze van het aantal geselecteerde frequentiecomponenten bepaalt de trade-off tussen efficiëntie en nauwkeurigheid.

### Datapipeline & modelinput
Invoer: tensor (batch, sequentielengte, features). De invoer wordt getransformeerd naar het frequentiedomein via FFT/DWT. Attention wordt berekend op sparse frequentierepresentaties. Decompositieblokken in elke laag scheiden trend en seizoenscomponenten. Output wordt teruggetransformeerd naar het tijddomein.

## Beperkingen
- De keuze tussen Fourier- en Wavelet-variant is dataset-afhankelijk en vereist experimentatie
- Het model veronderstelt dat tijdreeksen sparse zijn in het frequentiedomein, wat niet altijd geldt (bijv. bij sterk stochastische processen)
- Hogere implementatiecomplexiteit dan eenvoudiger modellen

## Gerelateerde bronnen
- [[zhou_2021_informer]] — eerdere efficiënte Transformer van dezelfde onderzoeksgroep
- [[wu_2021_autoformer]] — FEDformer bouwt direct voort op Autoformers decompositie-aanpak
- [[nie_2023_patchtst]] — alternatieve benadering die patches gebruikt in plaats van frequentiedomein
- [[zeng_2023_dlinear]] — stelt de noodzaak van complexe frequentie-attention in vraag

## Bronvermelding (APA 7e editie)
Zhou, T., Ma, Z., Wen, Q., Wang, X., Sun, L., & Jin, R. (2022). FEDformer: Frequency Enhanced Decomposed Transformer for Long-term Series Forecasting. *Proceedings of the 39th International Conference on Machine Learning (ICML)*, *162*, 27268-27286. https://arxiv.org/abs/2201.12740
