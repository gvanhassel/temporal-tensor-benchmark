---
title: "Literatuuroverzicht: Synthetische datageneratie voor tijdreeksen en benchmarking van temporele modellen"
onderwerp: "Synthetische datageneratie voor tijdreeksen en benchmarking van temporele modellen"
aantal_bronnen: 9
type: overzicht
tags: [overzicht, literatuur]
datum: 2026-04-07
---

# Literatuuroverzicht: Synthetische datageneratie voor tijdreeksen en benchmarking van temporele modellen

## Inleiding
Dit overzicht behandelt de wetenschappelijke literatuur rondom het genereren van synthetische tijdreeksdata en het benchmarken van modellen die temporele patronen moeten leren. De context is een project waarin mock-data wordt gegenereerd met controleerbare trends van toenemende complexiteit, om te testen welke patronen een transformer-architectuur kan leren. De literatuur omvat drie pijlers: (1) generatieve modellen voor tijdreeksen, (2) benchmark-archieven voor evaluatie, en (3) complexiteitsmaten en evaluatiemethoden.

## Samenvatting van de literatuur

### Generatieve modellen: van GAN naar diffusie

De ontwikkeling van generatieve modellen voor tijdreeksen laat een duidelijke evolutie zien. **TimeGAN** ([[yoon_2019_timegan]]) was in 2019 het eerste raamwerk dat adversarial training specifiek combineerde met gesuperviseerde temporele loss, waardoor het model stapsgewijze conditionele distributies leert. Een jaar later verbeterde **DoppelGANger** ([[lin_2020_doppelganger]]) hierop door metadata en tijdreeksen te ontkoppelen, wat tot 43% betere fidelity leidde. Beide methoden worstelen echter met lange-termijnafhankelijkheden en mode collapse.

De meest recente doorbraak komt van **diffusiemodellen**. **Diffusion-TS** ([[yuan_2024_diffusion_ts]], ICLR 2024) introduceert een transformer-gebaseerde architectuur die tijdreeksen ontleedt in trend- en seizoenscomponenten, met een Fourier-gebaseerde loss. Dit model overtreft GAN-methoden significant en biedt bovendien interpreteerbaarheid door de expliciete decompositie.

### Controleerbare generatie

Een andere benadering is het genereren van tijdreeksen met vooraf gespecificeerde eigenschappen. **GRATIS** ([[kang_2020_gratis]]) gebruikt mixture autoregressive modellen om tijdreeksen te genereren met controleerbare statistische kenmerken (trend, seizoenaliteit, entropie). Hoewel eenvoudiger dan GAN/diffusie-methoden, biedt GRATIS directere controle over de eigenschappen van de output -- precies wat relevant is voor het genereren van testdata met toenemende complexiteit.

### Benchmark-archieven

Het **UCR-archief** ([[dau_2019_ucr_archive]]) met 128 univariate datasets en het **UEA-archief** ([[bagnall_2018_uea_multivariate]]) met 30 multivariate datasets vormen samen de standaard voor tijdreeksclassificatie-evaluatie. Ze zijn onmisbaar als referentiepunt, maar hebben beperkingen: de patronen zijn niet controleerbaar, de complexiteit is niet systematisch gevarieerd, en ze testen alleen classificatie.

### Synthetische benchmarking

**SynTSBench** ([[tan_2025_syntsbench]], NeurIPS 2025) vertegenwoordigt een paradigmaverschuiving: in plaats van echte datasets, worden synthetische tijdreeksen met programmeerbare patronen (trend, seizoenaliteit, ruis, anomalieen) gebruikt om modellen te evalueren. Het cruciale inzicht is dat huidige deep learning modellen niet universeel alle patroontypen goed leren -- iets dat alleen zichtbaar wordt met gecontroleerde synthetische data.

### Complexiteitsmaten

**Permutatie-entropie** ([[bandt_2002_permutation_entropy]]) biedt een elegante, robuuste maat voor de complexiteit van tijdreeksen. Door alleen naar de relatieve ordening van waarden te kijken (ordinale patronen), is de maat invariant onder monotone transformaties en robuust tegen ruis. Dit maakt het ideaal voor het kwantificeren van de complexiteit van gegenereerde patronen in een benchmark.

### Deep learning evaluatie

De review van **Ismail Fawaz et al.** ([[ismail_fawaz_2019_dl_tsc_review]]) biedt het meest uitgebreide overzicht van deep learning architecturen voor tijdreeksclassificatie (8.730 modellen op 97 datasets). ResNet en FCN komen als beste individuele modellen naar voren. De studie vormt een methodologische basis voor het systematisch evalueren van wat modellen kunnen leren.

## Belangrijkste bevindingen

