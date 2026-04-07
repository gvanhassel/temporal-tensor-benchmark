---
title: "Learning the Joint Representation of Heterogeneous Temporal Events for Clinical Endpoint Prediction"
authors: ["Liu, L.", "Shen, J.", "Zhang, M.", "Wang, Z.", "Tang, J."]
year: 2018
doi: "10.48550/arXiv.1803.04837"
journal: "Proceedings of the AAAI Conference on Artificial Intelligence"
open_access_url: "https://arxiv.org/pdf/1803.04837"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, heterogeneous-events, temporal-data, clinical-prediction, LSTM, gate-mechanism, classificatie]
---

# Learning the Joint Representation of Heterogeneous Temporal Events for Clinical Endpoint Prediction

## Samenvatting
Dit paper pakt het probleem aan van het leren van gezamenlijke representaties van heterogene temporele events voor klinische voorspelling. In medische dossiers komen verschillende typen events voor (labuitslagen, diagnoses, medicatievoorschriften) die elk hun eigen onregelmatige bezoekpatronen en onderlinge niet-lineaire correlaties hebben. De auteurs stellen een nieuw model voor dat een extra gate toevoegt aan het LSTM-netwerk om de verschillende bezoekfrequenties van event-types te reguleren. Dit modelleert effectief de onregelmatige patronen van verschillende events en hun niet-lineaire samenhang. Experimenten op echte klinische data voor het voorspellen van sterfte en abnormale labuitslagen tonen de effectiviteit van de aanpak.

## Sleutelconclusies
- Heterogene temporele events (met verschillende frequenties en patronen) vereisen een specifiek gate-mechanisme om hun onderlinge relaties te leren
- Het gezamenlijk modelleren van meerdere event-types verbetert voorspellingen ten opzichte van het apart modelleren
- De gate reguleert hoeveel informatie van elk event-type wordt meegenomen, afhankelijk van de bezoekfrequentie

## Methodologie
Evaluatie op echte klinische datasets (MIMIC-III) voor twee taken: mortaliteitsvoorspelling en voorspelling van abnormale labuitslagen. Vergelijking met standaard LSTM, GRU, T-LSTM, en andere baselines. Analyse van het geleerde gate-gedrag voor interpretatie.

## Data & Techniek

### Gebruikte technieken
LSTM met extra event-type gate (HE-LSTM: Heterogeneous Event LSTM), embedding van medische codes, multi-task learning voor meerdere voorspellingstaken.

### Inputdata
Elektronische medische dossiers (MIMIC-III): tijdreeksen van heterogene events inclusief labwaarden (numeriek), diagnoses (categorisch), medicatie (categorisch). Onregelmatige tijdsintervallen per event-type.

### Preprocessing
Medische codes geembedded. Tijdsintervallen per event-type berekend. Events gegroepeerd per type met eigen frequentiepatronen. Numerieke labwaarden genormaliseerd.

### Preprocessing-problemen & oplossingen
Verschillende bezoekfrequenties per event-type — kernprobleem, opgelost via het voorgestelde gate-mechanisme. Ontbrekende waarden door onregelmatig bezoekgedrag — het gate reguleert welke informatie wordt bijgewerkt. Heterogeniteit van datatypes (numeriek vs. categorisch) — uniforme embedding-laag.

### Datapipeline & modelinput
Meerdere parallelle event-streams (lab, diagnose, medicatie) -> elk met eigen embedding -> HE-LSTM met gedeelde hidden state en event-type-specifieke gates -> gezamenlijke representatie -> classificatie-head voor eindpuntvoorspelling.

## Beperkingen
- RNN-gebaseerd (LSTM), wat moeite heeft met zeer lange sequenties
- Geen attention-mechanisme; de gate is een eenvoudiger alternatief
- Getest alleen in healthcare; generalisatie naar andere domeinen (bijv. belastingdata) niet onderzocht

## Gerelateerde bronnen
- [[choi_2016_retain]] — vergelijkbare healthcare-setting maar met attention in plaats van gates, focus op interpretatie
- [[zuo_2020_transformer_hawkes_process]] — modernere transformer-aanpak die ook heterogene events kan modelleren
- [[shchur_2021_neural_tpp_review]] — plaatst dit type model in het bredere TPP-landschap

## Bronvermelding (APA 7e editie)
Liu, L., Shen, J., Zhang, M., Wang, Z., & Tang, J. (2018). Learning the joint representation of heterogeneous temporal events for clinical endpoint prediction. In *Proceedings of the 32nd AAAI Conference on Artificial Intelligence* (AAAI 2018, pp. 3636–3643). https://arxiv.org/abs/1803.04837
