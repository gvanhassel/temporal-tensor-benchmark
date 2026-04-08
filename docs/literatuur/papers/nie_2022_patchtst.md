---
title: "A Time Series is Worth 64 Words: Long-term Forecasting with Transformers"
authors: ["Nie, Y.", "Nguyen, N. H.", "Sinthong, P.", "Kalagnanam, J."]
year: 2023
doi: ""
journal: "ICLR 2023"
open_access_url: "https://arxiv.org/abs/2211.14730"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, tijdreeksen, transformer, channel-independent, patching]
---

# A Time Series is Worth 64 Words: Long-term Forecasting with Transformers (PatchTST)

## Samenvatting
PatchTST introduceert twee kernconcepten voor tijdreeks-transformers: (1) **patching** — het opdelen van tijdreeksen in subseries-level patches die als tokens dienen, en (2) **channel-independence** — elke variabele (channel) wordt als aparte univariate tijdreeks verwerkt door dezelfde gedeelde Transformer-backbone. Het patchingmechanisme reduceert het aantal tokens van L naar ~L/S (waarbij S de stride is), waardoor de kwadratische complexiteit van self-attention sterk afneemt. Experimenten tonen aan dat deze eenvoudige architectuur state-of-the-art presteert op lange-termijnvoorspelling en dat channel-independence verrassend effectief is.

## Sleutelconclusies
- Channel-independence (elke variabele apart verwerken met gedeelde weights) presteert beter dan channel-mixing voor lange-termijnvoorspelling
- Patching behoudt lokale semantische informatie en reduceert rekentijd kwadratisch
- Het model kan langere historische vensters verwerken dankzij de tokenreductie door patching

## Methodologie
Experimenten op 8 populaire lange-termijnvoorspelling-benchmarks (ETTh1/h2, ETTm1/m2, Weather, Electricity, Traffic, ILI). Vergelijking met Informer, Autoformer, FEDformer en andere Transformer-varianten. Ablatiestudies over channel-independence vs. channel-mixing en overlap vs. non-overlap patching.

## Data & Techniek

### Gebruikte technieken
Transformer encoder met self-attention, lineaire projectie van patches naar embedding-ruimte, instance normalization per channel.

### Inputdata
Multivariate tijdreeksen in **wide format**: tensor van shape `(batch, M kanalen, L tijdstappen)`. Elke dataset bevat numerieke waarden op regelmatige tijdsintervallen.

### Preprocessing
Instance normalization (RevIN) per channel. Geen speciale behandeling van categorische data — PatchTST is ontworpen voor puur numerieke multivariate tijdreeksen.

### Preprocessing-problemen & oplossingen
_Niet vermeld_ — het model gaat uit van regelmatige, volledig geobserveerde numerieke tijdreeksen.

### Datapipeline & modelinput
**Concrete tensorshapes:**
1. Input: `(B, M, L)` — batch x kanalen x lookback-venster
2. Na patching: `(B, M, P, N)` — patches van lengte P, N patches per kanaal
3. Reshape voor Transformer: `(B*M, N, P)` — kanalen worden als extra batch-items behandeld
4. Na lineaire embedding: `(B*M, N, D)` — D = latente dimensie
5. Positie-encoding: `W_pos ∈ R^(D x N)` wordt opgeteld
6. Na Transformer encoder: `(B*M, N, D)`
7. Flatten + lineaire projectie naar voorspelling: `(B*M, T)` → reshape naar `(B, M, T)`

**Cruciaal inzicht voor ons project:** PatchTST gaat uit van **puur wide format** met alleen numerieke kanalen. Het model kan niet direct omgaan met mixed types (events + numeriek + categorisch). Elke feature is een apart kanaal met dezelfde tijdsas.

## Beperkingen
- Alleen geschikt voor regelmatige, numerieke tijdreeksen
- Geen ondersteuning voor categorische variabelen of events
- Channel-independence verliest inter-variabele correlaties (Crossformer lost dit op)
- Niet geschikt voor onregelmatig gesamplde data

## Gerelateerde bronnen
- [[zhang_2023_crossformer]] — channel-dependent alternatief met two-stage attention
- [[zhou_2021_informer]] — eerdere Transformer voor lange tijdreeksen zonder patching
- [[gorishniy_2021_ft_transformer]] — tokenisatie-aanpak voor mixed tabular features
- [[luetto_2023_unittab]] — combineert tabular tokenisatie met temporele transformers

## Bronvermelding (APA 7e editie)
Nie, Y., Nguyen, N. H., Sinthong, P., & Kalagnanam, J. (2023). A time series is worth 64 words: Long-term forecasting with transformers. *ICLR 2023*. https://arxiv.org/abs/2211.14730
