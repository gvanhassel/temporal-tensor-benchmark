---
title: "Structure-Aware Set Transformers: Temporal and Variable-Type Attention Biases for Asynchronous Clinical Time Series"
authors: ["Lee, J.", "Lee, K.", "Kim, C.", "Yang, E."]
year: 2026
doi: ""
journal: "arXiv preprint"
open_access_url: "https://arxiv.org/abs/2603.06605"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, klinisch, transformer, set-representatie, attention-bias, variabele-type, onregelmatig]
---

# Structure-Aware Set Transformers: Temporal and Variable-Type Attention Biases for Asynchronous Clinical Time Series (STAR)

## Samenvatting
STAR bouwt voort op de set-gebaseerde tokenisatie van STraTS maar voegt twee parameter-efficiente **soft attention biases** toe: (1) een **temporele locality penalty** `-|Delta_t|/tau` met leerbare tijdschaal tau, die temporeel nabije observaties begunstigt, en (2) een **variable-type affinity matrix** `B_{s_i, s_j}` die leert welke variabele-types sterke interacties hebben. Dit herstelt structurele priors die verloren gaan bij pure set-representatie, zonder terug te vallen op discretisatie of imputatie.

## Sleutelconclusies
- Set-gebaseerde tokenisatie (triplets) is flexibel maar verliest structurele informatie — STAR herstelt dit via attention biases
- Temporele bias: observaties dichtbij in de tijd krijgen hogere attention-gewichten
- Variable-type bias: bepaalde variabele-types (bijv. bloeddruk en hartslag) leren sterkere onderlinge interacties
- De biases worden op verschillende diepten in de Transformer ingevoegd — layer-fusion strategieën zijn onderzocht
- Consistente verbeteringen op meerdere ICU-voorspellingstaken versus grid- en set-baselines

## Methodologie
Experimenten op meerdere ICU-datasets. Vergelijking met grid-gebaseerde baselines (MIMIC-Extract stijl) en set-gebaseerde baselines (STraTS stijl). Ablatiestudies over temporal bias vs. variable-type bias vs. beide.

## Data & Techniek

### Gebruikte technieken
Set Transformer met soft attention biases, leerbare tijdschaalparameter, leerbare type-compatibiliteitsmatrix.

### Inputdata
Klinische observaties als **set van triplets** `(tijdstip, variabele-type, waarde)` — zelfde format als STraTS.

### Preprocessing
Vergelijkbaar met STraTS: geen discretisatie, geen imputatie. Observaties als triplets opgeslagen.

### Preprocessing-problemen & oplossingen
- **Verlies van structurele informatie bij set-representatie**: Opgelost door attention biases
- **Geen expliciete temporele nabijheid**: Opgelost door temporele penalty

### Datapipeline & modelinput
**Concrete attention-bias formules:**

**Temporele bias:**
```
temporal_bias(i, j) = -|t_i - t_j| / tau
```
Met leerbare tau per attention-head of laag.

**Variable-type bias:**
```
type_bias(i, j) = B[s_i, s_j]
```
Met B een leerbare matrix van dimensie `|variabele-types| x |variabele-types|`.

**Gecombineerde attention:**
```
attention(i, j) = softmax(Q_i * K_j^T / sqrt(d) + temporal_bias(i,j) + type_bias(i,j))
```

**Tensorshape:**
Zelfde als STraTS: `(n observaties x d embedding-dimensie)` als set, met n variabel per patiënt.

**Relevantie voor ons project:** STAR verbetert de STraTS-aanpak door structurele informatie terug te brengen via attention biases. Voor ons project betekent dit dat we de triplet-representatie kunnen gebruiken EN toch informatie coderen over:
1. Welke events/features temporeel nabij zijn (temporele bias)
2. Welke features inherent gerelateerd zijn (bijv. omzet en werknemers, of aangifte en te-laat-betalen) via de variable-type matrix

## Beperkingen
- Zeer recent (2026) — nog niet breed gevalideerd
- De variable-type matrix schaalt kwadratisch met het aantal variabele-types
- Nog geen gepubliceerde code beschikbaar
- Voornamelijk getest op klinische data

## Gerelateerde bronnen
- [[tipirneni_2022_strats]] — basis set/triplet-representatie waarop STAR voortbouwt
- [[shukla_2021_mtan]] — vergelijkbare continue-tijdsaanpak met attention
- [[wang_2020_mimic_extract]] — grid-gebaseerde baseline waartegen STAR wordt vergeleken

## Bronvermelding (APA 7e editie)
Lee, J., Lee, K., Kim, C., & Yang, E. (2026). Structure-aware set transformers: Temporal and variable-type attention biases for asynchronous clinical time series. *arXiv preprint arXiv:2603.06605*. https://arxiv.org/abs/2603.06605
