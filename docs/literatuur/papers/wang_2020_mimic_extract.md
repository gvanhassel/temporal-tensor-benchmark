---
title: "MIMIC-Extract: A Data Extraction, Preprocessing, and Representation Pipeline for MIMIC-III"
authors: ["Wang, S.", "McDermott, M. B. A.", "Chauhan, G.", "Ghassemi, M.", "Hughes, M. C.", "Naumann, T."]
year: 2020
doi: "10.1145/3368555.3384469"
journal: "ACM Conference on Health, Inference, and Learning (CHIL)"
open_access_url: "https://arxiv.org/abs/1907.08322"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, MIMIC-III, preprocessing, wide-format, klinisch, pipeline]
---

# MIMIC-Extract: A Data Extraction, Preprocessing, and Representation Pipeline for MIMIC-III

## Samenvatting
MIMIC-Extract is een open-source datapipeline die ruwe MIMIC-III klinische data transformeert naar kant-en-klare **wide-format** representaties voor machine learning. De pipeline produceert vier output-tabellen: statische demografie, vitale functies/labwaarden (uurlijkse statistieken), en interventies (binaire indicatoren per uur). De kernbeslissing is het discretiseren van onregelmatige klinische metingen naar **uurlijkse buckets** met aggregatiestatistieken (gemiddelde, telling, standaarddeviatie). 104 klinisch geaggregeerde tijdreeksvariabelen worden geproduceerd door semantisch vergelijkbare metingen te groeperen.

## Sleutelconclusies
- **Wide format is de de-facto standaard** voor MIMIC-III benchmarks — de meeste downstream modellen verwachten deze representatie
- Uurlijkse discretisatie is een pragmatisch compromis tussen granulariteit en bruikbaarheid
- Continue metingen → uurlijkse statistieken (mean, count, std); events/interventies → binaire indicatoren per uur
- Feature-aggregatie (semantisch vergelijkbare metingen groeperen) reduceert missingness significant
- Forward-fill imputatie + individueel/globaal gemiddelde voor volledig ontbrekende features

## Methodologie
Pipeline toegepast op MIMIC-III v1.4. 34.472 patiënten. Benchmarkresultaten op mortaliteitsvoorspelling, lengte-van-verblijf, en fysiologische decompensatie. Vergelijking met eerdere ad-hoc extracties.

## Data & Techniek

### Gebruikte technieken
Pandas DataFrames, unit-conversie, outlier-detectie, feature-aggregatie, forward-fill imputatie.

### Inputdata
Ruwe MIMIC-III tabellen: chartevents, labevents, inputevents, outputevents, prescriptions.

### Preprocessing
1. **Unit standaardisatie**: kg, cm, Celsius
2. **Outlier handling**: 35.251 niet-valide metingen vervangen, 5.402 extreme outliers verwijderd
3. **Feature-aggregatie**: Ruwe ItemIDs → 104 klinisch betekenisvolle features (handmatige taxonomie)
4. **Uurlijkse aggregatie**: mean, count, std per uur
5. **Imputatie**: Forward-fill → individueel gemiddelde → globaal gemiddelde

### Preprocessing-problemen & oplossingen
- **Inconsistente meeteenheden**: Unit-conversie per feature-type
- **Concept drift**: Verschillende ItemIDs voor dezelfde meting in oud/nieuw EHR-systeem → gegroepeerd
- **Extreme sparsiteit**: Forward-fill + meervoudige imputatiestrategie
- **Outliers**: Feature-level detectie en verwijdering/vervanging

### Datapipeline & modelinput
**Concrete output-structuur:**

**4 output-tabellen met gedeelde index `(subject_id, hadm_id, icustay_id, hours_in)`:**

1. **patients**: Statische demografie + outcomes (leeftijd, geslacht, etniciteit, mortaliteit, LOS)
2. **vitals_labs**: `(patiënt x uren x 104 features x 3 statistieken)` — mean, count, std per feature per uur
3. **vitals_labs_mean**: `(patiënt x uren x 104 features)` — alleen gemiddelden (vereenvoudigd)
4. **interventions**: `(patiënt x uren x N interventies)` — binaire indicatoren per uur

**Tensorshape voor ML:**
```
Vitals/Labs:      (N_patiënten, T_uren, 104 features)     — dense wide format
Interventies:     (N_patiënten, T_uren, N_interventies)    — binaire wide format
Demografie:       (N_patiënten, D_statische_features)      — apart
```

**CRUCIAAL INZICHT VOOR ONS PROJECT:**
MIMIC-Extract illustreert de **pragmatische wide-format aanpak**:
- Onregelmatige metingen → uurlijkse aggregatie (vergelijkbaar met onze maandelijkse/jaarlijkse tijdstappen)
- Numerieke metingen → mean/count/std per tijdstap
- Events/interventies → binaire indicatoren per tijdstap
- Statische features apart

Dit is precies wat ons wide format zou zijn:
```
(burger, tijdstap, [event_aangifte(0/1), event_te_laat(0/1), omzet(float), werknemers(int), ...])
```

Het nadeel: 89.7% van de cellen is leeg (missingness) — een enorme verspilling van geheugen en potentieel ruis voor het model.

## Beperkingen
- Uurlijkse discretisatie verliest sub-uurlijkse informatie
- Forward-fill imputatie introduceert bias (oude waarden worden herhaald)
- Wide format is extreem sparse bij hoge missingness
- Geen ondersteuning voor variabele rij-structuren of event-sequenties

## Gerelateerde bronnen
- [[tipirneni_2022_strats]] — triplet-alternatief dat de sparsity vermijdt
- [[shukla_2021_mtan]] — continue-tijdsalternatief zonder discretisatie
- [[choi_2016_retain]] — EHR-model dat wide format consumeert
- [[li_2020_behrt]] — BERT voor EHR met tokenisatie-aanpak

## Bronvermelding (APA 7e editie)
Wang, S., McDermott, M. B. A., Chauhan, G., Ghassemi, M., Hughes, M. C., & Naumann, T. (2020). MIMIC-Extract: A data extraction, preprocessing, and representation pipeline for MIMIC-III. *Proceedings of the ACM Conference on Health, Inference, and Learning*, 222-235. https://doi.org/10.1145/3368555.3384469
