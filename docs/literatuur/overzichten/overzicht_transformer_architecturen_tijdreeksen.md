---
title: "Literatuuroverzicht: Transformer-architecturen voor tijdreeksvoorspelling"
onderwerp: "Transformer-architecturen specifiek ontworpen voor tijdreeksen"
aantal_bronnen: 6
type: overzicht
tags: [overzicht, literatuur, transformer, tijdreeksen, 3D-tensordata]
datum: 2026-04-07
---

# Literatuuroverzicht: Transformer-architecturen voor tijdreeksvoorspelling

## Inleiding
Transformer-architecturen hebben sinds hun introductie in NLP een enorme impact gehad op diverse domeinen, waaronder tijdreeksvoorspelling. De directe toepassing van Transformers op tijdreeksen brengt echter unieke uitdagingen met zich mee: kwadratische complexiteit bij lange sequenties, verlies van temporele ordening door permutation-invariante self-attention, en de vraag hoe multivariate afhankelijkheden het best gemodelleerd worden. Dit overzicht bespreekt zes sleutelpapers (2021-2023) die deze uitdagingen adresseren, elk met een andere architecturale innovatie, en beoordeelt hun relevantie voor een project over transformers op 3D temporele tensordata (subject x tijd x features).

## Samenvatting van de literatuur

De evolutie van Transformer-modellen voor tijdreeksen verloopt in drie golven. De eerste golf (**efficiëntie**) wordt vertegenwoordigd door **Informer** ([[zhou_2021_informer]]), dat het fundamentele probleem van kwadratische complexiteit aanpakt met ProbSparse self-attention en self-attention distillatie, waardoor de complexiteit daalt naar O(L log L). De generatieve decoder elimineert bovendien de trage autoregressieve inferentie.

De tweede golf (**decompositie en domeinkennis**) omvat **Autoformer** ([[wu_2021_autoformer]]) en **FEDformer** ([[zhou_2022_fedformer]]). Autoformer integreert seizoen-trend decompositie als intern bouwblok en vervangt self-attention door een Auto-Correlation mechanisme dat periodiciteit benut op sub-serie niveau. FEDformer gaat een stap verder door attention te berekenen in het frequentiedomein (Fourier/Wavelet), waardoor lineaire complexiteit O(L) wordt bereikt en globale patronen effectiever worden gevangen.

De derde golf (**herontwerp van de inputrepresentatie**) brengt fundamentele vernieuwingen. **PatchTST** ([[nie_2023_patchtst]]) introduceert patching (sub-series segmentatie) en channel-independence, waarmee het aantoont dat een vanilla Transformer encoder met de juiste tokenisatie alle eerdere modellen overtreft. Het model maakt bovendien self-supervised pre-training mogelijk via masked patch prediction. **Crossformer** ([[zhang_2023_crossformer]]) neemt de tegenovergestelde positie in: het behoudt de 2D-structuur (tijd x dimensies) via DSW embedding en modelleert expliciet cross-dimensie afhankelijkheden met Two-Stage Attention.

Dwars door deze ontwikkeling snijdt de kritische paper van **Zeng et al.** ([[zeng_2023_dlinear]]), die aantoont dat een simpel lineair model (DLinear) de meeste Transformer-varianten overtreft. Hun analyse onthult dat de verbeterde prestaties eerder voortkomen uit de DMS-strategie dan uit het attention-mechanisme. PatchTST weerlegt deze kritiek gedeeltelijk door te demonstreren dat Transformers met de juiste inputrepresentatie wel degelijk meerwaarde bieden.

Een opvallende spanning in het veld betreft de vraag **channel-independence vs. cross-dimensie modellering**. PatchTST en DLinear presteren uitstekend met channel-independence, terwijl Crossformer betoogt dat cross-dimensie afhankelijkheden essentieel zijn. Voor 3D tensordata (subject x tijd x features) is dit debat bijzonder relevant: de feature-dimensie bevat mogelijk waardevolle onderlinge relaties die channel-independence negeert, maar de subject-dimensie voegt een extra laag complexiteit toe.

## Belangrijkste bevindingen

- **Patching is de meest impactvolle innovatie**: het segmenteren van tijdreeksen in sub-series tokens verbetert zowel efficiëntie als nauwkeurigheid en maakt self-supervised learning mogelijk -- onderbouwd door [[nie_2023_patchtst]] en indirect door [[zhang_2023_crossformer]]
- **Decompositie als intern architectuurblok werkt**: seizoen-trend scheiding in elke laag verbetert robuustheid -- aangetoond door [[wu_2021_autoformer]], [[zhou_2022_fedformer]], en zelfs door [[zeng_2023_dlinear]] (die het in DLinear overneemt)
- **De keuze van inputrepresentatie is belangrijker dan de complexiteit van het attention-mechanisme**: PatchTST met vanilla attention overtreft Informer, Autoformer en FEDformer met hun gespecialiseerde attention-varianten -- zie [[nie_2023_patchtst]] vs. [[zhou_2021_informer]], [[wu_2021_autoformer]], [[zhou_2022_fedformer]]
- **Cross-dimensie modellering is waardevol maar niet universeel**: Crossformer toont voordelen bij sterk gecorreleerde variabelen, maar PatchTST nuanceert dit -- vergelijk [[zhang_2023_crossformer]] met [[nie_2023_patchtst]]
- **Simpele baselines zijn essentieel**: DLinear dwingt het veld tot eerlijke vergelijkingen en voorkomt onnodige architecturale complexiteit -- [[zeng_2023_dlinear]]

