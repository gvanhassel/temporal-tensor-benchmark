---
title: "Time-series Generative Adversarial Networks"
authors: ["Yoon, J.", "Jarrett, D.", "van der Schaar, M."]
year: 2019
doi: ""
journal: "Advances in Neural Information Processing Systems (NeurIPS 2019)"
open_access_url: "https://proceedings.neurips.cc/paper/2019/file/c9efe5f26cd17ba6216bbe2a7d26d490-Paper.pdf"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, GAN, tijdreeksen, synthetische-data]
---

# Time-series Generative Adversarial Networks

## Samenvatting
TimeGAN is een raamwerk voor het genereren van realistische synthetische tijdreeksdata. Het combineert de flexibiliteit van ongesuperviseerd leren (adversarial training) met de controle van gesuperviseerd leren. Het model introduceert een embedding-netwerk dat een omkeerbare afbeelding biedt tussen features en latente representaties, waardoor de dimensionaliteit van de adversarial leerruimte wordt gereduceerd. Naast de standaard ongesuperviseerde adversarial loss introduceert TimeGAN een stapsgewijze gesuperviseerde loss die de originele data als supervisie gebruikt, waardoor het model expliciet wordt aangemoedigd om de stapsgewijze conditionele distributies in de data vast te leggen. TimeGAN presteert consistent beter dan state-of-the-art benchmarks op het gebied van gelijkenis en voorspellend vermogen.

## Sleutelconclusies
- De combinatie van ongesuperviseerde en gesuperviseerde training levert realistischere tijdreeksen op dan puur adversarial methoden
- Een embedding-netwerk dat de leerruimte reduceert is essentieel voor het vastleggen van temporele dynamiek
- De stapsgewijze gesuperviseerde loss zorgt ervoor dat het model conditionele afhankelijkheden in de tijd leert

## Methodologie
Het model bestaat uit vier componenten: een embedding-functie, een recovery-functie, een sequentiegenerator en een sequentiediscriminator. Training gebeurt in drie fasen: (1) autoencoder-training voor de embedding, (2) gesuperviseerde training van de generator in de latente ruimte, en (3) gezamenlijke training met adversarial en gesuperviseerde loss. Evaluatie op zowel synthetische als echte datasets (aandelen, energie, evenementen) met behulp van discriminatieve en predictieve scores.

## Data & Techniek

### Gebruikte technieken
GAN (Generative Adversarial Network), RNN/GRU voor sequentiemodellering, autoencoder voor embedding, gesuperviseerde en ongesuperviseerde loss-combinatie.

### Inputdata
Tijdreeksdata: aandelenkoersen (Google, 6 features), energieverbruik (28 features), medische data (ICU-patienten). Zowel univariate als multivariate tijdreeksen met vaste lengte.

### Preprocessing
Normalisatie van features, segmentatie in vensters van vaste lengte (24 tijdstappen), min-max scaling.

### Preprocessing-problemen & oplossingen
De hoge dimensionaliteit van de adversarial leerruimte werd aangepakt door een geleerde embedding-ruimte te introduceren in plaats van direct op de oorspronkelijke features te werken.

### Datapipeline & modelinput
Genormaliseerde tijdreeksvensters van vaste lengte (T x D tensor, waar T = tijdstappen en D = features) worden via het embedding-netwerk omgezet naar een lagerdimensionale latente representatie waarop de generator en discriminator opereren.

## Beperkingen
- Vaste vensterlengte vereist; geen ondersteuning voor variabele-lengte tijdreeksen
- Evaluatie beperkt tot relatief korte sequenties (24 tijdstappen)
- Geen expliciete controle over welke patronen de generator produceert
- Schaalbaarheid naar zeer lange tijdreeksen niet onderzocht

## Gerelateerde bronnen
- [[lin_2020_doppelganger]] — DoppelGANger verbetert op TimeGAN met betere fidelity (+43%) en metadata-ondersteuning
- [[yuan_2024_diffusion_ts]] — modernere diffusie-gebaseerde aanpak die TimeGAN overtreft
- [[ismail_fawaz_2019_dl_tsc_review]] — overzicht van deep learning architecturen voor tijdreeksen
- [[kang_2020_gratis]] — alternatieve aanpak voor controleerbare synthetische tijdreeksgeneratie

## Bronvermelding (APA 7e editie)
Yoon, J., Jarrett, D., & van der Schaar, M. (2019). Time-series Generative Adversarial Networks. In *Advances in Neural Information Processing Systems 32 (NeurIPS 2019)*. https://proceedings.neurips.cc/paper/2019/hash/c9efe5f26cd17ba6216bbe2a7d26d490-Abstract.html
