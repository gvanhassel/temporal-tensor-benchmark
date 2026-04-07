---
title: "A Time Series is Worth 64 Words: Long-term Forecasting with Transformers"
authors: ["Nie, Y.", "Nguyen, N. H.", "Sinthong, P.", "Kalagnanam, J."]
year: 2023
doi: "10.48550/arXiv.2211.14730"
journal: "Proceedings of the International Conference on Learning Representations (ICLR)"
open_access_url: "https://arxiv.org/pdf/2211.14730"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, transformer, tijdreeksen, patching, channel-independence, self-supervised]
---

# A Time Series is Worth 64 Words: Long-term Forecasting with Transformers

## Samenvatting
Nie et al. introduceren PatchTST, een Transformer-model dat twee kernprincipes toepast op tijdreeksvoorspelling: (1) patching -- het segmenteren van de tijdreeks in sub-series (patches) van vaste lengte die als tokens dienen, analoog aan woorden in NLP -- en (2) channel-independence -- elke variabele wordt onafhankelijk verwerkt door dezelfde Transformer. Patching biedt drie voordelen: lokale semantische informatie blijft behouden in de embedding, de rekentijd en geheugengebruik dalen kwadratisch bij hetzelfde look-back window, en het model kan een langere historie verwerken. PatchTST behaalt state-of-the-art resultaten op lange-termijn voorspellingsbenchmarks en presteert ook uitstekend bij self-supervised pre-training met masked patch prediction, vergelijkbaar met BERT voor tijdreeksen. Transfer learning tussen datasets is succesvol aangetoond.

## Sleutelconclusies
- Patching is effectiever dan punt-niveau tokenisatie: het behoudt lokale temporele informatie en reduceert de sequentielengte drastisch
- Channel-independence (elke variabele apart verwerken) presteert verrassend beter dan multivariate modellen die cross-variabele afhankelijkheden modelleren
- Self-supervised pre-training via masked patch prediction maakt effectief transfer learning mogelijk tussen tijdreeksdatasets

## Methodologie
Evaluatie op acht benchmarkdatasets: ETTh1, ETTh2, ETTm1, ETTm2, Weather, Electricity, Traffic, ILI. Vergelijking met Informer, Autoformer, FEDformer, DLinear, en andere Transformer-varianten. MSE en MAE als metrics. Voorspellingshorizons: 96, 192, 336, 720. Aanvullende experimenten met self-supervised pre-training en transfer learning.

## Data & Techniek

### Gebruikte technieken
Patch Embedding (sub-series segmentatie), Channel-Independent processing, Vanilla Transformer Encoder (geen decoder nodig), Masked Patch Prediction (self-supervised pre-training), Instance Normalization (RevIN), PyTorch

### Inputdata
Multivariate tijdreeksdata in tabelvorm. Elke variabele wordt als onafhankelijk univariaat kanaal behandeld. Look-back windows tot 512 tijdstappen. Datasets variëren van uurlijks tot 15-minuten granulariteit.

### Preprocessing
Instance normalization (RevIN) voor het normaliseren per sample. Patching: de invoersequentie wordt opgedeeld in niet-overlappende of overlappende patches van vaste lengte (typisch 16 tijdstappen). Elke patch wordt lineair geprojecteerd naar de model-dimensie. Chronologische train/val/test splits.

### Preprocessing-problemen & oplossingen
Het probleem van te lange token-sequenties wordt opgelost door patching: een invoer van 512 tijdstappen met patchlengte 16 resulteert in slechts 32 tokens. Channel-independence voorkomt het probleem van spurieuze cross-variabele correlaties die multivariate modellen kunnen misleiden.

### Datapipeline & modelinput
Invoer per kanaal: tensor (batch, 1, sequentielengte) -> patching -> (batch, aantal_patches, patch_embedding_dim) -> Transformer Encoder -> lineaire projectie naar voorspellingshorizon. Alle kanalen delen dezelfde Transformer-parameters. Finale output: (batch, aantal_variabelen, voorspellingshorizon).

## Beperkingen
- Channel-independence negeert mogelijk waardevolle cross-variabele afhankelijkheden die in sommige domeinen cruciaal zijn
- De patchlengte is een hyperparameter die de granulariteit van de informatie-extractie bepaalt
- Self-supervised pre-training vereist voldoende ongelabelde data en de effectiviteit hangt af van de gelijkenis tussen pre-training en downstream datasets

## Gerelateerde bronnen
- [[zhou_2021_informer]] — PatchTST verbetert op Informer's efficiëntie via patching in plaats van sparse attention
- [[wu_2021_autoformer]] — PatchTST overtreft Autoformer zonder decompositie of auto-correlatie
- [[zhou_2022_fedformer]] — PatchTST behaalt betere resultaten met een eenvoudiger architectuur
- [[zhang_2023_crossformer]] — tegenovergestelde ontwerpkeuze: Crossformer modelleert juist cross-dimensie afhankelijkheden
- [[zeng_2023_dlinear]] — PatchTST weerlegt deels DLinear's kritiek door te tonen dat Transformers met de juiste aanpak wel effectief zijn

## Bronvermelding (APA 7e editie)
Nie, Y., Nguyen, N. H., Sinthong, P., & Kalagnanam, J. (2023). A Time Series is Worth 64 Words: Long-term Forecasting with Transformers. *Proceedings of the International Conference on Learning Representations (ICLR 2023)*. https://arxiv.org/abs/2211.14730
