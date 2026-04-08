---
title: "Transformer Hawkes Process"
authors: ["Zuo, S.", "Jiang, H.", "Li, Z.", "Zhao, T.", "Zha, H."]
year: 2020
doi: ""
journal: "ICML 2020"
open_access_url: "https://arxiv.org/abs/2002.09291"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, event-sequentie, hawkes-proces, transformer, temporeel-punt-proces]
---

# Transformer Hawkes Process

## Samenvatting
Transformer Hawkes Process (THP) past de Transformer-architectuur toe op temporele puntprocessen — sequenties van getypeerde events op continue tijdstippen. Elk event wordt gerepresenteerd door een **type-embedding** (via one-hot encoding en geleerde embedding-matrix) plus een **temporele encoding** (sinusodale functies van het continue tijdstip). Self-attention met causaal masking (alleen naar het verleden kijken) modelleert de afhankelijkheden tussen events. Het model voorspelt zowel het volgende event-type als het tijdstip van het volgende event.

## Sleutelconclusies
- Event-types worden geëmbed via een trainbare embedding-matrix U, net als woorden in NLP
- Continue tijdstippen worden gecodeerd via sinusodale positie-encodings (niet geleerd)
- Self-attention vangt lange-termijnafhankelijkheden beter dan RNN-gebaseerde Hawkes-modellen
- Het model combineert event-type en tijdstip additief in één embedding

## Methodologie
Experimenten op synthetische Hawkes-data, MIMIC-II (medische events), StackOverflow (online activiteit), en financiële transactiedata. Vergelijking met RMTPP, NHP, SAHP.

## Data & Techniek

### Gebruikte technieken
Transformer met causaal masking, sinusodale tijdsencoding, event-type embedding matrix.

### Inputdata
Event-sequenties: reeksen van `(event_type, tijdstip)` paren. Puur categorische events op continue tijdstippen.

### Preprocessing
Events worden chronologisch geordend. Event-types als integers gecodeerd. Tijdstippen als continue scalaire waarden.

### Preprocessing-problemen & oplossingen
_Niet vermeld_ — de data is van nature in event-sequentie formaat.

### Datapipeline & modelinput
**Concrete embedding-formules:**

**Event-type embedding:**
```
U ∈ R^(M x K)  — M = embedding-dimensie, K = aantal event-types
event_embedding = U * k_j  — k_j = one-hot vector van event-type j
```

**Temporele encoding:**
```
z(t_j) ∈ R^M  — sinusodale encoding:
z(t)[2i] = sin(t / 10000^(2i/M))
z(t)[2i+1] = cos(t / 10000^(2i/M))
```

**Gecombineerde event-embedding:**
```
X = (U*Y + Z)^T ∈ R^(L x M)
```
Waarbij Y de matrix van one-hot encodings is en Z de matrix van temporele encodings. L = aantal events, M = embedding-dimensie.

**Causaal masking:** Bij het berekenen van attention-output S(j,:) worden alle toekomstige posities gemaskeerd.

**Tensorshape:**
```
Input sequentie:  (L events, 2 kolommen: type + tijdstip)  — LONG format
Na embedding:     (L x M)  — uniforme embedding per event
Na Transformer:   (L x M)  — gecontextualiseerde embeddings
Output:           (L x K)  — voorspelde kans per event-type + (L x 1) voorspeld tijdstip
```

**Relevantie voor ons project:** THP toont hoe **categorische events op continue tijdstippen** worden gerepresenteerd. De aanpak is in LONG format: elke rij is één event met een type en tijdstip. Dit is direct toepasbaar op onze events (aangifte doen, te laat betalen). Echter, THP ondersteunt geen bijbehorende numerieke waarden per event — het kent alleen event-types en tijden.

## Beperkingen
- Alleen categorische event-types — geen numerieke attributen per event
- Geen ondersteuning voor continue variabelen die meeveranderen over de tijd
- Events hebben geen "marks" met variabele waarden (bijv. bedrag van de aangifte)
- Schaalt kwadratisch met sequentielengte

## Gerelateerde bronnen
- [[zhang_2020_sahp]] — Self-Attentive Hawkes Process met tijds-bewuste positie-encoding
- [[tipirneni_2022_strats]] — triplet-representatie die events EN numerieke waarden combineert
- [[choi_2016_retain]] — EHR-model met vergelijkbare event-sequentie aanpak

## Bronvermelding (APA 7e editie)
Zuo, S., Jiang, H., Li, Z., Zhao, T., & Zha, H. (2020). Transformer Hawkes process. *Proceedings of the 37th International Conference on Machine Learning (ICML)*, 11692-11702. https://arxiv.org/abs/2002.09291
