---
title: "Using GANs for Sharing Networked Time Series Data: Challenges, Initial Promise, and Open Questions"
authors: ["Lin, Z.", "Jain, A.", "Wang, C.", "Fanti, G.", "Sekar, V."]
year: 2020
doi: "10.1145/3419394.3423643"
journal: "ACM Internet Measurement Conference (IMC 2020)"
open_access_url: "https://arxiv.org/abs/1909.13403"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, GAN, tijdreeksen, synthetische-data, privacy]
---

# Using GANs for Sharing Networked Time Series Data: Challenges, Initial Promise, and Open Questions

## Samenvatting
DoppelGANger (DG) is een GAN-gebaseerd raamwerk voor het genereren van synthetische tijdreeksdata met bijbehorende metadata, specifiek ontworpen voor netwerkdata. Het paper identificeert fundamentele uitdagingen van bestaande GAN-benaderingen voor tijdreeksdata: lange-termijnafhankelijkheden, complexe multidimensionale relaties en mode collapse. DoppelGANger introduceert een workflow die metadata en tijdreeksdata ontkoppelt: eerst worden metadata gegenereerd, vervolgens worden tijdreeksen geconditioneerd op die metadata. Het systeem behaalt tot 43% betere fidelity dan baseline-modellen (waaronder TimeGAN) over diverse real-world datasets.

## Sleutelconclusies
- Het scheiden van metadata-generatie en tijdreeksgeneratie verbetert de kwaliteit significant
- Bestaande GAN-methoden falen bij lange tijdreeksen door mode collapse en het verliezen van temporele structuur
- Privacy blijft een onopgelost probleem; klassieke privacynoties zijn ontoereikend voor tijdreeksdata

## Methodologie
Evaluatie op vijf real-world datasets: bandbreedte-metingen, clusterverzoeken, websessies, Wikipedia-paginaweergaven en netwerk-intrusion data. Fidelity wordt gemeten via structurele karakterisering (autocorrelatie, cross-correlatie), predictieve modellering en algoritmevergelijking. De architectuur scheidt metadata-generatie (feedforward netwerk) van tijdreeksgeneratie (LSTM-gebaseerd), met een "batched" generatiemechanisme voor lange sequenties.

## Data & Techniek

### Gebruikte technieken
GAN met gescheiden generatoren voor metadata en tijdreeksen, LSTM voor temporele generatie, feedforward netwerk voor metadata, Wasserstein-afstandsmaat.

### Inputdata
Netwerkgerelateerde tijdreeksdata met metadata: bandbreedte-metingen per ISP, Google Cluster trace-verzoeken, websessiedata, Wikipedia-paginaweergaven. Multivariate tijdreeksen met categorische en continue metadata.

### Preprocessing
Normalisatie van continue features, one-hot encoding van categorische metadata, segmentatie in batches voor lange sequenties, min-max scaling.

### Preprocessing-problemen & oplossingen
Lange-termijnafhankelijkheden werden aangepakt door een "batched" generatiestrategie: in plaats van de hele reeks in een keer te genereren, worden kortere segmenten sequentieel gegenereerd met conditionering op voorgaande segmenten. Mode collapse werd gereduceerd door de gescheiden metadata-generatie.

### Datapipeline & modelinput
Metadata wordt eerst gegenereerd als conditioneringsvector, waarna de tijdreeksgenerator batchgewijs segmenten produceert. Inputformaat: metadata-vector + tijdreekstensor (T x D) per batch.

## Beperkingen
- Privacy is niet opgelost; het paper identificeert dit als een open vraag
- Schaalbaarheid naar zeer hoge dimensionaliteit niet volledig onderzocht
- De batched-strategie kan artefacten introduceren op batchgrenzen
- Specifiek ontworpen voor netwerkdata; generaliseerbaarheid naar andere domeinen onzeker

## Gerelateerde bronnen
- [[yoon_2019_timegan]] — TimeGAN is een van de baselines die DoppelGANger overtreft
- [[yuan_2024_diffusion_ts]] — diffusie-gebaseerde aanpak als alternatief voor GAN-methoden
- [[kang_2020_gratis]] — andere aanpak voor controleerbare tijdreeksgeneratie, niet GAN-gebaseerd

## Bronvermelding (APA 7e editie)
Lin, Z., Jain, A., Wang, C., Fanti, G., & Sekar, V. (2020). Using GANs for Sharing Networked Time Series Data: Challenges, Initial Promise, and Open Questions. In *Proceedings of the ACM Internet Measurement Conference (IMC '20)* (pp. 464-483). ACM. https://doi.org/10.1145/3419394.3423643
