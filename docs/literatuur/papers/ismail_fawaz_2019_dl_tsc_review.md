---
title: "Deep learning for time series classification: a review"
authors: ["Ismail Fawaz, H.", "Forestier, G.", "Weber, J.", "Idoumghar, L.", "Muller, P.-A."]
year: 2019
doi: "10.1007/s10618-019-00619-1"
journal: "Data Mining and Knowledge Discovery"
open_access_url: "https://arxiv.org/abs/1809.04356"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, deep-learning, tijdreeksen, classificatie, review, CNN, ResNet]
---

# Deep learning for time series classification: a review

## Samenvatting
Dit paper presenteert het meest uitgebreide empirische onderzoek naar deep neural network (DNN) architecturen voor tijdreeksclassificatie (TSC) tot op dat moment. De auteurs trainden 8.730 deep learning modellen op 97 tijdreeksdatasets uit het UCR/UEA-archief. Ze bieden een uniforme taxonomie van DNN's voor TSC en een open source framework met implementaties van alle vergeleken methoden. De resultaten tonen dat ResNet en Fully Convolutional Networks (FCN) de beste prestaties leveren onder de onderzochte architecturen, terwijl Encoder en Multi-Channel CNN ook competitief zijn.

## Sleutelconclusies
- ResNet is de beste individuele deep learning architectuur voor tijdreeksclassificatie op het UCR-archief
- Fully Convolutional Networks (FCN) presteren vergelijkbaar met ResNet en zijn eenvoudiger
- Geen enkel deep learning model domineert op alle datasets; ensemble-methoden zoals COTE en HIVE-COTE presteren nog beter
- Generatieve modellen (echo state networks) presteren onder de maat voor classificatie

## Methodologie
Systematische vergelijking van 9 deep learning architecturen: MLP, FCN, ResNet, Encoder, MCNN, t-LeNet, MCDCNN, Time-CNN en TWIESN. Training op 97 datasets uit het UCR-archief (44 univariate + 12 multivariate in een subset). Evaluatie via accuracy op vaste train/test-splitsingen. Statistische vergelijking via critical difference diagrams (Friedman-test + Nemenyi post-hoc). Open source implementatie in TensorFlow/Keras.

## Data & Techniek

### Gebruikte technieken
MLP, Fully Convolutional Network (FCN), Residual Network (ResNet), Encoder, Multi-Channel CNN (MCNN), Time-Le-Net, MCDCNN, Time-CNN, Echo State Network (TWIESN). Alle geimplementeerd in TensorFlow/Keras.

### Inputdata
97 univariate tijdreeksdatasets uit het UCR-archief + 12 multivariate datasets uit het UEA-archief. Lengte varieert van 24 tot 2844 tijdstappen. Aantal klassen van 2 tot 60.

### Preprocessing
Z-normalisatie (standaard voor het UCR-archief). Geen aanvullende feature engineering; ruwe tijdreeksen als input. Voor sommige modellen: zero-padding tot gelijke batchlengte.

### Preprocessing-problemen & oplossingen
Varierende datasetgrootte werd aangepakt door per-dataset hyperparameteroptimalisatie achterwege te laten (standaard architecturen). Kleine datasets leidden tot overfitting bij complexere modellen; dit werd geobserveerd maar niet expliciet opgelost.

### Datapipeline & modelinput
Univariate tijdreeksen als 1D-vectoren direct als input voor convolutionele lagen. Multivariate reeksen als 2D-matrices (T x D). Standaard evaluatieprotocol van het UCR-archief.

## Beperkingen
- Geen hyperparameteroptimalisatie per dataset; standaardconfiguraties kunnen suboptimaal zijn
- Alleen classificatie onderzocht; geen regressie, voorspelling of anomaliedetectie
- Beperkt tot het UCR/UEA-archief; geen evaluatie op andere domeinen
- Geen aandacht voor interpreteerbaarheid of verklaarbare AI
- Transformers en attention-mechanismen niet opgenomen (nog niet gangbaar in 2019)

## Gerelateerde bronnen
- [[dau_2019_ucr_archive]] — het UCR-archief waarop de evaluatie is uitgevoerd
- [[bagnall_2018_uea_multivariate]] — het UEA-archief voor de multivariate evaluatie
- [[yoon_2019_timegan]] — generatief model voor tijdreeksen, complementair aan classificatie
- [[tan_2025_syntsbench]] — modernere synthetische benchmark die voortbouwt op dit type evaluatie

## Bronvermelding (APA 7e editie)
Ismail Fawaz, H., Forestier, G., Weber, J., Idoumghar, L., & Muller, P.-A. (2019). Deep learning for time series classification: a review. *Data Mining and Knowledge Discovery*, *33*(4), 917-963. https://doi.org/10.1007/s10618-019-00619-1
