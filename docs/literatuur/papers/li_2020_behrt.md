---
title: "BEHRT: Transformer for Electronic Health Records"
authors: ["Li, Y.", "Rao, S.", "Solares, J. R. A.", "Hassaine, A.", "Ramakrishnan, R.", "Canoy, D.", "Zhu, Y.", "Rahimi, K.", "Salimi-Khorshidi, G."]
year: 2020
doi: "10.1038/s41598-020-62922-y"
journal: "Scientific Reports"
open_access_url: "https://arxiv.org/abs/1907.09538"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, EHR, BERT, transformer, medische-codes, tokenisatie]
---

# BEHRT: Transformer for Electronic Health Records

## Samenvatting
BEHRT past de BERT-architectuur toe op elektronische patiëntendossiers door medische codes te behandelen als "woorden", bezoeken als "zinnen", en de volledige medische geschiedenis als een "document". Het model gebruikt vier embedding-lagen: **disease embedding** (301 codes → 288-dim), **age embedding** (leeftijd bij bezoek), **position embedding** (volgorde), en **segment embedding** (bezoekgrenzen). Voorspelt toekomstige diagnoses via masked language modeling (MLM) op de medische code-sequentie.

## Sleutelconclusies
- Medische diagnoses worden direct als NLP-tokens behandeld — de sequentie van bezoeken is de "tekst"
- Vier additieve embeddings coderen concept, leeftijd, positie en segment
- Alleen diagnoses (301 gegroepeerde ICD-10 codes) — geen medicaties, procedures of labwaarden
- Flexibele architectuur: extra concept-types kunnen als vijfde, zesde embedding worden toegevoegd
- SEP-tokens scheiden bezoeken, CLS-token markeert het begin

## Methodologie
Experimenten op CPRD-dataset (Clinical Practice Research Datalink, UK): 1.6M patiënten. Voorspelling van 301 ziektecodes voor toekomstige bezoeken. Vergelijking met GRU, RETAIN, en logistische regressie.

## Data & Techniek

### Gebruikte technieken
BERT-architectuur met masked language modeling, multi-head self-attention, vier embedding-lagen.

### Inputdata
Sequenties van diagnose-codes per bezoek, in **tokenized long format**: elke diagnose is een apart token, bezoeken worden gescheiden door SEP-tokens.

### Preprocessing
- ICD-10 en Read Codes → 301 gestandaardiseerde Caliber-codes
- Chronologische ordening van bezoeken
- Special tokens: CLS (start), SEP (bezoekscheiding)
- Alleen diagnoses — medicaties en procedures worden niet meegenomen

### Preprocessing-problemen & oplossingen
- **Groot vocabulaire**: Gereduceerd van duizenden naar 301 gegroepeerde codes
- **Variabel aantal codes per bezoek**: Opgelost door tokenisatie + padding
- **Geen numerieke waarden**: Labwaarden en vitale functies worden genegeerd

### Datapipeline & modelinput
**Concrete tokensequentie:**
```
{CLS, diag_1, diag_2, SEP, diag_3, diag_4, diag_5, SEP, ..., diag_n, SEP}
```

**Vier embedding-lagen (additief):**
```
input_embedding = disease_emb + age_emb + position_emb + segment_emb
```

1. **Disease embedding**: `LookupTable(301 codes) → R^288`
2. **Age embedding**: `LookupTable(leeftijdsbuckets) → R^288` — leeftijd bij elk bezoek
3. **Position embedding**: Sinusodale encoding (Vaswani et al.)
4. **Segment embedding**: Binair A/B per bezoek

**Tensorshape:**
```
Input tokens:    (patiënt, max_seq_length)      — integer indices
Na embedding:    (patiënt, max_seq_length, 288)  — dense embeddings
Na BERT:         (patiënt, max_seq_length, 288)  — contextuele embeddings
Output:          (patiënt, max_seq_length, 301)  — voorspelde code-kansen
```

**Relevantie voor ons project:** BEHRT illustreert de **tokenized long format** aanpak: elke medische code wordt een token, bezoeken worden gescheiden door speciale tokens. Dit is toepasbaar op onze events: elk event-type kan een token zijn, en tijdstappen worden gescheiden door SEP-tokens of vergelijkbare markers. Het nadeel: er is geen plek voor numerieke waarden in deze representatie.

## Beperkingen
- Alleen diagnose-codes — geen medicaties, procedures, labwaarden of numerieke metingen
- De sequentie wordt erg lang bij veel bezoeken met veel diagnoses
- Geen continue tijdsrepresentatie — alleen discrete leeftijd en positie
- Segment embedding (A/B) is te simpel voor complexe bezoekstructuren

## Gerelateerde bronnen
- [[pang_2021_cehr_bert]] — uitbreiding met artificiële tijd-tokens en multi-domein concepten
- [[choi_2016_retain]] — multi-hot encoding alternatief voor tokenisatie
- [[tipirneni_2022_strats]] — triplet-representatie die OOK numerieke waarden ondersteunt
- [[luetto_2023_unittab]] — heterogene tabular data met temporele verwerking

## Bronvermelding (APA 7e editie)
Li, Y., Rao, S., Solares, J. R. A., Hassaine, A., Ramakrishnan, R., Canoy, D., Zhu, Y., Rahimi, K., & Salimi-Khorshidi, G. (2020). BEHRT: Transformer for electronic health records. *Scientific Reports*, *10*, 7155. https://doi.org/10.1038/s41598-020-62922-y
