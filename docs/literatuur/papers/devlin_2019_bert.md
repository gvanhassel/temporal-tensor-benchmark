---
title: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"
authors: ["Devlin, J.", "Chang, M.-W.", "Lee, K.", "Toutanova, K."]
year: 2019
doi: "10.18653/v1/N19-1423"
journal: "Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL-HLT 2019)"
open_access_url: "https://aclanthology.org/N19-1423.pdf"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, transformer, bert, pre-training, NLP]
---

# BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

## Samenvatting
BERT (Bidirectional Encoder Representations from Transformers) introduceert een methode voor het pre-trainen van diepe bidirectionele taalrepresentaties. In tegenstelling tot eerdere modellen die slechts van links naar rechts of oppervlakkig bidirectioneel trainden, conditioneert BERT in alle lagen simultaan op zowel linker- als rechtercontext. Het model wordt gepretraind met twee taken: Masked Language Modeling (MLM), waarbij willekeurige tokens worden gemaskeerd en voorspeld, en Next Sentence Prediction (NSP), waarbij wordt voorspeld of twee zinnen opeenvolgend zijn. Na pre-training kan BERT met slechts een extra uitvoerlaag worden finegetuned voor uiteenlopende taken. BERT behaalde op het moment van publicatie state-of-the-art op elf NLP-benchmarks, waaronder een GLUE-score van 80,5% (+7,7 procentpunt), MultiNLI-accuratesse van 86,7% (+4,6%) en SQuAD v2.0 F1 van 83,1 (+5,1 punt).

## Sleutelconclusies
- Bidirectionele pre-training levert significant betere taalrepresentaties op dan unidirectionele of ondiep bidirectionele benaderingen
- Een gepretraind model kan met minimale taakspecifieke aanpassingen worden finegetuned voor zeer diverse NLP-taken
- Masked Language Modeling maakt echte bidirectionele training mogelijk door het probleem van "zichzelf zien" in standaard bidirectionele modellen te vermijden

## Methodologie
Pre-training op BooksCorpus (800M woorden) en Engelse Wikipedia (2.500M woorden). Twee modelgroottes: BERT-Base (110M parameters, 12 lagen) en BERT-Large (340M parameters, 24 lagen). Evaluatie op GLUE, SQuAD v1.1/v2.0 en SWAG benchmarks. Ablatiestudies tonen het belang van bidirectionele pre-training en NSP.

## Data & Techniek

### Gebruikte technieken
Transformer-encoder (multi-head self-attention), Masked Language Modeling (MLM), Next Sentence Prediction (NSP), WordPiece tokenisatie, fine-tuning met taakspecifieke uitvoerlagen. Architectuur gebaseerd op de encoder-zijde van Vaswani et al. (2017).

### Inputdata
Pre-training: BooksCorpus (800M woorden) + Engelse Wikipedia (2.500M woorden). Fine-tuning: diverse NLP-benchmarkdatasets (GLUE, SQuAD, SWAG).

### Preprocessing
WordPiece tokenisatie met vocabulaire van 30.000 tokens. Input bestaat uit token-embeddings + segment-embeddings + positie-embeddings. Speciale tokens: [CLS] aan het begin, [SEP] tussen zinnen.

### Preprocessing-problemen & oplossingen
Het probleem van bidirectionele training (een woord kan "zichzelf zien") wordt opgelost door Masked Language Modeling: 15% van de tokens wordt willekeurig gemaskeerd. Van die 15% wordt 80% vervangen door [MASK], 10% door een willekeurig token en 10% blijft ongewijzigd, om mismatch tussen pre-training en fine-tuning te verminderen.

### Datapipeline & modelinput
Input is een sequentie van maximaal 512 WordPiece tokens. Het model verwacht een tensor van (batch_size x sequentielengte) met token-IDs, plus bijbehorende segment-maskers en attention-maskers. De [CLS]-representatie wordt gebruikt voor classificatietaken; individuele tokenrepresentaties voor token-level taken.

## Beperkingen
- Mismatch tussen pre-training (met [MASK]-tokens) en fine-tuning (zonder [MASK]-tokens)
- Maximale sequentielengte van 512 tokens beperkt toepassing op lange documenten
- Grote rekenkosten voor pre-training (4 dagen op 64 TPU's voor BERT-Large)
- Alleen encoder-gebaseerd: niet geschikt voor generatieve taken

## Gerelateerde bronnen
- [[vaswani_2017_attention_is_all_you_need]] — de Transformer-architectuur waarop BERT is gebaseerd
- [[dosovitskiy_2020_vision_transformer]] — past vergelijkbaar pre-training concept toe op beelden
- [[li_2019_logsparse_transformer_time_series]] — alternatieve toepassing van Transformers buiten NLP
- [[wu_2020_deep_transformer_influenza]] — gebruikt Transformer-architectuur voor tijdreeksen, zonder pre-training

## Bronvermelding (APA 7e editie)
Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of deep bidirectional transformers for language understanding. *Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT 2019)*, *1*, 4171-4186. https://doi.org/10.18653/v1/N19-1423
