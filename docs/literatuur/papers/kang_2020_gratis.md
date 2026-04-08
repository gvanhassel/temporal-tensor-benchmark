---
title: "GRATIS: GeneRAting TIme Series with diverse and controllable characteristics"
authors: ["Kang, Y.", "Hyndman, R. J.", "Li, F."]
year: 2020
doi: "10.1002/sam.11461"
journal: "Statistical Analysis and Data Mining: The ASA Data Science Journal"
open_access_url: "https://arxiv.org/abs/1903.02787"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, synthetische-data, tijdreeksen, controleerbaar, MAR, benchmark]
---

# GRATIS: GeneRAting TIme Series with diverse and controllable characteristics

## Samenvatting
GRATIS is een methode voor het genereren van synthetische tijdreeksen met diverse en controleerbare eigenschappen, gebaseerd op mixture autoregressive (MAR) modellen. Door de parameters van de MAR-modellen te varieren, kunnen tijdreeksen worden gegenereerd met specifieke statistische kenmerken zoals trend, seizoenaliteit, autocorrelatie en entropie. Het paper onderzoekt de diversiteit en dekking van gegenereerde tijdreeksen in een feature-ruimte en toont aan dat GRATIS kan dienen als een kosteneffectief alternatief voor het verzamelen van echte data bij het evalueren van voorspellings- en classificatiealgoritmen.

## Sleutelconclusies
- Mixture autoregressive modellen bieden een flexibele basis voor het genereren van tijdreeksen met controleerbare statistische eigenschappen
- De gegenereerde tijdreeksen dekken de feature-ruimte breder dan bestaande benchmark-datasets
- GRATIS is bijzonder geschikt als evaluatiemiddel voor forecasting-algoritmen doordat de moeilijkheidsgraad systematisch kan worden gevarieerd

## Methodologie
Generatie van tijdreeksen via MAR(p)-modellen met Gaussische innovaties. Karakterisering van tijdreeksen via een set van features (trend, seizoenaliteit, autocorrelatie, spectrale entropie, etc.) berekend met het tsfeatures R-pakket. Visualisatie van de feature-ruimte via PCA. Evaluatie door gegenereerde data te vergelijken met echte datasets uit het M3/M4 forecasting-competitie archief.

## Data & Techniek

### Gebruikte technieken
Mixture Autoregressive (MAR) modellen, tsfeatures (R-pakket) voor feature-extractie, PCA voor visualisatie van feature-ruimte, diverse forecasting-methoden voor validatie (ETS, ARIMA, Theta, etc.).

### Inputdata
Referentiedata uit M3- en M4-forecastingcompetities als vergelijkingsmateriaal. Gegenereerde data via MAR-modellen met varierende parameters (orde p, aantal componenten K, gewichten).

### Preprocessing
Feature-extractie uit gegenereerde en echte tijdreeksen. Normalisatie van features voor PCA-analyse.

### Preprocessing-problemen & oplossingen
Het bereiken van voldoende diversiteit in gegenereerde data werd opgelost door systematisch de MAR-parameters te varieren. Instabiliteit van sommige MAR-configuraties werd afgevangen door stationariteitscontroles.

### Datapipeline & modelinput
MAR-parameters -> tijdreeksgeneratie -> feature-extractie -> feature-ruimte analyse. De gegenereerde tijdreeksen kunnen direct als input dienen voor elk classificatie- of forecastingalgoritme.

## Beperkingen
- MAR-modellen genereren per definitie lineaire processen; niet-lineaire patronen zijn beperkt
- Geen ondersteuning voor multivariate tijdreeksen
- De controle over features is indirect (via MAR-parameters) in plaats van direct (specificeer gewenste feature-waarden)
- Complexe temporele patronen zoals level shifts, structurele breuken of chaotische dynamiek worden niet expliciet gemodelleerd

## Gerelateerde bronnen
- [[yoon_2019_timegan]] — GAN-gebaseerde aanpak; meer expressief maar minder controleerbaar dan GRATIS
- [[lin_2020_doppelganger]] — GAN-methode met metadata-conditionering als alternatieve controlestrategie
- [[dau_2019_ucr_archive]] — GRATIS kan de feature-ruimte breder dekken dan het UCR-archief
- [[tan_2025_syntsbench]] — vergelijkbaar doel (synthetische benchmark) maar met focus op deep learning evaluatie
- [[bandt_2002_permutation_entropy]] — permutatie-entropie is een van de features die GRATIS gebruikt voor karakterisering

## Bronvermelding (APA 7e editie)
Kang, Y., Hyndman, R. J., & Li, F. (2020). GRATIS: GeneRAting TIme Series with diverse and controllable characteristics. *Statistical Analysis and Data Mining: The ASA Data Science Journal*, *13*(4), 354-376. https://doi.org/10.1002/sam.11461
