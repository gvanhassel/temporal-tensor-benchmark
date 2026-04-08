---
title: "Self-Attentive Hawkes Process"
authors: ["Zhang, Q.", "Lipani, A.", "Kirnap, O.", "Yilmaz, E."]
year: 2020
doi: ""
journal: "Proceedings of the 37th International Conference on Machine Learning (ICML)"
open_access_url: "http://proceedings.mlr.press/v119/zhang20q/zhang20q.pdf"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, self-attention, hawkes-process, temporal-point-process, positional-encoding, event-sequences]
---

# Self-Attentive Hawkes Process

## Samenvatting
Dit paper stelt het Self-Attentive Hawkes Process (SAHP) model voor, dat self-attention toepast op de intensiteitsfunctie van Hawkes-processen. De kernbijdrage is een aangepaste positional encoding die rekening houdt met de werkelijke tijdsintervallen tussen events, in plaats van alleen de volgorde. Dit wordt bereikt door tijdsintervallen te vertalen naar faseverschuivingen van sinusodale functies. Vergeleken met conventionele statistische methoden is SAHP krachtiger in het identificeren van complexe afhankelijkheden; vergeleken met diepe recurrente netwerken vangt het langere historische informatie op en is het beter interpreteerbaar doordat de geleerde attention-gewichten de bijdrage van elk historisch event tonen.

## Sleutelconclusies
- Temporele positional encoding via faseverschuivingen van sinusfuncties is effectiever dan standaard positional encoding voor event-sequenties met onregelmatige tijdsintervallen
- De attention-gewichten bieden directe interpretatie van welke historische events invloed hebben op toekomstige events
- SAHP presteert vergelijkbaar met of beter dan RNN-gebaseerde modellen op standaard temporal point process benchmarks

## Methodologie
Aanpassing van de transformer self-attention voor continue-tijd event-sequenties. De sinusodale positional encoding van Vaswani et al. wordt uitgebreid met leerbare faseparameters die afhangen van de tijdsintervallen. Evaluatie op synthetische en echte datasets (stackoverflow, retweets, financiele data).

## Data & Techniek

### Gebruikte technieken
Self-attention mechanisme, aangepaste sinusodale temporele encoding met faseverschuivingen, Hawkes-proces intensiteitsfunctie, maximum likelihood-schatting.

### Inputdata
Event-sequenties met tijdstempels en event-types. Datasets: synthetische Hawkes-processen, StackOverflow-data, retweet-data, financiele transacties.

### Preprocessing
Events als (type, tijdstip)-paren. Berekening van inter-event tijden. Event-type embeddings.

### Preprocessing-problemen & oplossingen
Onregelmatige tijdsintervallen — kernprobleem van dit paper, opgelost via de tijdsafhankelijke faseverschuiving in de positional encoding. Dit is conceptueel eleganter dan de ad-hoc oplossingen in eerdere modellen.

### Datapipeline & modelinput
Input: sequentie van event-embeddings verrijkt met tijdsafhankelijke positional encoding. De attention-lagen produceren contextuele representaties. Output: continue intensiteitsfunctie per event-type die de kans op het volgende event over de tijd beschrijft.

## Beperkingen
- Net als THP geen integratie van numerieke features naast event-types
- Evaluatie voornamelijk op next-event prediction en likelihood, niet op classificatietaken
- Schaalbaarheid bij zeer lange sequenties niet expliciet geadresseerd

## Gerelateerde bronnen
- [[zuo_2020_transformer_hawkes_process]] — parallelle ICML 2020 paper met vergelijkbare doelstelling maar andere temporele encoding
- [[shchur_2021_neural_tpp_review]] — overzicht dat SAHP bespreekt als een van de transformer-gebaseerde TPP-modellen
- [[choi_2016_retain]] — eerdere attention voor event sequences, maar met GRU in plaats van pure self-attention

## Bronvermelding (APA 7e editie)
Zhang, Q., Lipani, A., Kirnap, O., & Yilmaz, E. (2020). Self-attentive Hawkes process. In *Proceedings of the 37th International Conference on Machine Learning* (ICML 2020, Vol. 119, pp. 11183–11193). PMLR. http://proceedings.mlr.press/v119/zhang20q.html
