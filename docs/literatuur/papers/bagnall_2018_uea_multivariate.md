---
title: "The UEA multivariate time series classification archive, 2018"
authors: ["Bagnall, A.", "Dau, H. A.", "Lines, J.", "Flynn, M.", "Large, J.", "Bostrom, A.", "Southam, P.", "Keogh, E."]
year: 2018
doi: "10.48550/arXiv.1811.00075"
journal: "arXiv preprint (arXiv:1811.00075)"
open_access_url: "https://arxiv.org/abs/1811.00075"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, benchmark, tijdreeksen, classificatie, multivariaat, archief]
---

# The UEA multivariate time series classification archive, 2018

## Samenvatting
Dit paper introduceert het UEA Multivariate Time Series Classification Archive, bestaande uit 30 multivariate tijdreeksdatasets. Het archief is ontwikkeld als complement voor het UCR univariate archief en adresseert het probleem dat multivariate tijdreeksclassificatie-algoritmen vaak worden geevalueerd op slechts een handvol datasets zonder statistische vergelijking. Alle datasets zijn geformatteerd tot gelijke lengte, zonder ontbrekende waarden, en voorzien van vaste train/test-splitsingen. Het paper biedt ook een eerste benchmark met bestaande classificatiealgoritmen.

## Sleutelconclusies
- Er bestond geen gestandaardiseerde benchmark voor multivariate tijdreeksclassificatie; dit archief vult die lacune
- De 30 datasets bestrijken diverse domeinen: menselijke activiteit, EEG, ECG, beweging, audio, en meer
- Bestaande univariate methoden presteren vaak verrassend goed op multivariate data wanneer ze per kanaal worden toegepast

## Methodologie
Systematische verzameling en curation van 30 multivariate datasets uit diverse bronnen. Elk dataset heeft een vaste train/test-splitsing. Vergelijking van classificatiealgoritmen waaronder DTW-varianten (DTW_D, DTW_I), shapelet-gebaseerde methoden en ensemble-methoden. Statistische vergelijking via Friedman-test met post-hoc analyse.

## Data & Techniek

### Gebruikte technieken
Dynamic Time Warping (dependent en independent varianten), shapelet-transformaties, ensemble-classificatie, 1-Nearest Neighbor.

### Inputdata
30 multivariate tijdreeksdatasets. Dimensionaliteit varieert van 2 tot 963 kanalen. Lengte varieert van 8 tot 17984 tijdstappen. Aantal klassen van 2 tot 39.

### Preprocessing
Alle datasets zijn geformatteerd tot gelijke lengte per dataset. Ontbrekende waarden zijn verwijderd of geinterpoleerd. Z-normalisatie per kanaal wordt aanbevolen.

### Preprocessing-problemen & oplossingen
Variabele lengte werd opgelost door padding tot de maximale lengte per dataset. Datasets met ontbrekende waarden werden uitgesloten of vooraf opgeschoond.

### Datapipeline & modelinput
Multivariate tijdreeksen als 2D-matrices (T x D, tijdstappen x dimensies) met klasselabel. Standaard evaluatieprotocol identiek aan het UCR-archief.

## Beperkingen
- Eerste versie bevat slechts 30 datasets; kleiner dan het UCR univariate archief
- Alle reeksen zijn tot gelijke lengte gebracht, wat informatie kan vernietigen
- Geen ondersteuning voor ontbrekende waarden in de standaardversie
- Sommige datasets zijn erg klein voor betrouwbare statistische conclusies

## Gerelateerde bronnen
- [[dau_2019_ucr_archive]] — het univariate UCR-archief, het directe complement van dit multivariate archief
- [[ismail_fawaz_2019_dl_tsc_review]] — evalueert ook multivariate datasets uit dit archief
- [[tan_2025_syntsbench]] — synthetische benchmark als alternatieve evaluatiemethode

## Bronvermelding (APA 7e editie)
Bagnall, A., Dau, H. A., Lines, J., Flynn, M., Large, J., Bostrom, A., Southam, P., & Keogh, E. (2018). The UEA multivariate time series classification archive, 2018. *arXiv preprint arXiv:1811.00075*. https://arxiv.org/abs/1811.00075
