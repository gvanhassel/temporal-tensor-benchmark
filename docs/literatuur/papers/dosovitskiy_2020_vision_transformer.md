---
title: "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale"
authors: ["Dosovitskiy, A.", "Beyer, L.", "Kolesnikov, A.", "Weissenborn, D.", "Zhai, X.", "Unterthiner, T.", "Dehghani, M.", "Minderer, M.", "Heigold, G.", "Gelly, S.", "Uszkoreit, J.", "Houlsby, N."]
year: 2021
doi: "10.48550/arXiv.2010.11929"
journal: "International Conference on Learning Representations (ICLR 2021)"
open_access_url: "https://arxiv.org/pdf/2010.11929"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, transformer, vision, ViT, beeldherkenning, patches]
---

# An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale

## Samenvatting
Dit paper toont aan dat een pure Transformer-architectuur, zonder convolutionele componenten, uitstekend presteert op beeldclassificatietaken. Het kernidee is simpel maar krachtig: een afbeelding wordt opgedeeld in vaste patches (bijv. 16x16 pixels), deze patches worden lineair geprojecteerd naar embeddings en als een sequentie van tokens aan een standaard Transformer-encoder gevoed, aangevuld met positie-embeddings en een classificatietoken [CLS]. Wanneer gepretraind op grote datasets (JFT-300M of ImageNet-21k) en vervolgens finegetuned op kleinere benchmarks (ImageNet, CIFAR-100, VTAB), behaalt de Vision Transformer (ViT) resultaten die vergelijkbaar zijn met of beter dan state-of-the-art convolutionele netwerken (zoals BiT en EfficientNet), terwijl de trainingskosten aanzienlijk lager zijn. Het paper demonstreert daarmee dat de dominantie van CNN's in computer vision niet onvermijdelijk is.

## Sleutelconclusies
- Een pure Transformer kan CNN's evenaren of overtreffen op beeldclassificatie, mits gepretraind op voldoende data
- De Transformer heeft minder inductieve bias (geen ingebouwde lokale structuur) dan CNN's, waardoor meer data nodig is, maar bij voldoende data betere generalisatie mogelijk is
- Het opdelen van beelden in patches als "tokens" is een effectieve strategie om de Transformer-architectuur toe te passen buiten NLP

## Methodologie
Afbeeldingen opgedeeld in patches van 16x16 of 14x14 pixels. Pre-training op JFT-300M (303M gelabelde afbeeldingen) of ImageNet-21k (14M afbeeldingen). Fine-tuning op ImageNet (1,3M), CIFAR-10/100, Oxford Flowers, Oxford-IIIT Pets, en VTAB (19 taken). Drie modelgroottes: ViT-Base (86M parameters), ViT-Large (307M), ViT-Huge (632M). Vergelijking met BiT (ResNet-gebaseerd) en EfficientNet.

## Data & Techniek

### Gebruikte technieken
Standaard Transformer-encoder (multi-head self-attention, MLP-blokken, layer normalization), lineaire projectie van afbeeldingspatches, leerbare positie-embeddings, [CLS]-token voor classificatie. Pre-training + fine-tuning paradigma. Geen convoluties in het kernmodel.

### Inputdata
Afbeeldingen van variabele resolutie, opgedeeld in vaste patches. Pre-training op JFT-300M (303M afbeeldingen, 18.291 klassen) of ImageNet-21k (14,2M afbeeldingen, 21.843 klassen). Fine-tuning benchmarks: ImageNet (1.000 klassen), CIFAR-100, VTAB.

### Preprocessing
Afbeeldingen worden opgedeeld in niet-overlappende patches (bijv. een 224x224 afbeelding wordt 196 patches van 16x16). Elke patch wordt afgevlakt tot een vector en lineair geprojecteerd naar de model-dimensie. Standaard data-augmentatie (random cropping, flipping). Bij fine-tuning: hogere resolutie met meer patches, positie-embeddings worden geinterpoleerd.

### Preprocessing-problemen & oplossingen
Het gebrek aan inductieve bias voor lokale structuur (in tegenstelling tot CNN's) wordt gecompenseerd door pre-training op zeer grote datasets. Bij fine-tuning op hogere resoluties dan pre-training worden de geleerde positie-embeddings 2D-geinterpoleerd naar de nieuwe gridgrootte.

### Datapipeline & modelinput
Pipeline: afbeelding -> opdelen in N patches van PxP pixels -> afvlakken naar vectoren van P^2*C dimensies -> lineaire projectie naar D dimensies -> toevoegen positie-embeddings -> prependen van [CLS]-token -> invoer tensor van (batch_size x (N+1) x D). Het model verwerkt dit als een standaard sequentie, analoog aan tokens in NLP.

## Beperkingen
- Vereist zeer grote pre-trainingdatasets; bij training op alleen ImageNet (1,3M afbeeldingen) presteert ViT slechter dan vergelijkbare CNN's
- Patches zijn rigide en niet-overlappend, wat kan leiden tot verlies van fijnkorrelige ruimtelijke informatie
- Quadratische complexiteit in het aantal patches beperkt schaalbaarheid naar zeer hoge resoluties
- Alleen getest op classificatie, niet op detectie of segmentatie (in het originele paper)

## Gerelateerde bronnen
- [[vaswani_2017_attention_is_all_you_need]] — de oorspronkelijke Transformer-architectuur waarop ViT direct is gebaseerd
- [[devlin_2019_bert]] — vergelijkbaar pre-training + fine-tuning paradigma, maar voor tekst; [CLS]-token concept overgenomen
- [[li_2019_logsparse_transformer_time_series]] — alternatieve toepassing van Transformer buiten NLP, op tijdreeksen
- [[wu_2020_deep_transformer_influenza]] — toepassing van Transformer op sequentiele data buiten NLP

## Bronvermelding (APA 7e editie)
Dosovitskiy, A., Beyer, L., Kolesnikov, A., Weissenborn, D., Zhai, X., Unterthiner, T., Dehghani, M., Minderer, M., Heigold, G., Gelly, S., Uszkoreit, J., & Houlsby, N. (2021). An image is worth 16x16 words: Transformers for image recognition at scale. *Proceedings of the International Conference on Learning Representations (ICLR 2021)*. https://doi.org/10.48550/arXiv.2010.11929
