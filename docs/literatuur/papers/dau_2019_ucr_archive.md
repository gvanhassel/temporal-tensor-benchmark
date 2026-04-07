---
title: "The UCR Time Series Archive"
authors: ["Dau, H. A.", "Bagnall, A.", "Kamgar, K.", "Yeh, C.-C. M.", "Zhu, Y.", "Gharghabi, S.", "Ratanamahatana, C. A.", "Keogh, E."]
year: 2019
doi: "10.1109/JAS.2019.1911747"
journal: "IEEE/CAA Journal of Automatica Sinica"
open_access_url: "https://arxiv.org/abs/1810.07758"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, benchmark, tijdreeksen, classificatie, archief]
---

# The UCR Time Series Archive

## Samenvatting
Dit paper beschrijft de uitbreiding van het UCR Time Series Classification Archive van 85 naar 128 datasets. Het archief, opgezet in 2002, is de de facto standaard benchmark voor tijdreeksclassificatie en is gebruikt in meer dan duizend wetenschappelijke publicaties. Naast de uitbreiding biedt het paper pragmatisch advies voor onderzoekers die nieuwe algoritmen willen evalueren op het archief, waaronder richtlijnen voor eerlijke vergelijkingen, statistische tests en het vermijden van veelgemaakte fouten. De datasets bestrijken diverse domeinen: medisch, industrieel, beeld, beweging, spectroscopie en meer.

## Sleutelconclusies
- Het UCR-archief is de belangrijkste benchmark voor univariate tijdreeksclassificatie met 128 datasets
- Veel gepubliceerde claims van algoritmeverbetering zijn statistisch niet onderbouwd; het paper geeft richtlijnen voor correcte evaluatie
- De diversiteit van datasets maakt het mogelijk om algoritmen te testen op uiteenlopende temporele patronen en complexiteitsniveaus

## Methodologie
Systematische curation van tijdreeksdatasets uit diverse bronnen. Elk dataset heeft een vaste train/test-splitsing, z-normalisatie wordt aanbevolen. Het paper vergelijkt meerdere classificatiealgoritmen (1-NN DTW, COTE, InceptionTime) als baseline. Statistische vergelijking via Friedman-test met post-hoc Nemenyi-test of Wilcoxon signed-rank test.

## Data & Techniek

### Gebruikte technieken
Dynamic Time Warping (DTW), 1-Nearest Neighbor, COTE (Collective of Transformation-based Ensembles), diverse afstandsmaten voor tijdreeksen.

### Inputdata
128 univariate tijdreeksdatasets. Grootte varieert van tientallen tot duizenden samples. Lengte varieert van 24 tot 2844 tijdstappen. Elk dataset heeft twee tot zestig klassen.

### Preprocessing
Z-normalisatie (gemiddelde 0, standaarddeviatie 1) wordt sterk aanbevolen als standaard preprocessing. Vaste train/test-splitsingen worden meegeleverd.

### Preprocessing-problemen & oplossingen
Variabele lengte van tijdreeksen werd opgelost door padding of truncatie tot gelijke lengte per dataset. Ontbrekende waarden komen in sommige datasets voor en worden per dataset behandeld.

### Datapipeline & modelinput
Genormaliseerde univariate tijdreeksen als 1D-vectoren met een klasselabel. Standaard evaluatieprotocol: train op de trainset, evalueer op de testset, rapporteer accuracy.

## Beperkingen
- Alleen univariate tijdreeksen; multivariate datasets zijn apart beschikbaar in het UEA-archief
- Vaste train/test-splitsingen beperken de mogelijkheid tot cross-validatie
- Sommige datasets zijn erg klein, wat statistisch betrouwbare conclusies bemoeilijkt
- Het archief test alleen classificatie, niet voorspelling of anomaliedetectie

## Gerelateerde bronnen
- [[bagnall_2018_uea_multivariate]] — het multivariate complement van het UCR-archief, door dezelfde onderzoeksgroep
- [[ismail_fawaz_2019_dl_tsc_review]] — uitgebreide evaluatie van deep learning modellen op het UCR-archief
- [[tan_2025_syntsbench]] — synthetische benchmark als alternatief/aanvulling op het UCR-archief

## Bronvermelding (APA 7e editie)
Dau, H. A., Bagnall, A., Kamgar, K., Yeh, C.-C. M., Zhu, Y., Gharghabi, S., Ratanamahatana, C. A., & Keogh, E. (2019). The UCR time series archive. *IEEE/CAA Journal of Automatica Sinica*, *6*(6), 1293-1305. https://doi.org/10.1109/JAS.2019.1911747
