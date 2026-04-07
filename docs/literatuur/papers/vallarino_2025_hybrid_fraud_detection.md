---
title: "Detecting Financial Fraud with Hybrid Deep Learning: A Mix-of-Experts Approach to Sequential and Anomalous Patterns"
authors: ["Vallarino, D."]
year: 2025
doi: "10.48550/arXiv.2504.03750"
journal: "arXiv preprint"
open_access_url: "https://arxiv.org/pdf/2504.03750"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, fraud-detection, transformer, mixture-of-experts, RNN, autoencoder, anomaly-detection]
---

# Detecting Financial Fraud with Hybrid Deep Learning: A Mix-of-Experts Approach to Sequential and Anomalous Patterns

## Samenvatting
Dit paper presenteert een hybride architectuur voor creditcardfraude-detectie die een Mixture of Experts (MoE) raamwerk combineert met drie gespecialiseerde componenten: RNN's voor sequentieel gedrag, Transformer-encoders voor complexe feature-interacties, en Autoencoders voor anomaliedetectie via reconstructiefout. Elk component fungeert als een "expert" die een ander aspect van frauduleus gedrag vangt. Het gating-netwerk van de MoE leert welke expert het meest relevant is per transactie. Op synthetische transactiedata behaalt het systeem 98.7% nauwkeurigheid, 94.3% precisie en 91.5% recall, beter dan individuele modellen en traditionele ML-methoden.

## Sleutelconclusies
- De combinatie van sequentiele modellering (RNN), feature-interacties (Transformer) en anomaliedetectie (Autoencoder) via MoE is krachtiger dan elk model apart
- De Autoencoder-component is bijzonder effectief voor het detecteren van nieuwe, onbekende fraudepatronen
- Het modulaire MoE-ontwerp maakt het systeem schaalbaar en uitbreidbaar met nieuwe expertmodellen

## Methodologie
Evaluatie op synthetische transactiedata die echte fraudepatronen nabootst. Vergelijking van het hybride MoE-model met individuele componenten (RNN-only, Transformer-only, Autoencoder-only) en traditionele ML-methoden. Evaluatie op accuracy, precision, recall en F1-score.

## Data & Techniek

### Gebruikte technieken
Mixture of Experts (MoE) framework, RNN (voor sequentiele patronen), Transformer encoder (voor feature-interacties), Autoencoder (voor anomaliedetectie via reconstructiefout), gating network.

### Inputdata
Synthetische creditcard-transactiedata die echte fraudepatronen nabootst. Features omvatten transactiebedrag, tijdstip, locatie, merchant-categorie, en gedragspatronen.

### Preprocessing
Feature-engineering voor transactiekenmerken. Sequentieconstructie van transactiehistorie per klant. Normalisatie van numerieke features. Encoding van categorische features.

### Preprocessing-problemen & oplossingen
Class imbalance (fraude is zeldzaam) — opgelost via de MoE-architectuur die specifieke experts heeft voor zeldzame patronen. Synthetische data — beperking erkend; echte data niet beschikbaar. Nieuwe fraudepatronen — de Autoencoder vangt onbekende anomalieen.

### Datapipeline & modelinput
Transactiedata -> feature-engineering -> drie parallelle paden: (1) transactiesequentie -> RNN-expert, (2) feature-matrix -> Transformer-expert, (3) feature-vector -> Autoencoder-expert. Outputs van experts -> gating network -> gewogen combinatie -> fraudeclassificatie.

## Beperkingen
- Alleen getest op synthetische data; prestaties op echte transactiedata niet gevalideerd
- Single-author paper; beperkte methodologische validatie
- Niet peer-reviewed (arXiv preprint)
- Regulatorische overwegingen (AML, KYC) worden genoemd maar niet rigoureus getest

## Gerelateerde bronnen
- [[zhang_2018_sequential_fraud_detection]] — eerdere sequentiele fraudedetectie, hier uitgebreid met transformers en anomaliedetectie
- [[min_2021_explainable_fraud_clustering]] — complementaire aanpak met nadruk op verklaarbaarheid
- [[gorishniy_2021_ft_transformer]] — de transformer-component in dit paper bouwt voort op tabular transformer-principes

## Bronvermelding (APA 7e editie)
Vallarino, D. (2025). Detecting financial fraud with hybrid deep learning: A mix-of-experts approach to sequential and anomalous patterns. *arXiv preprint arXiv:2504.03750*. https://arxiv.org/abs/2504.03750
