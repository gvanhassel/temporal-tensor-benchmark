---
title: "Transformer Hawkes Process"
authors: ["Zuo, S.", "Jiang, H.", "Li, Z.", "Zhao, T.", "Zha, H."]
year: 2020
doi: "10.48550/arXiv.2002.09291"
journal: "Proceedings of the 37th International Conference on Machine Learning (ICML)"
open_access_url: "https://arxiv.org/pdf/2002.09291"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, transformer, hawkes-process, temporal-point-process, event-sequences, self-attention]
---

# Transformer Hawkes Process

## Samenvatting
Dit paper introduceert het Transformer Hawkes Process (THP) model, dat het self-attention mechanisme van transformers combineert met het Hawkes-procesraamwerk voor het modelleren van event-sequenties. Waar eerdere RNN-gebaseerde modellen moeite hadden met het vastleggen van zowel korte- als langetermijnafhankelijkheden in temporele data, lost THP dit op door de parallelle verwerking en lange-afstandsattentie van de transformer-architectuur. Het model is getest op diverse datasets (sociale media, healthcare, financiele markten) en presteert significant beter dan bestaande modellen op zowel likelihood-schattingen als event-voorspelling.

## Sleutelconclusies
- Self-attention vangt zowel korte- als langetermijnafhankelijkheden in event-sequenties effectief op, iets waar RNN-modellen tekort schieten
- Het model is rekenkundig efficienter dan recurrente alternatieven door parallelle verwerking
- THP kan flexibel uitgebreid worden om meerdere gerelateerde point processes tegelijk te modelleren

## Methodologie
Het model past de transformer-architectuur aan voor continue tijd door een speciale temporele encoding toe te voegen. De conditionele intensiteitsfunctie van het Hawkes-proces wordt geparametriseerd via de transformer-output. Evaluatie op meerdere benchmark-datasets voor temporal point processes, vergeleken met RMTPP, NHP, en andere state-of-the-art modellen.

## Data & Techniek

### Gebruikte technieken
Transformer (self-attention), Hawkes process parameterisering, temporele positional encoding, maximum likelihood-schatting. Geimplementeerd in Python 3.7 met PyTorch 1.4.0.

### Inputdata
Event-sequenties met tijdstempels en event-types uit diverse domeinen: sociale media (retweets), healthcare (MIMIC-III), financiele transacties. Variabele lengte sequenties met continue tijdsintervallen.

### Preprocessing
Events worden gerepresenteerd als (type, tijdstip)-paren. Tijdsintervallen tussen events worden berekend en gebruikt in de temporele encoding. Event-types worden geembedded.

### Preprocessing-problemen & oplossingen
Onregelmatige tijdsintervallen — opgelost via continue temporele encoding in plaats van discrete positional encoding. Variabele sequentielengtes — standaard transformer-padding en masking.

### Datapipeline & modelinput
Inputsequentie: reeks van (event-type embedding + temporele encoding) vectoren. De transformer-encoder verwerkt deze parallel via self-attention. Output: conditionele intensiteitsfunctie per event-type, die zowel het volgende event-type als de wachttijd voorspelt.

## Beperkingen
- Focus op event-type en timing; geen integratie van aanvullende numerieke features bij events
- Schaalt kwadratisch met sequentielengte (standaard transformer-beperking)
- Evaluatie voornamelijk op next-event prediction, minder op downstream classificatietaken

## Gerelateerde bronnen
- [[zhang_2020_self_attentive_hawkes]] — parallelle ontwikkeling van attention voor Hawkes processes, met nadruk op temporele phase-shift encoding
- [[shchur_2021_neural_tpp_review]] — overzicht dat THP plaatst binnen het veld van neural temporal point processes
- [[choi_2016_retain]] — eerdere attention-aanpak voor medische event-sequenties, maar zonder Hawkes-procesformulering

## Bronvermelding (APA 7e editie)
Zuo, S., Jiang, H., Li, Z., Zhao, T., & Zha, H. (2020). Transformer Hawkes process. In *Proceedings of the 37th International Conference on Machine Learning* (ICML 2020, Vol. 119, pp. 11692–11702). PMLR. https://arxiv.org/abs/2002.09291
