---
title: "Literatuuroverzicht: Transformers op 3D temporele tensordata"
onderwerp: "Transformers op 3D temporele tensordata (subject x tijd x features)"
aantal_bronnen: 5
type: overzicht
tags: [overzicht, literatuur, transformer, tijdreeksen, tensordata]
datum: 2026-04-07
---

# Literatuuroverzicht: Transformers op 3D temporele tensordata

## Inleiding
Dit literatuuroverzicht brengt de wetenschappelijke basis in kaart voor het toepassen van Transformer-architecturen op 3D temporele tensordata met de structuur subject x tijd x features. Deze datastructuur komt veelvuldig voor in domeinen als gezondheidszorg (patienten x meetmomenten x biomarkers), neurowetenschappen (proefpersonen x tijdstappen x kanalen) en sociale wetenschappen (individuen x observaties x variabelen). Het overzicht volgt de evolutie van de Transformer: van de oorspronkelijke architectuur, via bidirectionele pre-training en visuele toepassingen, tot de eerste specifieke aanpassingen voor tijdreeksdata.

## Samenvatting van de literatuur
De Transformer-architectuur, geintroduceerd door Vaswani et al. (2017), heeft een fundamentele verschuiving teweeggebracht in hoe sequentiele data wordt verwerkt. Door recurrence volledig te vervangen door self-attention mechanismen, maakte het model parallelle verwerking mogelijk en kon het lange-afstandsafhankelijkheden effectiever vastleggen dan RNN's en LSTM's. Dit legde de basis voor alle latere toepassingen.

BERT (Devlin et al., 2019) toonde aan dat bidirectionele pre-training op ongelabelde data gevolgd door fine-tuning een uiterst effectief paradigma is. Dit concept is direct relevant voor 3D tensordata: een model zou gepretraind kunnen worden op grote hoeveelheden ongelabelde tijdreeksdata om vervolgens finegetuned te worden op specifieke voorspeltaken. Het masked modeling-concept (willekeurig datapunten maskeren en laten reconstrueren) is direct vertaalbaar naar tijdreeksen.

De Vision Transformer (Dosovitskiy et al., 2021) bewees dat de Transformer-architectuur succesvol buiten NLP kan worden ingezet door beelden op te delen in patches. Dit "patchificatie"-concept is cruciaal voor 3D tensordata: net zoals een beeld wordt opgedeeld in ruimtelijke patches, kan een 3D tensor worden opgedeeld in temporele vensters, subjectgroepen, of feature-subsets die als tokens aan de Transformer worden gevoed.

Li et al. (2019) leverden de eerste specifieke aanpassingen van de Transformer voor tijdreeksdata. Hun convolutional self-attention lost het probleem op dat standaard attention niet gevoelig is voor lokale temporele patronen — essentieel voor data waar nabijgelegen tijdstappen sterk gecorreleerd zijn. De LogSparse attention reduceert het kwadratische geheugenverbruik, wat cruciaal is wanneer de tijdsdimensie van de 3D tensor lang is.

Wu et al. (2020) demonstreerden de praktische toepasbaarheid van Transformers op multivariate tijdreeksdata in een epidemiologische context. Hun generieke raamwerk voor zowel univariate als multivariate tijdreeksen bevestigt dat de architectuur flexibel genoeg is voor de multidimensionale structuur van 3D tensordata.

Samen schetsen deze werken een duidelijke lijn: van de fundamentele architectuur, via het pre-training paradigma en de uitbreiding naar niet-tekstuele data, tot concrete aanpassingen voor temporele data. Voor 3D tensordata (subject x tijd x features) moeten elementen uit al deze werken gecombineerd worden.

## Belangrijkste bevindingen
- **Self-attention is een universeel mechanisme** dat effectief werkt op diverse datatypen (tekst, beeld, tijdreeksen) en daarmee geschikt is als basis voor 3D tensordata — onderbouwd door [[vaswani_2017_attention_is_all_you_need]], [[dosovitskiy_2020_vision_transformer]] en [[li_2019_logsparse_transformer_time_series]]
- **Pre-training + fine-tuning is het dominante paradigma** voor het leren van rijke representaties uit ongelabelde data — zie [[devlin_2019_bert]]; dit is direct toepasbaar door tijdreeksmasking of reconstructietaken
- **Lokaliteit moet expliciet worden ingebouwd** voor tijdreeksdata, omdat standaard attention locality-agnostisch is — [[li_2019_logsparse_transformer_time_series]] lost dit op met convolutionele attention
- **Geheugenreductie is essentieel** voor lange sequenties: de O(n^2) complexiteit van standaard attention is een bottleneck — [[li_2019_logsparse_transformer_time_series]] biedt LogSparse als oplossing; maar [[wu_2020_deep_transformer_influenza]] nuanceert dit door te laten zien dat voor kortere reeksen standaard attention volstaat
- **Patchificatie/tokenisatie van niet-tekstuele data** is een bewezen strategie — [[dosovitskiy_2020_vision_transformer]] voor beelden, vertaalbaar naar temporele vensters of subject-feature blokken in 3D tensors

## Kennislacunes & aanbevelingen
- **Multi-dimensionale attention**: geen van de besproken papers modelleert expliciet de driedimensionale structuur (subject x tijd x features) met aparte attention-mechanismen per dimensie. Onderzoek naar hierarchische of factored attention (bijv. apart over subjects, tijd en features) is nodig.
- **Cross-subject leren**: de besproken tijdreekspapers behandelen elke tijdreeks onafhankelijk of als kanalen. Expliciete modellering van relaties tussen subjects (bijv. via graph attention of cross-subject attention) ontbreekt.
- **Pre-training voor 3D tensordata**: hoewel BERT's pre-training paradigma conceptueel vertaalbaar is, ontbreekt onderzoek naar effectieve pre-training taken voor 3D temporele tensors (bijv. masked time-step prediction, masked feature prediction, masked subject prediction).
- **Schaalbaarheid**: de combinatie van drie dimensies maakt het geheugenprobleem ernstiger. Efficient attention mechanismen die specifiek rekening houden met de tensorstructuur zijn een open onderzoeksvraag.
- **Positional encoding voor meerdere dimensies**: standaard sinusvormige of leerbare positie-embeddings zijn ontworpen voor een dimensie. Hoe positie-informatie over drie dimensies tegelijk te coderen is onvoldoende onderzocht.

## Conclusie
De wetenschappelijke basis voor het toepassen van Transformers op 3D temporele tensordata is stevig maar verspreid. De kernarchitectuur, het pre-training paradigma, de uitbreiding naar niet-tekstuele data en de eerste temporele aanpassingen zijn afzonderlijk goed onderbouwd. De uitdaging ligt in het integreren van deze inzichten tot een coherente architectuur die de driedimensionale structuur van subject x tijd x features expliciet en efficient modelleert.

## Gebruikte bronnen

### Wetenschappelijke bronnen
1. [[vaswani_2017_attention_is_all_you_need]] — Vaswani et al. (2017)
2. [[devlin_2019_bert]] — Devlin et al. (2019)
3. [[dosovitskiy_2020_vision_transformer]] — Dosovitskiy et al. (2021)
4. [[li_2019_logsparse_transformer_time_series]] — Li et al. (2019)
5. [[wu_2020_deep_transformer_influenza]] — Wu et al. (2020)
