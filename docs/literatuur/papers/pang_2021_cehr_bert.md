---
title: "CEHR-BERT: Incorporating Temporal Information from Structured EHR Data to Improve Prediction Tasks"
authors: ["Pang, C.", "Jiang, X.", "Kalluri, K. S.", "Spotnitz, M.", "Chen, R.", "Perotte, A.", "Natarajan, K."]
year: 2021
doi: ""
journal: "Machine Learning for Health (ML4H) 2021, PMLR"
open_access_url: "https://arxiv.org/abs/2111.08585"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, EHR, BERT, temporeel, artificiële-tijd-tokens, multi-domein]
---

# CEHR-BERT: Incorporating Temporal Information from Structured EHR Data to Improve Prediction Tasks

## Samenvatting
CEHR-BERT verbetert klinische BERT-modellen door **artificiële tijd-tokens (ATT)** toe te voegen aan de input-sequentie. Deze tokens coderen het tijdsinterval tussen opeenvolgende bezoeken als discrete categorieën: W_0-W_3 (weken), M_1-M_11 (maanden), of LT (lang termijn, >1 jaar). Daarnaast combineert het model **concept embeddings** (medische codes), **tijds-embeddings** en **leeftijds-embeddings** via concatenatie en een fully-connected laag tot een temporele concept-embedding. Het model verwerkt meerdere klinische domeinen (diagnoses, medicaties, procedures) in één sequentie.

## Sleutelconclusies
- **Artificiële Tijd-Tokens** (ATT) coderen tijdsintervallen als discrete categorieën (W_n, M_n, LT) en worden als gewone tokens in de sequentie ingevoegd
- **Multi-domein**: Verwerkt diagnoses, medicaties EN procedures in één sequentie (in tegenstelling tot BEHRT dat alleen diagnoses gebruikt)
- **Visit Start/End tokens** (VS/VE) definiëren bezoekgrenzen — alle codes binnen een bezoek zitten tussen VS en VE
- Concatenatie van concept + tijd + leeftijd embeddings → FC-laag → temporele embedding
- Tweede leerdoelstelling: bezoek-type voorspelling naast masked language modeling

## Methodologie
Experimenten op Columbia University Irving Medical Center data: 2.4M patiënten, >30 jaar aan data. 4 voorspellingstaken. Vergelijking met Med-BERT, BEHRT, en baseline modellen.

## Data & Techniek

### Gebruikte technieken
BERT met artificiële tijd-tokens, multi-domein concept embeddings, visit-type prediction als tweede pretraining-taak.

### Inputdata
Sequenties van medische concepten met bezoekstructuur in **tokenized long format met tijd-tokens**.

### Preprocessing
- Medische codes uit meerdere domeinen (diagnoses, medicaties, procedures)
- Tijdsintervallen gediscretiseerd in ATT-categorieën
- Bezoekgrenzen gemarkeerd met VS/VE tokens

### Preprocessing-problemen & oplossingen
- **Geen temporele informatie in standaard BERT**: Opgelost door ATT-tokens in de sequentie in te voegen
- **Multi-domein codes**: Alle concepten in één vocabulaire samengevoegd
- **Variabele bezoekintervallen**: Gediscretiseerd in W_n/M_n/LT categorieën

### Datapipeline & modelinput
**Concrete input-sequentie:**
```
[VS] [concept_1] [concept_2] ... [VE] [ATT: W_2] [VS] [concept_3] ... [VE] [ATT: M_3] [VS] ...
```

Waarbij:
- VS = Visit Start token
- VE = Visit End token
- ATT: W_n = week-interval (n=0-3, <28 dagen)
- ATT: M_n = maand-interval (n=1-11, 28-365 dagen)
- ATT: LT = lang termijn (>365 dagen)

**Embedding-formule:**
```
temporal_concept_emb = FC(concat(concept_emb, time_emb, age_emb))
```

Drie embeddings worden geconcateneerd en door een fully-connected laag geprojecteerd.

**Relevantie voor ons project:** De ATT-aanpak is direct toepasbaar op ons probleem. We kunnen tijdsintervallen tussen observaties coderen als speciale tokens in de sequentie. De multi-domein aanpak (diagnoses + medicaties + procedures in één sequentie) is analoog aan onze behoefte om events + numerieke wijzigingen in één sequentie te combineren. Echter, CEHR-BERT behandelt alle concepten als categorisch — numerieke waarden (labresultaten, omzet) worden niet native ondersteund.

## Beperkingen
- Alleen categorische concepten — geen numerieke waarden
- Discretisatie van tijdsintervallen (W/M/LT) verliest precisie
- De sequentie wordt lang door de extra ATT- en VS/VE-tokens
- Geen ondersteuning voor continue meetwaarden

## Gerelateerde bronnen
- [[li_2020_behrt]] — basis BERT voor EHR zonder temporele tokens
- [[choi_2016_retain]] — multi-hot encoding alternatief
- [[tipirneni_2022_strats]] — triplet-representatie met continue waarden
- [[luetto_2023_unittab]] — mixed types + temporeel in Transformer

## Bronvermelding (APA 7e editie)
Pang, C., Jiang, X., Kalluri, K. S., Spotnitz, M., Chen, R., Perotte, A., & Natarajan, K. (2021). CEHR-BERT: Incorporating temporal information from structured EHR data to improve prediction tasks. *Proceedings of Machine Learning for Health (ML4H)*, *158*, 239-260. https://arxiv.org/abs/2111.08585
