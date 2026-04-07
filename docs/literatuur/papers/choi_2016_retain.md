---
title: "RETAIN: An Interpretable Predictive Model for Healthcare using Reverse Time Attention Mechanism"
authors: ["Choi, E.", "Bahadori, M. T.", "Kulas, J. A.", "Schuetz, A.", "Stewart, W. F.", "Sun, J."]
year: 2016
doi: "10.48550/arXiv.1608.05745"
journal: "Advances in Neural Information Processing Systems (NeurIPS)"
open_access_url: "https://arxiv.org/pdf/1608.05745"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, attention, healthcare, EHR, event-sequences, interpretability]
---

# RETAIN: An Interpretable Predictive Model for Healthcare using Reverse Time Attention Mechanism

## Samenvatting
RETAIN is een interpreterbaar voorspellend model voor gezondheidszorg dat twee niveaus van attention gebruikt om medische dossiers (EHR) te analyseren. Het model verwerkt een reeks ziekenhuisbezoeken in omgekeerde tijdsvolgorde, wat de klinische redenering van artsen nabootst: recente bezoeken krijgen doorgaans meer aandacht. Het eerste attention-niveau bepaalt welke eerdere bezoeken invloedrijk zijn, het tweede niveau bepaalt welke klinische variabelen binnen die bezoeken significant zijn. Getest op 14 miljoen bezoeken van 263.000 patienten over 8 jaar bereikte RETAIN een voorspellende nauwkeurigheid vergelijkbaar met RNN's, terwijl de interpreterbaarheid vergelijkbaar bleef met traditionele modellen zoals logistische regressie.

## Sleutelconclusies
- Twee-niveau attention (visit-level en variable-level) maakt het model interpreteerbaar zonder significante prestatiedaling
- Omgekeerde tijdsvolgorde (reverse time) geeft recent bezoekgedrag meer gewicht, wat klinisch relevant is
- Het model schaalt goed naar grote datasets en is rekenkundig efficienter dan volledige RNN-modellen

## Methodologie
Retrospectieve studie op een groot EHR-dataset (14M bezoeken, 263K patienten, 8 jaar). Het model gebruikt twee GRU-netwerken die in omgekeerde volgorde door de bezoekhistorie lopen om attention-gewichten te genereren. Evaluatie via voorspelling van diagnoses bij toekomstige bezoeken, vergeleken met RNN, GRU en logistische regressie.

## Data & Techniek

### Gebruikte technieken
GRU (Gated Recurrent Unit) voor het genereren van attention-gewichten, twee-niveau neural attention mechanisme, embedding van medische codes.

### Inputdata
Elektronische medische dossiers (EHR): sequenties van ziekenhuisbezoeken, elk bezoek bevat meerdere medische codes (diagnoses, medicatie, procedures). Dataset: 14 miljoen bezoeken, 263.000 patienten, 8 jaar tijdspanne.

### Preprocessing
Medische codes worden omgezet naar embedding-vectoren. Bezoeken worden gerepresenteerd als sets van medische codes. Sequenties van bezoeken worden in omgekeerde chronologische volgorde verwerkt.

### Preprocessing-problemen & oplossingen
Variabele lengte van bezoeksequenties wordt afgehandeld door de RNN-architectuur. Het grote aantal unieke medische codes wordt gereduceerd via embeddings. Class imbalance bij zeldzame diagnoses — _Niet expliciet vermeld hoe dit is opgelost_.

### Datapipeline & modelinput
Elke patient wordt gerepresenteerd als een tijdgeordende sequentie van bezoeken. Elk bezoek is een multi-hot vector van medische codes, omgezet naar een embedding. De sequentie wordt in omgekeerde volgorde door twee GRU-netwerken gevoerd die alpha (visit-level) en beta (variable-level) attention-gewichten produceren. De gewogen som van bezoekrepresentaties vormt de uiteindelijke patientrepresentatie voor classificatie.

## Beperkingen
- Het model gaat uit van discrete bezoeken en modelleert niet continu verlopende tijdsintervallen
- De interpretaties zijn op visit- en variabele-niveau, niet op interactieniveau tussen variabelen
- Getest in een healthcare-setting; generalisatie naar andere domeinen is niet onderzocht

## Gerelateerde bronnen
- [[liu_2018_heterogeneous_temporal_events]] — vergelijkbare aanpak voor heterogene medische events met gate-mechanisme
- [[zuo_2020_transformer_hawkes_process]] — modernere transformer-aanpak voor event sequences
- [[shchur_2021_neural_tpp_review]] — overzichtspaper dat RETAIN plaatst in het bredere TPP-landschap

## Bronvermelding (APA 7e editie)
Choi, E., Bahadori, M. T., Kulas, J. A., Schuetz, A., Stewart, W. F., & Sun, J. (2016). RETAIN: An interpretable predictive model for healthcare using reverse time attention mechanism. *Advances in Neural Information Processing Systems*, *29*. https://arxiv.org/abs/1608.05745
