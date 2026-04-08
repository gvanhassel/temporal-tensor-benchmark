---
title: "Self-Supervised Transformer for Sparse and Irregularly Sampled Multivariate Clinical Time-Series"
authors: ["Tipirneni, S.", "Reddy, C. K."]
year: 2022
doi: "10.1145/3516367"
journal: "ACM Transactions on Knowledge Discovery from Data"
open_access_url: "https://arxiv.org/abs/2107.14293"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, klinisch, transformer, triplet-representatie, onregelmatig, mixed-types, self-supervised]
---

# Self-Supervised Transformer for Sparse and Irregularly Sampled Multivariate Clinical Time-Series (STraTS)

## Samenvatting
STraTS introduceert een fundamenteel andere benadering van multivariate tijdreeksrepresentatie: in plaats van de traditionele dense matrix `(T x D)` met imputatie voor ontbrekende waarden, wordt elke tijdreeks gerepresenteerd als een **verzameling observatie-triplets** `(tijdstip, variabele, waarde)`. Een nieuwe Continuous Value Embedding (CVE) techniek embedt continue waarden (zowel tijd als meetwaarden) zonder discretisatie via een geleerd feedforward-netwerk. De Transformer verwerkt deze triplet-embeddings als een set (niet als sequentie), waardoor onregelmatige sampling en sparse data native worden ondersteund. Self-supervised pretraining via tijdreeksvoorspelling als proxy-taak verbetert prestaties bij gelimiteerde labels.

## Sleutelconclusies
- **Triplet-representatie** `(t, f, v)` is superieur aan dense matrix-representatie voor sparse, onregelmatige klinische data
- **Continuous Value Embedding** (CVE) vermijdt discretisatie/binning van continue waarden — essentieel voor tijd en meetwaarden
- Set-gebaseerde verwerking (niet volgorde-afhankelijk) elimineert de noodzaak van imputatie
- Self-supervised pretraining verbetert voorspellingen bij beperkte labels significant
- 89.7% missing rate in MIMIC-III data — traditionele matrix-aanpak verspilt enorm veel geheugen aan nullen

## Methodologie
Experimenten op MIMIC-III en PhysioNet Challenge 2012 datasets. Mortaliteitsvoorspelling en klinische outcome-voorspelling. 129 variabelen uit input/output events, lab events, chart events en prescripties. Vergelijking met GRU-D, SeFT, mTAND, IP-Nets.

## Data & Techniek

### Gebruikte technieken
Transformer met multi-head self-attention, Continuous Value Embedding (CVE), self-supervised forecasting pretraining.

### Inputdata
Klinische tijdreeksdata in **long/triplet format**: elke observatie is een triplet `(t_i, f_i, v_i)` waarbij:
- `t_i ∈ R≥0` = continue tijdstempel
- `f_i ∈ F` = categorische variabele-identifier (welke meting)
- `v_i ∈ R` = continue meetwaarde

### Preprocessing
- MIMIC-III: 129 variabelen geextraheerd uit chart events, lab events, input/output events, prescripties
- Eerste 24 uur van ICU-verblijf
- Geen tijdsdiscretisatie of imputatie nodig — dat is het hele punt
- Demografische features apart verwerkt

### Preprocessing-problemen & oplossingen
- **Extreme sparsiteit (89.7% missing)**: Opgelost door triplet-representatie — alleen geobserveerde waarden worden opgeslagen
- **Onregelmatige sampling**: Opgelost door continue tijdsembedding (CVE) in plaats van vaste tijdsgrid
- **Mixed meettypen**: Alle variabelen behandeld als (identifier, waarde) paren

### Datapipeline & modelinput
**Concrete embedding-formules:**

**Continuous Value Embedding (CVE):**
```
FFN(x) = U * tanh(W*x + b)
```
Met: W ∈ R^(1 x floor(sqrt(d))), b ∈ R^floor(sqrt(d)), U ∈ R^(floor(sqrt(d)) x d)
Input: enkele scalaire waarde → Output: d-dimensionale embedding

**Triplet-embedding per observatie:**
```
e_i = e_i^f + e_i^v + e_i^t
```
Waarbij:
- `e_i^f = LookupTable(f_i) ∈ R^d` — categorische embedding voor variabele-type
- `e_i^v = CVE_v(v_i) ∈ R^d` — continue embedding voor meetwaarde
- `e_i^t = CVE_t(t_i) ∈ R^d` — continue embedding voor tijdstip

**Tensorshape naar Transformer:**
```
E ∈ R^(n x d)  — n observatie-triplets, d embedding-dimensie
```
Na Transformer: `C ∈ R^(n x d)` (contextuele embeddings)

**Demografische features:**
```
e^d = tanh(W_2 * tanh(W_1 * d + b_1) + b_2) ∈ R^d
```
Apart verwerkt via twee-laags FFN, geconcateneerd aan het einde.

**CRUCIAAL INZICHT VOOR ONS PROJECT:**
Dit is de meest relevante architectuur voor ons probleem. De triplet-representatie `(t, f, v)` lost precies ons mixed-types probleem op:
- **Events** (aangifte doen, te laat betalen): triplet `(tijdstip, "event_aangifte", 1.0)` of `(tijdstip, "event_te_laat", 1.0)`
- **Numerieke waarden** (omzet): triplet `(tijdstip, "omzet", 150000.0)`
- **Categorische waarden** (sector): kunnen als aparte lookup-embedding naast de triplet worden verwerkt

De variabele-identifier `f` fungeert als een feature-type token, en de CVE-embedding van de waarde `v` werkt voor zowel 0/1 event-indicatoren als continue numerieke waarden. Er is geen wide-format tensor nodig — het aantal observaties per tijdstap is variabel.

## Beperkingen
- Transformer-geheugen schaalt kwadratisch met het aantal observaties n
- Bij zeer lange histories (veel events) moet truncatie of windowing worden toegepast
- Alle meetwaarden worden als scalaire continue waarden behandeld — multi-categorische features (bijv. sector met 20 opties) zijn niet direct ondersteund als waarde
- Geen hierarchische structuur (bezoeken/episodes) — alle triplets zijn vlak

## Gerelateerde bronnen
- [[shukla_2021_mtan]] — vergelijkbare aanpak met time-attention voor onregelmatige tijdreeksen
- [[lee_2026_star_set_transformer]] — vernieuwing van STraTS met temporal en variable-type attention biases
- [[wang_2020_mimic_extract]] — MIMIC-III preprocessing pipeline die wide-format produceert
- [[gorishniy_2021_ft_transformer]] — feature tokenisatie voor mixed tabular data (zonder temporele component)
- [[choi_2016_retain]] — EHR-model met multi-hot encoding (wide format)

## Bronvermelding (APA 7e editie)
Tipirneni, S., & Reddy, C. K. (2022). Self-supervised transformer for sparse and irregularly sampled multivariate clinical time-series. *ACM Transactions on Knowledge Discovery from Data*, *16*(6), 1-20. https://doi.org/10.1145/3516367
