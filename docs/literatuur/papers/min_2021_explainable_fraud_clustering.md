---
title: "Explainable Deep Behavioral Sequence Clustering for Transaction Fraud Detection"
authors: ["Min, W.", "Liang, W.", "Yin, H.", "Wang, Z.", "Li, M.", "Lal, A."]
year: 2021
doi: "10.48550/arXiv.2101.04285"
journal: "AAAI 2021 KDF Workshop"
open_access_url: "https://arxiv.org/pdf/2101.04285"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, fraud-detection, behavioral-sequences, Bi-LSTM, attention, clustering, explainability]
---

# Explainable Deep Behavioral Sequence Clustering for Transaction Fraud Detection

## Samenvatting
Dit paper introduceert FinDeepBehaviorCluster, een methode die clickstream-data als event-sequenties behandelt voor fraudedetectie bij financiele transacties. Het model gebruikt een time attention-gebaseerde Bi-LSTM om sequentie-embeddings te leren op een unsupervised manier. Deze embeddings worden gecombineerd met door risicospecialisten ontworpen features. Voor de clustering is pHDBSCAN ontwikkeld, een geoptimaliseerd clusteralgoritme dat 500 keer sneller is dan de originele implementatie, waardoor honderden miljoenen transacties snel geanalyseerd kunnen worden. Het framework identificeert gemiste fraudegevallen en extraheert verklaarbare patronen uit risicovolle clusters voor onderzoek.

## Sleutelconclusies
- Unsupervised learning van gedragssequenties via Bi-LSTM met time attention is effectief voor het ontdekken van fraudepatronen zonder labels
- De combinatie van deep learning embeddings met expertfeatures levert betere resultaten dan elk afzonderlijk
- Verklaarbare clusterpatronen zijn cruciaal voor praktische fraudeonderzoeken; puur black-box modellen zijn onvoldoende

## Methodologie
Unsupervised sequentie-embedding via time attention Bi-LSTM op clickstream-data. Clustering via geoptimaliseerd pHDBSCAN. Evaluatie op echte financiele transactiedata (PayPal). Vergelijking van gevonden fraudepatronen met bekende cases en nieuw ontdekte cases.

## Data & Techniek

### Gebruikte technieken
Bi-LSTM met time attention mechanisme, pHDBSCAN (parallelle HDBSCAN), unsupervised embedding learning, combinatie met handmatige expertfeatures.

### Inputdata
Clickstream-data van financiele transacties (PayPal): sequenties van gebruikersacties met tijdstempels. Honderden miljoenen transacties. Binaire classificatie: fraude vs. legitiem (maar training is unsupervised).

### Preprocessing
Clickstream-events gecodeerd als discrete acties. Tijdsintervallen berekend voor time attention. Expertfeatures (door risicospecialisten ontworpen) als aanvullende input.

### Preprocessing-problemen & oplossingen
Schaalbaarheid — opgelost via pHDBSCAN (500x sneller). Geen fraudelabels voor training — unsupervised aanpak via clustering. Interpretatie — risicovolle clusters worden geanalyseerd op gemeenschappelijke patronen.

### Datapipeline & modelinput
Clickstream -> event-encoding + tijdsintervallen -> time attention Bi-LSTM -> sequentie-embedding. Embedding + expertfeatures -> pHDBSCAN clustering -> risicovolle clusters -> patroonextractie voor verklaring.

## Beperkingen
- Unsupervised aanpak; geen directe optimalisatie op fraudedetectie-objectief
- Afhankelijk van expertfeatures naast de geleerde embeddings
- Workshop-paper; beperkte peer-review
- Specifiek voor PayPal-context; generalisatie niet aangetoond

## Gerelateerde bronnen
- [[zhang_2018_sequential_fraud_detection]] — eerdere aanpak voor sequentiele fraudedetectie met RNN en Markov Transition Field
- [[vallarino_2025_hybrid_fraud_detection]] — modernere hybride architectuur met transformers
- [[choi_2016_retain]] — vergelijkbare attention op sequentiele data, maar in healthcare-domein

## Bronvermelding (APA 7e editie)
Min, W., Liang, W., Yin, H., Wang, Z., Li, M., & Lal, A. (2021). Explainable deep behavioral sequence clustering for transaction fraud detection. In *AAAI 2021 Workshop on Knowledge Discovery from Unstructured Data in Financial Services*. https://arxiv.org/abs/2101.04285
