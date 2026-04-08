---
title: "Neural Temporal Point Processes: A Review"
authors: ["Shchur, O.", "Turkmen, A. C.", "Januschowski, T.", "Gunnemann, S."]
year: 2021
doi: "10.48550/arXiv.2104.03528"
journal: "Proceedings of the International Joint Conference on Artificial Intelligence (IJCAI)"
open_access_url: "https://arxiv.org/pdf/2104.03528"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, survey, temporal-point-process, neural-networks, event-sequences, review]
---

# Neural Temporal Point Processes: A Review

## Samenvatting
Dit overzichtspaper consolideert de kennis over neurale temporal point processes (TPP's), probabilistische generatieve modellen voor continue-tijd event-sequenties. De auteurs structureren het veld door de belangrijkste ontwerpchoices en algemene principes voor het definieren van neurale TPP-modellen te identificeren. Ze bespreken de encoder-keuze (RNN vs. attention/transformer), de parametrisering van de intensiteitsfunctie, en de trainingsmethoden. Het paper biedt een overzicht van toepassingsgebieden (healthcare, sociale netwerken, seismologie, financien) en sluit af met open uitdagingen en toekomstige onderzoeksrichtingen.

## Sleutelconclusies
- Neurale TPP's combineren de wiskundige basis van point processes met de flexibiliteit van deep learning, wat krachtigere modellen oplevert
- De keuze tussen RNN- en attention-gebaseerde encoders heeft significante impact op modelprestaties en schaalbaarheid
- Er is een spanning tussen modelcomplexiteit en de mogelijkheid tot exacte likelihood-berekening; veel modellen gebruiken benaderingen

## Methodologie
Systematisch literatuuroverzicht van neurale TPP-modellen. Categorisatie langs drie assen: (1) history-encoder architectuur, (2) parametrisering van de conditionele intensiteit/distributie, (3) trainings- en inferentiemethoden. Vergelijking van benaderingen op theoretische eigenschappen en empirische prestaties.

## Data & Techniek

### Gebruikte technieken
_N.v.t._ — dit is een review-paper. Besproken technieken omvatten: RNN (LSTM, GRU), Transformer/self-attention, normalizing flows, variational autoencoders, neurale ODE's, toegepast op temporal point processes.

### Inputdata
_N.v.t._ — het review bespreekt diverse datasets uit healthcare (MIMIC), sociale media (retweets, StackOverflow), seismologie (aardbevingsdata), en financiele markten.

### Preprocessing
_N.v.t._ — het paper bespreekt algemene preprocessingstappen voor TPP-data: event-type encoding, tijdsnormalisatie, sequence truncatie/padding.

### Preprocessing-problemen & oplossingen
Het review identificeert veelvoorkomende uitdagingen: onregelmatige tijdsintervallen, variabele sequentielengtes, schaarse event-types, en de noodzaak van efficiënte likelihood-berekening.

### Datapipeline & modelinput
_N.v.t._ — het paper beschrijft het generieke TPP-framework: input is een sequentie van (event-type, tijdstip)-paren, de encoder produceert een history-representatie, en de decoder parametriseert de conditionele intensiteitsfunctie of de conditionele distributie over het volgende event.

## Beperkingen
- Het review focust voornamelijk op univariate en multivariate TPP's; spatiaal-temporele uitbreidingen worden kort behandeld
- De vergelijking van modellen is beperkt door het ontbreken van gestandaardiseerde benchmarks op het moment van publicatie
- Classificatietaken (downstream) worden minder diepgaand behandeld dan next-event prediction

## Gerelateerde bronnen
- [[zuo_2020_transformer_hawkes_process]] — een van de besproken transformer-gebaseerde TPP-modellen
- [[zhang_2020_self_attentive_hawkes]] — een van de besproken self-attention TPP-modellen
- [[choi_2016_retain]] — vroeg voorbeeld van attention voor medische event-sequenties, conceptueel verwant

## Bronvermelding (APA 7e editie)
Shchur, O., Turkmen, A. C., Januschowski, T., & Gunnemann, S. (2021). Neural temporal point processes: A review. In *Proceedings of the 30th International Joint Conference on Artificial Intelligence* (IJCAI 2021, pp. 4585–4593). https://arxiv.org/abs/2104.03528
