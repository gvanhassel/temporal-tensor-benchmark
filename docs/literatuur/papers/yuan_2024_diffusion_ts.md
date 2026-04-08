---
title: "Diffusion-TS: Interpretable Diffusion for General Time Series Generation"
authors: ["Yuan, X.", "Qiao, Y."]
year: 2024
doi: "10.48550/arXiv.2403.01742"
journal: "International Conference on Learning Representations (ICLR 2024)"
open_access_url: "https://arxiv.org/abs/2403.01742"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, diffusie, tijdreeksen, synthetische-data, transformer, interpreteerbaarheid]
---

# Diffusion-TS: Interpretable Diffusion for General Time Series Generation

## Samenvatting
Diffusion-TS is een niet-autoregressief diffusiemodel voor het genereren van hoogwaardige synthetische tijdreeksen. Het model introduceert een transformer-gebaseerde architectuur die een ontlede (disentangled) seizoens-trend representatie van tijdreeksen leert. De decoder gebruikt een meerlaagse structuur waarin elk blok een transformer-blok, een feedforward-netwerk en interpreteerbare lagen (Trend- en Fourier-synthese laag) bevat. Door een Fourier-gebaseerde loss te gebruiken in plaats van ruis-reconstructie in elke diffusiestap, genereert het model nauwkeurigere tijdreeksen. Diffusion-TS overtreft eerdere methoden (waaronder TimeGAN en DoppelGANger) met een significante marge.

## Sleutelconclusies
- Diffusiemodellen overtreffen GAN-gebaseerde methoden voor tijdreeksgeneratie
- Het ontleden van tijdreeksen in trend- en seizoenscomponenten binnen het generatieve model verbetert zowel kwaliteit als interpreteerbaarheid
- Fourier-gebaseerde loss is effectiever dan standaard ruis-reconstructie voor temporele data

## Methodologie
Non-autoregressief diffusiemodel met transformer-encoder en decomposition-decoder. De decoder ontleedt elke tijdreeks in een trendcomponent (via polynomiale regressie) en seizoenscomponenten (via Fourier-synthese). Training via een diffusieproces met Fourier-gebaseerde reconstructie-loss. Evaluatie op standaard benchmarks (aandelen, energie, MuJoCo) met vergelijking tegen TimeGAN, RCGAN, C-RNN-GAN, TimeVAE, GT-GAN en Cot-GAN.

## Data & Techniek

### Gebruikte technieken
Denoising Diffusion Probabilistic Model (DDPM), Transformer-encoder, seizoens-trend decompositie, Fourier-synthese, polynomiale trendmodellering.

### Inputdata
Benchmarkdatasets: aandelenkoersen (6 features, 24 tijdstappen), energieverbruik (28 features, 24 tijdstappen), MuJoCo fysica-simulatie (14 features, variabele lengte). Multivariate tijdreeksen.

### Preprocessing
Min-max normalisatie, segmentatie in vensters van vaste lengte, standaard train/test-splitsingen conform eerdere werken (TimeGAN).

### Preprocessing-problemen & oplossingen
Het probleem van het vastleggen van zowel lokale als globale temporele patronen werd opgelost door de decompositie-architectuur die trend en seizoenaliteit expliciet scheidt.

### Datapipeline & modelinput
Genormaliseerde tijdreeksvensters (T x D tensor) -> ruis toevoegen via forward diffusion -> transformer-encoder verwerkt verruiste input -> decomposition-decoder reconstrueert trend + seizoenaliteit -> Fourier-loss optimaliseert reconstructie.

## Beperkingen
- Computationeel duurder dan GAN-methoden door het iteratieve diffusieproces
- Vaste vensterlengte; geen ondersteuning voor variabele-lengte generatie
- De decompositie veronderstelt dat trend en seizoenaliteit de dominante componenten zijn; chaotische of stochastische patronen worden minder goed gevangen
- Relatief nieuw; minder uitgebreid gevalideerd dan TimeGAN

## Gerelateerde bronnen
- [[yoon_2019_timegan]] — TimeGAN is een van de baselines die Diffusion-TS overtreft
- [[lin_2020_doppelganger]] — DoppelGANger is een andere baseline
- [[kang_2020_gratis]] — GRATIS biedt controleerbare generatie via een ander paradigma (MAR)
- [[ismail_fawaz_2019_dl_tsc_review]] — transformer-architecturen voor tijdreeksen bouwen voort op deze review

## Bronvermelding (APA 7e editie)
Yuan, X., & Qiao, Y. (2024). Diffusion-TS: Interpretable Diffusion for General Time Series Generation. In *Proceedings of the International Conference on Learning Representations (ICLR 2024)*. https://arxiv.org/abs/2403.01742
