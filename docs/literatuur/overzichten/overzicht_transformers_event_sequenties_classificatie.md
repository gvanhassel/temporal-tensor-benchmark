---
title: "Literatuuroverzicht: Transformers voor event-sequenties, heterogene temporele data en classificatie"
onderwerp: "Transformers voor event-sequenties, heterogene temporele data en classificatie (fraudedetectie)"
aantal_bronnen: 11
type: overzicht
tags: [overzicht, literatuur, transformer, event-sequences, temporal-point-process, tabular-data, fraud-detection]
datum: 2026-04-07
---

# Literatuuroverzicht: Transformers voor event-sequenties, heterogene temporele data en classificatie

## Inleiding
Dit overzicht brengt de wetenschappelijke literatuur in kaart rondom het modelleren van event-sequenties en heterogene temporele data met transformers en aanverwante deep learning-architecturen, specifiek gericht op classificatietaken (zoals fraudedetectie). De context is een project waarin subjects (bijv. burgers bij de Belastingdienst) zowel events genereren (aangifte doen, te laat betalen) als numerieke variabelen hebben (omzet, aantal werknemers) die over de tijd veranderen, en we willen classificeren wie een verhoogd risico heeft op fraude.

## Samenvatting van de literatuur

De literatuur laat drie duidelijke onderzoekslijnen zien die voor dit project samenkomen:

**1. Attention en transformers voor event-sequenties.** Het pionierswerk van Choi et al. (2016) met RETAIN toonde aan dat attention-mechanismen op sequenties van medische bezoeken zowel hoge voorspelkracht als interpreterbaarheid bieden. Het twee-niveau attention-model (welke bezoeken en welke variabelen zijn belangrijk) is direct toepasbaar op belastingdata: welke aangiftemomenten en welke kenmerken zijn het meest voorspellend voor fraude. Liu et al. (2018) breidden dit uit door heterogene event-types met verschillende frequenties gezamenlijk te modelleren via een gate-mechanisme — een directe parallel met belastingdata waar verschillende event-types (aangiftes, betalingen, controles) elk hun eigen ritme hebben.

**2. Temporal point processes met transformers.** Zuo et al. (2020) en Zhang et al. (2020) pasten beide (onafhankelijk, beide gepubliceerd op ICML 2020) de transformer-architectuur aan voor temporal point processes. Het kernprobleem dat zij oplossen — het modelleren van onregelmatige tijdsintervallen tussen events — is direct relevant voor belastingdata waar de timing van events informatief is (bijv. te laat indienen). Zuo's THP gebruikt een continue temporele encoding, terwijl Zhang's SAHP faseverschuivingen in sinusfuncties toepast. Shchur et al. (2021) bieden een uitstekend overzicht dat deze modellen plaatst en de belangrijkste ontwerpkeuzes (encoder-type, intensiteitsfunctie, trainingsmethode) systematiseert.

**3. Tabular transformers voor mixed data.** TabTransformer (Huang et al., 2020), FT-Transformer (Gorishniy et al., 2021) en SAINT (Somepalli et al., 2021) lossen het probleem op van het verwerken van gemengde data (numeriek + categorisch) met transformers. FT-Transformer is hierin het meest volledig: het tokeniseert zowel numerieke als categorische features. SAINT voegt daar intersample attention aan toe, wat relevant is wanneer subjects met vergelijkbaar gedrag vergeleken moeten worden (zoals bij peer-group analyse voor fraudedetectie).

**4. Fraudedetectie met sequentiele deep learning.** Zhang et al. (2018) en Min et al. (2021) passen RNN-gebaseerde modellen toe op clickstream- en gedragssequenties voor fraudedetectie, met respectievelijk Markov Transition Fields en time attention Bi-LSTM. Vallarino (2025) combineert RNN, Transformer en Autoencoder in een Mixture-of-Experts architectuur. De trend is duidelijk: van pure RNN-modellen naar hybride architecturen die transformers integreren.

**De grote kennislacune** is de integratie van deze drie lijnen: er is nog geen gevestigde architectuur die (a) heterogene event-sequenties modelleert met temporal point process-transformers, (b) tegelijkertijd numerieke features per tijdstip meeneemt via tabular transformer-technieken, en (c) dit optimaliseert voor een classificatietaak. Dit is precies de uitdaging van dit project.

## Belangrijkste bevindingen

