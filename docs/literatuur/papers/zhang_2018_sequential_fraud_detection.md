---
title: "Sequential Behavioral Data Processing Using Deep Learning and the Markov Transition Field in Online Fraud Detection"
authors: ["Zhang, R.", "Zheng, F.", "Min, W."]
year: 2018
doi: "10.48550/arXiv.1808.05329"
journal: "KDD 2018 Data Science in Fintech Workshop"
open_access_url: "https://arxiv.org/pdf/1808.05329"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, fraud-detection, sequential-data, RNN, markov-transition-field, behavioral-sequences]
---

# Sequential Behavioral Data Processing Using Deep Learning and the Markov Transition Field in Online Fraud Detection

## Samenvatting
Dit paper stelt een RNN-gebaseerde architectuur voor die is geintegreerd met het Markov Transition Field (MTF) voor het detecteren van online fraude op basis van sequentieel gedragsdata. Klantinteracties met websites of apps worden gemodelleerd als een reeks van toestanden (states), en het model voorspelt frauduleus gedrag op basis van deze gedragsequenties. Het MTF zet de sequentie om naar een 2D-matrixrepresentatie die temporele patronen vastlegt. De combinatie van RNN en MTF presteert significant beter dan multilayer perceptrons en afstandsgebaseerde classificatoren met Dynamic Time Warping.

## Sleutelconclusies
- Sequentieel klantgedrag (clickstream, navigatiepatronen) bevat sterke signalen voor fraudedetectie
- De combinatie van RNN met Markov Transition Field vangt zowel sequentiele als probabilistische patronen in gedragsdata
- Het modelleren van gedrag als state-sequenties is effectiever dan het gebruik van geaggregeerde features

## Methodologie
Vergelijking van RNN+MTF met MLP en DTW-gebaseerde classificatoren op online fraudedetectie-data. Gedragssequenties gemodelleerd als opeenvolgingen van gebruikersacties op websites/apps. Evaluatie op detectienauwkeurigheid.

## Data & Techniek

### Gebruikte technieken
Recurrent Neural Network (RNN), Markov Transition Field (MTF) voor 2D-representatie van sequenties, Deep Learning classificatie. Dynamic Time Warping (DTW) als baseline.

### Inputdata
Clickstream-data van online financiele diensten: sequenties van gebruikersinteracties (pagina-bezoeken, klikken, formulierinvullingen) met tijdstempels. Binaire classificatie: fraude vs. legitiem.

### Preprocessing
Gebruikersacties gecodeerd als discrete states. Sequenties omgezet naar Markov Transition Field matrices. Standaard preprocessing voor RNN-input (padding, truncatie).

### Preprocessing-problemen & oplossingen
Variabele sequentielengtes — padding/truncatie. Class imbalance (fraude is zeldzaam) — _Niet expliciet vermeld hoe opgelost_. Ruizige clickstream-data — het MTF biedt een robuustere representatie dan ruwe sequenties.

### Datapipeline & modelinput
Ruwe clickstream -> state-encoding -> twee parallelle paden: (1) sequentie -> RNN, (2) sequentie -> MTF-matrix -> CNN/dense verwerking. Gecombineerde representatie -> classificatie-head.

## Beperkingen
- RNN-gebaseerd; geen attention-mechanisme, wat interpretatie bemoeilijkt
- Alleen gedragsequenties; geen integratie van numerieke of tabulaire features naast de sequentie
- Relatief vroeg werk (2018); sindsdien zijn transformer-modellen beschikbaar voor sequentiele data
- Workshop-paper (KDD); niet volledige peer-review van hoofdconferentie

## Gerelateerde bronnen
- [[min_2021_explainable_fraud_clustering]] — modernere aanpak met Bi-LSTM en attention voor fraudedetectie op gedragssequenties
- [[vallarino_2025_hybrid_fraud_detection]] — state-of-the-art hybride architectuur met transformers voor fraudedetectie
- [[choi_2016_retain]] — vergelijkbare sequentiele modellering maar in healthcare-domein

## Bronvermelding (APA 7e editie)
Zhang, R., Zheng, F., & Min, W. (2018). Sequential behavioral data processing using deep learning and the Markov Transition Field in online fraud detection. In *KDD 2018 Workshop on Data Science in Fintech*. https://arxiv.org/abs/1808.05329
