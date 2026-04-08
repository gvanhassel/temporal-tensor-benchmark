---
title: "On Embeddings for Numerical Features in Tabular Deep Learning"
authors: ["Gorishniy, Y.", "Rubachev, I.", "Babenko, A."]
year: 2022
doi: ""
journal: "NeurIPS 2022"
open_access_url: "https://arxiv.org/abs/2203.05556"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, tabular, numerieke-embeddings, piecewise-linear, periodiek]
---

# On Embeddings for Numerical Features in Tabular Deep Learning

## Samenvatting
Dit paper onderzoekt systematisch hoe scalaire numerieke waarden het best kunnen worden geëmbed voor deep learning op tabulaire data. Twee benaderingen worden voorgesteld: (1) **piecewise-linear encoding** die numerieke waarden omzet in een stuksgewijs lineaire functie (vergelijkbaar met een zachte histogram), en (2) **periodieke activaties** (sinusodale functies) die de waarde projecteren naar een hogerdimensionale ruimte via geleerde frequenties en fases. Beide methoden presteren significant beter dan conventionele lineaire embeddings of ReLU-lagen, en maken deep learning competitief met GBDT op traditioneel GBDT-vriendelijke benchmarks.

## Sleutelconclusies
- Numerieke embeddings zijn een onderzocht maar cruciaal vrijheidsgraad in tabulair deep learning
- Piecewise-linear encoding: numerieke waarde → zachte positie in geleerde bins → sparse representatie
- Periodieke encoding: `sin(omega * x + phi)` met geleerde frequentie en fase per dimensie
- Beide methoden verbeteren FT-Transformer significant op meerdere benchmarks
- De keuze tussen piecewise-linear en periodiek is dataset-afhankelijk

## Methodologie
Experimenten op 18 tabulaire benchmarks. Vergelijking van lineaire embedding, ReLU-embedding, piecewise-linear, en periodiek. Toegepast op MLP, ResNet en FT-Transformer backbones.

## Data & Techniek

### Gebruikte technieken
Piecewise-linear encoding, periodieke activatie-functies, FT-Transformer als backbone.

### Inputdata
Tabulaire data met numerieke features.

### Preprocessing
Standaard kwantiel-normalisatie. De embedding-laag vervangt handmatige feature engineering.

### Preprocessing-problemen & oplossingen
- **Lineaire embeddings zijn te simpel**: Opgelost door niet-lineaire transformaties (piecewise-linear of periodiek)
- **Numerieke waarden in verschillende schalen**: De geleerde frequenties/bins passen zich automatisch aan

### Datapipeline & modelinput
**Piecewise-Linear Encoding:**
Numerieke waarde x → bepaal in welke bin(nen) het valt → wijs gewichten toe aan nabije bins → sparse vector van lengte B (aantal bins).

**Periodieke Encoding:**
```
periodic(x) = concat(sin(omega_1 * x + phi_1), ..., sin(omega_d * x + phi_d))
```
Met geleerde frequenties omega en fases phi per dimensie.

Beide encodings produceren een d-dimensionale embedding per numerieke feature, die vervolgens door de Transformer wordt verwerkt.

**Relevantie voor ons project:** Dit paper is direct relevant voor hoe we numerieke features (omzet, werknemers) embedden. In plaats van simpele lineaire projectie (zoals in vanilla FT-Transformer) kunnen we periodieke of piecewise-linear encodings gebruiken voor betere representatie. Dit is complementair aan de feature-tokenisatie van FT-Transformer en de triplet-CVE van STraTS.

## Beperkingen
- Alleen voor tabulaire data — geen temporele component
- Extra hyperparameters (aantal bins, frequenties)
- De keuze tussen methoden is dataset-afhankelijk

## Gerelateerde bronnen
- [[gorishniy_2021_ft_transformer]] — basis FT-Transformer architectuur
- [[luetto_2023_unittab]] — gebruikt frequentie-functies (NeRF-stijl) voor numerieke embeddings in temporele context
- [[tipirneni_2022_strats]] — Continuous Value Embedding (CVE) als alternatieve numerieke embedding

## Bronvermelding (APA 7e editie)
Gorishniy, Y., Rubachev, I., & Babenko, A. (2022). On embeddings for numerical features in tabular deep learning. *Advances in Neural Information Processing Systems*, *35*. https://arxiv.org/abs/2203.05556