## Relevantie voor 3D temporele tensordata (subject x tijd x features)

Voor een project met 3D tensordata (subject x tijd x features) zijn de volgende inzichten bijzonder relevant:

| Paper | Relevantie voor 3D tensordata |
|-------|-------------------------------|
| [[zhou_2021_informer]] | **Matig** -- ProbSparse attention schaalt naar lange tijdsequenties maar adresseert niet de subject- of feature-dimensies |
| [[wu_2021_autoformer]] | **Matig** -- Decompositie is nuttig per subject; auto-correlatie kan periodiciteit per subject detecteren |
| [[zhou_2022_fedformer]] | **Matig-hoog** -- Frequentiedomein-representatie kan per subject spectra analyseren; wavelet-variant kan multi-scale patronen per subject vangen |
| [[nie_2023_patchtst]] | **Hoog** -- Patching is direct toepasbaar op de tijddimensie; channel-independence kan per feature OF per subject worden toegepast; self-supervised pre-training is waardevol bij beperkte gelabelde data |
| [[zhang_2023_crossformer]] | **Zeer hoog** -- De DSW embedding en Two-Stage Attention zijn direct relevant: de 2D-structuur (dimensies x tijd) kan worden uitgebreid naar 3D door subjects als extra dimensie te behandelen; het router-mechanisme schaalt naar veel features |
| [[zeng_2023_dlinear]] | **Hoog als baseline** -- DLinear moet als baseline dienen om te verifiëren dat een complexer Transformer-model daadwerkelijk meerwaarde biedt |

### Aanbevolen architectuurkeuzes voor 3D tensordata

1. **Patching op de tijddimensie** (PatchTST): segmenteer de tijdreeks per subject per feature in patches
2. **Cross-feature attention** (Crossformer): gebruik TSA of een variant om afhankelijkheden tussen features te modelleren
3. **Subject-niveau aggregatie**: behandel subjects als een batch-dimensie (channel-independence over subjects) of gebruik een hiërarchisch attention-mechanisme
4. **Decompositie** (Autoformer/FEDformer): integreer trend-seizoen scheiding als intern blok
5. **DLinear als sanity check**: altijd vergelijken met een simpel lineair model

## Kennislacunes & aanbevelingen

- **Geen van de papers adresseert expliciet een 3D tensorstructuur** (subject x tijd x features): de meeste werken met 2D data (tijd x features). Uitbreiding naar 3D vereist architecturale aanpassingen, met name in de embedding- en attention-lagen.
- **De interactie tussen subject-niveau en feature-niveau patronen** is ononderzocht: in veel toepassingen (bijv. medische data, sensornetwerken) variëren patronen per subject.
- **Self-supervised pre-training voor multivariate/multi-subject data** is nog beperkt onderzocht: PatchTST toont het potentieel voor univariate pre-training, maar uitbreiding naar 3D is een open vraag.
- **Schaalbaarheid naar zeer veel features of subjects** is beperkt geëvalueerd: de meeste benchmarks hebben minder dan 1000 variabelen.
- **Latere ontwikkelingen** (iTransformer, TimesFM, Chronos, Moirai) adresseren deels deze lacunes en verdienen nader onderzoek.

## Conclusie
De literatuur toont dat de meest veelbelovende richting voor Transformers op tijdreeksen ligt in de juiste inputrepresentatie (patching) gecombineerd met domeinspecifieke inductive biases (decompositie, frequentiedomein). Voor 3D temporele tensordata biedt een hybride aanpak -- patching op de tijddimensie, cross-feature attention (Crossformer-stijl), en channel-independence over subjects -- het meeste potentieel. DLinear moet altijd als baseline dienen om de meerwaarde van complexere architecturen te valideren.

## Gebruikte bronnen

### Wetenschappelijke bronnen
1. [[zhou_2021_informer]] — Zhou et al. (2021)
2. [[wu_2021_autoformer]] — Wu et al. (2021)
3. [[zhou_2022_fedformer]] — Zhou et al. (2022)
4. [[nie_2023_patchtst]] — Nie et al. (2023)
5. [[zhang_2023_crossformer]] — Zhang & Yan (2023)
6. [[zeng_2023_dlinear]] — Zeng et al. (2023)
