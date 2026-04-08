---
title: "SynTSBench: Rethinking Temporal Pattern Learning in Deep Learning Models for Time Series"
authors: ["Tan, Q.", "Chen, Y.", "Li, M.", "Gu, R.", "Su, Y.", "Zhang, X.-P."]
year: 2025
doi: "10.48550/arXiv.2510.20273"
journal: "NeurIPS 2025"
open_access_url: "https://arxiv.org/abs/2510.20273"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, benchmark, synthetische-data, tijdreeksen, deep-learning, evaluatie, temporele-patronen]
---

# SynTSBench: Rethinking Temporal Pattern Learning in Deep Learning Models for Time Series

## Samenvatting
SynTSBench is een synthetisch data-gedreven evaluatieparadigma dat de fundamentele modelleercapaciteiten van deep learning modellen voor tijdreeksvoorspelling systematisch beoordeelt via programmeerbare feature-configuratie. Het raamwerk isoleert verstorende factoren en stelt een interpreteerbaar evaluatiesysteem op met drie kernanalysedimensies: (1) temporele feature-decompositie en capabiliteitsmapping, (2) robuustheidsanalyse onder data-irregulariteiten, en (3) theoretisch optimum-benchmarking. Het paper toont aan dat huidige deep learning modellen niet universeel de optimale baselines benaderen voor alle types temporele patronen.

## Sleutelconclusies
- Huidige state-of-the-art deep learning modellen falen bij specifieke types temporele patronen, ondanks sterke prestaties op standaard benchmarks
- Synthetische data met controleerbare eigenschappen is een krachtigere evaluatiemethode dan echte datasets omdat verstorende factoren kunnen worden geisoleerd
- Er bestaan fundamentele grenzen aan wat elk type model kan leren; het paper kwantificeert deze grenzen per patroontype

## Methodologie
Generatie van synthetische tijdreeksen met programmeerbare temporele patronen: trend (lineair, polynomiaal), seizoenaliteit (sinusoiden, harmonischen), ruis (Gaussisch, met varierende SNR), anomalieen en structurele breuken. Evaluatie van populaire modellen (Transformer, Informer, Autoformer, DLinear, PatchTST, iTransformer, etc.) op elk patroontype afzonderlijk. Vergelijking met theoretische optima (bijv. perfecte Fourier-reconstructie voor seizoenaliteit).

## Data & Techniek

### Gebruikte technieken
Synthetische datageneratie via parametrische modellen (sinusoiden, polynomen, stochastische processen). Evaluatie van Transformer-varianten, MLP-modellen en hybride architecturen. Theoretische optimum-berekening per patroontype.

### Inputdata
Volledig synthetische tijdreeksen met controleerbare parameters: frequentie, amplitude, trendorde, ruisniveau, anomalietype. Univariate en multivariate configuraties.

### Preprocessing
Minimale preprocessing door ontwerp: de synthetische data is al in het gewenste formaat. Standaard normalisatie waar nodig.

### Preprocessing-problemen & oplossingen
_N.v.t._ — door het gebruik van synthetische data zijn typische preprocessing-problemen (ontbrekende waarden, outliers, inconsistente formaten) door ontwerp afwezig.

### Datapipeline & modelinput
Parameterconfiguratie -> synthetische tijdreeksgeneratie -> standaard train/val/test-splitsing -> model training en evaluatie -> vergelijking met theoretisch optimum.

## Beperkingen
- Synthetische patronen zijn per definitie eenvoudiger dan echte data; de vertaling naar real-world prestaties is niet direct
- Alleen voorspelling (forecasting) onderzocht; geen classificatie of anomaliedetectie
- De theoretische optima zijn alleen beschikbaar voor eenvoudige patroontypen
- Interacties tussen meerdere patroontypen (bijv. trend + seizoenaliteit + ruis) zijn minder uitgebreid onderzocht

## Gerelateerde bronnen
- [[dau_2019_ucr_archive]] — SynTSBench positioneert zich als complementair aan echte benchmark-archieven
- [[bagnall_2018_uea_multivariate]] — multivariate benchmark waarvoor SynTSBench een synthetisch alternatief biedt
- [[ismail_fawaz_2019_dl_tsc_review]] — SynTSBench evalueert vergelijkbare deep learning architecturen
- [[kang_2020_gratis]] — GRATIS deelt het idee van controleerbare synthetische datageneratie maar richt zich op forecasting-evaluatie
- [[bandt_2002_permutation_entropy]] — complexiteitsmaten zijn relevant voor het ontwerpen van de moeilijkheidsgraad van synthetische patronen

## Bronvermelding (APA 7e editie)
Tan, Q., Chen, Y., Li, M., Gu, R., Su, Y., & Zhang, X.-P. (2025). SynTSBench: Rethinking Temporal Pattern Learning in Deep Learning Models for Time Series. In *Advances in Neural Information Processing Systems 38 (NeurIPS 2025)*. https://arxiv.org/abs/2510.20273
