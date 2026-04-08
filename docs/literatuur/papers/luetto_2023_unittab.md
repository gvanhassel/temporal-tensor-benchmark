---
title: "One Transformer for All Time Series: Representing and Training with Time-Dependent Heterogeneous Tabular Data"
authors: ["Luetto, S.", "Garuti, F.", "Sangineto, E.", "Forni, L.", "Cucchiara, R."]
year: 2025
doi: "10.1007/s10994-025-06778-1"
journal: "Machine Learning"
open_access_url: "https://arxiv.org/abs/2302.06375"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, tabular, tijdreeksen, transformer, mixed-types, heterogeen, feature-tokenizer]
---

# One Transformer for All Time Series: Representing and Training with Time-Dependent Heterogeneous Tabular Data (UniTTab)

## Samenvatting
UniTTab is de meest directe oplossing voor ons probleem: het is een Transformer-architectuur die expliciet ontworpen is voor **tijdreeksen van heterogene tabulaire data** — rijen met gemixte numerieke en categorische features die over de tijd veranderen. Het model heeft twee niveaus: een **Field Transformer** die per rij (tijdstap) alle features tokeniseert en verwerkt, en een **Sequence Transformer** die de sequentie van rij-representaties over de tijd verwerkt. Numerieke waarden worden geëmbed via **frequentie-functies** (geïnspireerd door NeRF-coördinaat-embeddings), categorische waarden via standaard lookup-table embeddings. Het model wordt getraind met een **Masked Token** pretext-taak waarbij numerieke waarden worden gediscretiseerd (binned) als target, met neighborhood label smoothing om ordinaliteit te behouden.

## Sleutelconclusies
- **Twee-niveau architectuur**: Field Transformer (features binnen een rij) + Sequence Transformer (rijen over de tijd) — dit is precies de structuur die we nodig hebben
- Numerieke waarden worden geëmbed via frequentie-functies: `gamma(v) = (sin(2^0 * pi * v), cos(2^0 * pi * v), ..., sin(2^(L-1) * pi * v), cos(2^(L-1) * pi * v))` met L=8 → 16-dimensionale frequentie-vector → lineaire projectie naar d
- Categorische waarden via standaard lookup-table embeddings
- Rijen mogen **variabele structuur** hebben (verschillend aantal features per rij-type) — opgelost door per rij-type een projectiematrix
- Getraind met uniforme cross-entropy loss voor ALLE features (ook numerieke, via binning)

## Methodologie
Experimenten op 4 datasets: PKDD'99 (financiële transacties), Berka (banktransacties), Retail (e-commerce), en synthetische data. Vergelijking met TabTransformer, FT-Transformer, LSTM, GRU.

## Data & Techniek

### Gebruikte technieken
Twee-niveau Transformer (Field + Sequence), frequentie-gebaseerde numerieke embedding, Masked Token pretraining, neighborhood label smoothing.

### Inputdata
Tijdreeksen van tabulaire rijen: `s = [r_1, r_2, ..., r_t]` waarbij elke rij `r_i = [v_1, v_2, ..., v_k]` een mix van numerieke en categorische features bevat. **Long format concept op sequence-niveau, wide format op rij-niveau.**

### Preprocessing
- Numerieke waarden genormaliseerd
- Categorische waarden als indices
- Tijdstempels opgesplitst in categorische componenten (jaar, maand, dag)
- Geen speciale imputatie nodig

### Preprocessing-problemen & oplossingen
- **Heterogene rij-types** (bijv. verschillende transactietypes met verschillende kolommen): Opgelost door per rij-type een aparte projectiematrix `W_h ∈ R^(d*k_h x m)` die de variabele Field Transformer output projecteert naar een vaste dimensie m
- **Numerieke waarden als target**: Gediscretiseerd in bins voor cross-entropy training, met neighborhood label smoothing (range R = {b-5, ..., b+5}) om ordinaliteit te behouden

### Datapipeline & modelinput
**Concrete architectuur:**

**Stap 1 — Feature Embedding per rij:**
- Numerieke feature j: `emb_j = Linear(gamma(v_j))` waarbij gamma de frequentie-encoding is (16-dim → d-dim)
- Categorische feature j: `emb_j = LookupTable(v_j) ∈ R^d`
- Resultaat per rij: k embeddings van dimensie d

**Stap 2 — Field Transformer (per rij):**
- Input: k feature-embeddings `∈ R^(k x d)`
- 1 Transformer-laag met 8 attention-heads
- Output: k contextuele embeddings → geconcateneerd tot `g ∈ R^(d*k)`

**Stap 3 — Rij-type projectie:**
- Als rij van type h met k_h features: `W_h * g ∈ R^m` (projectie naar vaste dimensie m)
- Dit maakt variabele rij-structuren mogelijk!

**Stap 4 — Sequence Transformer (over de tijd):**
- Input: t rij-representaties `∈ R^(t x m)`
- 12 Transformer-lagen met 12 attention-heads
- Output: t contextuele embeddings `z_1, ..., z_t ∈ R^(t x d)`

**Tensorshape overzicht:**
```
Ruwe input:           (subject, t rijen, variabel k_h features per rij)
Na feature embedding: (subject, t rijen, k features, d dimensie)
Na Field Transformer: (subject, t rijen, d*k dimensie)
Na rij-projectie:     (subject, t rijen, m dimensie)    — VAST formaat
Na Seq Transformer:   (subject, t rijen, d dimensie)
```

**CRUCIAAL INZICHT VOOR ONS PROJECT:**
UniTTab is het meest direct relevante model:
1. Het combineert **mixed types** (numeriek + categorisch) via feature tokenisatie
2. Het verwerkt **temporele sequenties** van tabulaire rijen
3. Het ondersteunt **variabele rij-structuren** (precies ons probleem met events die op sommige tijdstappen wel/niet voorkomen)
4. De twee-niveau architectuur (features → temporeel) kan direct worden toegepast op ons subject × tijd × features probleem

## Beperkingen
- Rijen moeten in een vaste volgorde (chronologisch) staan — geen continue tijdsrepresentatie
- Discretisatie van numerieke targets voor training is een compromis
- 12-lagen Sequence Transformer is computationeel zwaar
- Nog geen expliciete event-representatie (events moeten als features in rijen worden opgenomen)

## Gerelateerde bronnen
- [[gorishniy_2021_ft_transformer]] — feature tokenisatie basis (zonder temporele component)
- [[huang_2020_tabtransformer]] — alleen categorische tokenisatie
- [[tipirneni_2022_strats]] — triplet-representatie als alternatief voor rij-gebaseerde aanpak
- [[nie_2022_patchtst]] — temporele Transformer maar zonder mixed types
- [[gorishniy_2022_numerical_embeddings]] — verbeterde numerieke embeddings

## Bronvermelding (APA 7e editie)
Luetto, S., Garuti, F., Sangineto, E., Forni, L., & Cucchiara, R. (2025). One transformer for all time series: Representing and training with time-dependent heterogeneous tabular data. *Machine Learning*. https://doi.org/10.1007/s10994-025-06778-1
