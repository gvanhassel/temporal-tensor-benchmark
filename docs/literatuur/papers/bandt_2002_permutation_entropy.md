---
title: "Permutation Entropy: A Natural Complexity Measure for Time Series"
authors: ["Bandt, C.", "Pompe, B."]
year: 2002
doi: "10.1103/PhysRevLett.88.174102"
journal: "Physical Review Letters"
open_access_url: ""
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, complexiteit, entropie, tijdreeksen, ordinale-patronen]
---

# Permutation Entropy: A Natural Complexity Measure for Time Series

## Samenvatting
Dit seminale paper introduceert permutatie-entropie (PE) als een eenvoudige, robuuste en snel berekenbare complexiteitsmaat voor tijdreeksen. De methode analyseert ordinale patronen: korte opeenvolgende segmenten van de tijdreeks worden gerangschikt op waarde, en de Shannon-entropie van de frequentieverdeling van deze permutaties kwantificeert de diversiteit van patronen. Hogere entropie duidt op meer willekeur of complexiteit. Voor chaotische dynamische systemen gedraagt de complexiteit zich vergelijkbaar met Lyapunov-exponenten. De methode is invariant onder monotone transformaties en robuust tegen ruis.

## Sleutelconclusies
- Permutatie-entropie is een universeel toepasbare complexiteitsmaat die alleen afhangt van de relatieve ordening van waarden
- De maat is extreem snel te berekenen, robuust tegen ruis en vereist geen preprocessing of parameterafstemming
- PE onderscheidt effectief tussen reguliere, chaotische en stochastische tijdreeksen

## Methodologie
Theoretische afleiding van permutatie-entropie gebaseerd op ordinale patronen van orde d (embeddings van d opeenvolgende waarden). Demonstratie op logistische afbeelding en andere dynamische systemen. Vergelijking met Lyapunov-exponenten voor validatie. Analyse van de invloed van de orde d en de vertraging tau op de resultaten.

## Data & Techniek

### Gebruikte technieken
Shannon-entropie, ordinale patroonanalyse, permutaties van orde d, embedding met vertraging tau. Geen machine learning; puur informatietheorie en dynamische systeemanalyse.

### Inputdata
Synthetische tijdreeksen van dynamische systemen (logistische afbeelding, Henon-afbeelding) en experimentele data (laserdynamiek). Univariate tijdreeksen.

### Preprocessing
Geen preprocessing nodig; de methode werkt direct op ruwe tijdreekswaarden doordat alleen de relatieve ordening wordt gebruikt.

### Preprocessing-problemen & oplossingen
_N.v.t._ — de methode is inherent robuust en vereist geen preprocessing.

### Datapipeline & modelinput
Ruwe tijdreeks -> extractie van ordinale patronen van orde d met vertraging tau -> frequentieverdeling van permutaties -> Shannon-entropie berekening -> scalaire complexiteitswaarde.

## Beperkingen
- PE houdt geen rekening met de amplitude van waarden, alleen met de ordening
- Korte tijdreeksen leveren onbetrouwbare schattingen op doordat niet alle permutaties worden geobserveerd
- De keuze van orde d en vertraging tau beinvloedt de resultaten; er zijn geen universele richtlijnen
- PE kan niet onderscheiden tussen verschillende types complexiteit (bijv. periodiek vs. quasi-periodiek)

## Gerelateerde bronnen
- [[kang_2020_gratis]] — gebruikt spectrale entropie en gerelateerde features voor het karakteriseren van gegenereerde tijdreeksen
- [[tan_2025_syntsbench]] — complexiteitsmaten zijn relevant voor het ontwerpen van synthetische benchmarks met varierende moeilijkheidsgraad
- [[dau_2019_ucr_archive]] — PE kan worden gebruikt om de complexiteit van UCR-datasets te karakteriseren

## Bronvermelding (APA 7e editie)
Bandt, C., & Pompe, B. (2002). Permutation entropy: A natural complexity measure for time series. *Physical Review Letters*, *88*(17), 174102. https://doi.org/10.1103/PhysRevLett.88.174102