- **Twee-niveau attention is krachtig en interpreteerbaar**: zowel visit/event-level als variable-level attention biedt inzicht in welke momenten en welke kenmerken een classificatie sturen — cruciaal voor fraudedetectie waar uitlegbaarheid vereist is ([[choi_2016_retain]], [[liu_2018_heterogeneous_temporal_events]])
- **Temporele encoding is essentieel**: standaard positional encoding (op volgorde) is onvoldoende voor event-sequenties met onregelmatige tijdsintervallen; continue temporele encodings of faseverschuivingen zijn nodig ([[zuo_2020_transformer_hawkes_process]], [[zhang_2020_self_attentive_hawkes]])
- **Numerieke features moeten als tokens worden verwerkt**: TabTransformer's beperking (alleen categorische features door de transformer) is opgelost door FT-Transformer's Feature Tokenizer, die elke feature projecteert naar een embedding ([[huang_2020_tabtransformer]], [[gorishniy_2021_ft_transformer]])
- **Intersample attention vergelijkt subjects onderling**: SAINT's rij-attention plaatst een subject in context van vergelijkbare subjects, vergelijkbaar met peer-group analyse ([[somepalli_2021_saint]])
- **Unsupervised en hybride methoden detecteren onbekende patronen**: Autoencoders en unsupervised clustering vangen nieuwe fraudepatronen die supervised modellen missen ([[min_2021_explainable_fraud_clustering]], [[vallarino_2025_hybrid_fraud_detection]])
- **Gedragssequenties bevatten sterkere signalen dan geaggregeerde features**: het modelleren van de volgorde en timing van acties is effectiever dan statische samenvattingen ([[zhang_2018_sequential_fraud_detection]])

## Kennislacunes & aanbevelingen

1. **Integratie van TPP-transformers met tabular transformers**: Er ontbreekt een unified architectuur die event-sequenties (met timing) en tabulaire features (numeriek + categorisch) per tijdstip combineert in een enkel transformer-model. Dit is de kernuitdaging voor het Belastingdienst-scenario.

2. **Classificatie vs. forecasting bij TPP's**: De meeste temporal point process-papers focussen op next-event prediction en likelihood. De vertaling naar een downstream classificatietaak (risico/geen risico) is onderbelicht. Hoe gebruik je de geleerde representaties van een TPP-model als input voor classificatie?

3. **Schaalbaarheid naar miljoenen subjects**: De meeste papers testen op datasets van duizenden tot honderdduizenden samples. Schaalbaarheid naar miljoenen belastingplichtigen met lange event-historieën is niet gevalideerd.

4. **Verklaarbaarheid in de context van regelgeving**: RETAIN biedt interpretatie, maar de vertaling naar juridisch houdbare verklaringen voor fraudeonderzoek ontbreekt in de literatuur.

5. **Veranderend gedrag over lange periodes**: Geen van de besproken modellen adresseert expliciet concept drift — het veranderen van fraudepatronen over de jaren.

## Conclusie
De bouwstenen voor een transformer-gebaseerd classificatiemodel op heterogene temporele event-data zijn beschikbaar in de literatuur. De meest veelbelovende richting voor het project is een architectuur die de temporele encoding van THP/SAHP combineert met de feature-tokenisatie van FT-Transformer, het twee-niveau attention-mechanisme van RETAIN toepast voor interpretatie, en dit optimaliseert voor een classificatiedoel. De fraudedetectie-literatuur bevestigt dat sequentieel gedrag sterke voorspellende waarde heeft en dat hybride architecturen de beste resultaten leveren.

## Gebruikte bronnen

### Wetenschappelijke bronnen
1. [[choi_2016_retain]] — Choi et al. (2016) — RETAIN: attention voor medische event-sequenties
2. [[liu_2018_heterogeneous_temporal_events]] — Liu et al. (2018) — Heterogene temporele events met gate-mechanisme
3. [[zhang_2018_sequential_fraud_detection]] — Zhang et al. (2018) — Sequentiele fraudedetectie met RNN en MTF
4. [[zuo_2020_transformer_hawkes_process]] — Zuo et al. (2020) — Transformer Hawkes Process
5. [[zhang_2020_self_attentive_hawkes]] — Zhang et al. (2020) — Self-Attentive Hawkes Process
6. [[huang_2020_tabtransformer]] — Huang et al. (2020) — TabTransformer
7. [[gorishniy_2021_ft_transformer]] — Gorishniy et al. (2021) — FT-Transformer
8. [[somepalli_2021_saint]] — Somepalli et al. (2021) — SAINT
9. [[min_2021_explainable_fraud_clustering]] — Min et al. (2021) — Explainable fraud clustering met Bi-LSTM
10. [[shchur_2021_neural_tpp_review]] — Shchur et al. (2021) — Review neural temporal point processes
11. [[vallarino_2025_hybrid_fraud_detection]] — Vallarino (2025) — Hybride MoE voor fraudedetectie