- **Diffusiemodellen zijn de nieuwe state-of-the-art** voor tijdreeksgeneratie, met Diffusion-TS als koploper die GAN-methoden (TimeGAN, DoppelGANger) significant overtreft -- zie [[yuan_2024_diffusion_ts]], vergelijk [[yoon_2019_timegan]] en [[lin_2020_doppelganger]]
- **Controleerbare generatie is haalbaar** via verschillende paradigma's: parametrische modellen (GRATIS, [[kang_2020_gratis]]), GAN-conditionering (DoppelGANger), en programmeerbare patronen (SynTSBench, [[tan_2025_syntsbench]])
- **Huidige deep learning modellen falen bij specifieke patroontypen**, zelfs wanneer ze op standaard benchmarks goed presteren -- dit onderstreept de noodzaak van systematische synthetische benchmarks ([[tan_2025_syntsbench]], [[ismail_fawaz_2019_dl_tsc_review]])
- **Permutatie-entropie** biedt een betrouwbare, snel berekenbare maat om de complexiteit van gegenereerde patronen te kwantificeren en te controleren ([[bandt_2002_permutation_entropy]])
- **Het UCR/UEA-archief** blijft de referentiestandaard maar is onvoldoende voor het systematisch testen van specifieke modelcapaciteiten ([[dau_2019_ucr_archive]], [[bagnall_2018_uea_multivariate]])

## Kennislacunes & aanbevelingen

1. **Multivariate controleerbare generatie** -- GRATIS en SynTSBench richten zich voornamelijk op univariate data; er is behoefte aan methoden die multivariate afhankelijkheden systematisch controleren
2. **Interactie-effecten** -- de interactie tussen meerdere patroontypen (trend + seizoenaliteit + ruis + anomalieen) is onvoldoende onderzocht; de meeste evaluaties isoleren patronen
3. **Complexiteitscontinuum** -- er ontbreekt een gestandaardiseerd raamwerk dat complexiteit van patronen definieert op een continue schaal, zodat de leercapaciteit van modellen als functie van complexiteit kan worden gekarakteriseerd
4. **Transformers specifiek** -- de meeste generatieve methoden gebruiken RNN/GRU; evaluatie van wat transformers specifiek wel en niet kunnen leren bij toenemende temporele complexiteit is schaars
5. **Vertaling synthetisch naar reeel** -- het is nog onvoldoende aangetoond dat prestaties op synthetische benchmarks voorspellend zijn voor prestaties op echte data

### Aanbevelingen voor dit project
- Gebruik de **SynTSBench-aanpak** als inspiratie voor het ontwerp van de datagenerator: programmeerbare patronen met toenemende complexiteit
- Implementeer **permutatie-entropie** als objectieve maat voor de complexiteit van gegenereerde patronen
- Gebruik het **UCR/UEA-archief** als referentie om te valideren dat synthetische patronen representatief zijn
- Overweeg **Diffusion-TS** als generatief model indien realistische (niet-parametrische) data nodig is naast de gecontroleerde patronen
- Bouw het complexiteitscontinuum op via **GRATIS-achtige feature-extractie** om de positie van elk gegenereerd patroon in de feature-ruimte te karakteriseren

## Conclusie
De literatuur toont dat synthetische datageneratie voor tijdreeksen een actief en snel evoluerend veld is, met een verschuiving van GAN-methoden naar diffusiemodellen en van echte benchmark-archieven naar programmeerbare synthetische evaluatieparadigma's. Voor het testen van transformer-capaciteiten bij toenemende temporele complexiteit biedt de combinatie van controleerbare generatie (GRATIS/SynTSBench-stijl) met objectieve complexiteitsmaten (permutatie-entropie) de meest veelbelovende aanpak.

## Gebruikte bronnen

### Wetenschappelijke bronnen
1. [[yoon_2019_timegan]] — Yoon, Jarrett & van der Schaar (2019)
2. [[lin_2020_doppelganger]] — Lin, Jain, Wang, Fanti & Sekar (2020)
3. [[dau_2019_ucr_archive]] — Dau, Bagnall, Kamgar et al. (2019)
4. [[bagnall_2018_uea_multivariate]] — Bagnall, Dau, Lines et al. (2018)
5. [[ismail_fawaz_2019_dl_tsc_review]] — Ismail Fawaz, Forestier, Weber et al. (2019)
6. [[kang_2020_gratis]] — Kang, Hyndman & Li (2020)
7. [[yuan_2024_diffusion_ts]] — Yuan & Qiao (2024)
8. [[bandt_2002_permutation_entropy]] — Bandt & Pompe (2002)
9. [[tan_2025_syntsbench]] — Tan, Chen, Li et al. (2025)
