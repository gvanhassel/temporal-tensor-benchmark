---
title: "Are Transformers Effective for Time Series Forecasting?"
authors: ["Zeng, A.", "Chen, M.", "Zhang, L.", "Xu, Q."]
year: 2023
doi: "10.1609/aaai.v37i9.26317"
journal: "Proceedings of the AAAI Conference on Artificial Intelligence"
open_access_url: "https://arxiv.org/pdf/2205.13504"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, transformer, tijdreeksen, lineair-model, kritiek, DLinear]
---

# Are Transformers Effective for Time Series Forecasting?

## Samenvatting
Zeng et al. stellen een fundamentele vraag: zijn Transformers werkelijk effectief voor tijdreeksvoorspelling? De auteurs betogen dat het permutation-invariante karakter van self-attention inherent leidt tot verlies van temporele ordening-informatie, zelfs met positional encoding. Ze tonen aan dat de verbeterde prestaties van recente Transformer-modellen (Informer, Autoformer, FEDformer) niet voortkomen uit het attention-mechanisme zelf, maar uit de Direct Multi-Step (DMS) voorspellingsstrategie. Als bewijs introduceren ze LTSF-Linear: een set van extreem eenvoudige modellen, waaronder DLinear (decompositie + twee enkellaagse lineaire netwerken) en NLinear (normalisatie + één lineaire laag). Verrassend genoeg overtreffen deze simpele lineaire modellen de complexe Transformer-varianten op negen benchmarkdatasets. Dit resultaat dwingt het veld om de rol van Transformers in tijdreeksanalyse te heroverwegen.

## Sleutelconclusies
- Self-attention is permutation-invariant en verliest inherent temporele ordening, waardoor het fundamenteel minder geschikt is voor tijdreeksen dan voor NLP
- De betere prestaties van Transformer-modellen zijn grotendeels toe te schrijven aan de DMS-strategie, niet aan het attention-mechanisme
- Een simpel lineair model (DLinear) met seizoen-trend decompositie overtreft complexe Transformer-architecturen, wat wijst op mogelijke overfitting of architecturale mismatch

## Methodologie
Evaluatie op negen benchmarkdatasets: ETTh1, ETTh2, ETTm1, ETTm2, Weather, Electricity, Traffic, Exchange-Rate, ILI. Vergelijking met Informer, Autoformer, FEDformer, Pyraformer, LogTrans. MSE en MAE als metrics. Voorspellingshorizons: 96, 192, 336, 720. Uitgebreide ablatiestudies en analyse van temporal attention patronen.

## Data & Techniek

### Gebruikte technieken
DLinear: Moving Average decompositie + twee enkellaagse lineaire netwerken (één voor trend, één voor seizoen). NLinear: Normalisatie (laatste waarde aftrekken) + één lineaire laag. Geen attention, geen niet-lineariteit (bij NLinear), geen complexe architectuur. Vergelijkende analyse van attention maps in Transformer-modellen.

### Inputdata
Multivariate tijdreeksdata in tabelvorm, identiek aan de standaard benchmarks. Negen datasets met variërende granulariteit en aantal variabelen.

### Preprocessing
Standaard normalisatie. Voor DLinear: moving average kernel voor trend-seizoen decompositie (vergelijkbaar met Autoformer). Voor NLinear: aftrekken van de laatste waarde in het invoerwindow (distributieschifting tegengaan). Chronologische train/val/test splits.

### Preprocessing-problemen & oplossingen
Distributieverschuiving (distribution shift) in tijdreeksen wordt aangepakt door NLinear's normalisatie-truc. Het probleem van temporeel informatieverlies in Transformers wordt niet opgelost maar geïdentificeerd als fundamentele beperking.

### Datapipeline & modelinput
DLinear invoer: tensor (batch, sequentielengte, features) -> moving average -> trend (batch, sequentielengte, features) + seizoen (batch, sequentielengte, features) -> twee lineaire lagen -> som -> output (batch, voorspellingshorizon, features). NLinear: invoer - laatste waarde -> lineaire laag -> + laatste waarde -> output.

## Beperkingen
- De lineaire modellen missen het vermogen om complexe niet-lineaire patronen te vangen
- De analyse richt zich op standaard voorspellingsbenchmarks; andere tijdreekstaken (classificatie, anomaliedetectie) zijn niet onderzocht
- Latere papers (PatchTST) tonen aan dat Transformers met de juiste aanpak (patching) wel degelijk effectief kunnen zijn, wat de generaliseerbaarheid van de conclusies nuanceert
- De vergelijking is beperkt tot de toenmalige Transformer-varianten

## Gerelateerde bronnen
- [[zhou_2021_informer]] — een van de Transformer-modellen die DLinear overtreft
- [[wu_2021_autoformer]] — DLinear leent de decompositie-aanpak van Autoformer
- [[zhou_2022_fedformer]] — een van de Transformer-modellen die DLinear overtreft
- [[nie_2023_patchtst]] — weerlegging: PatchTST toont dat Transformers met patching wel effectief zijn
- [[zhang_2023_crossformer]] — Crossformer's cross-dimensie benadering staat ook ter discussie door DLinear's channel-independence resultaten

## Bronvermelding (APA 7e editie)
Zeng, A., Chen, M., Zhang, L., & Xu, Q. (2023). Are Transformers Effective for Time Series Forecasting? *Proceedings of the AAAI Conference on Artificial Intelligence*, *37*(9), 11121-11128. https://doi.org/10.1609/aaai.v37i9.26317
