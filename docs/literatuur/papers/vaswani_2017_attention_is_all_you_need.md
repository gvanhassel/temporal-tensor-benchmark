---
title: "Attention Is All You Need"
authors: ["Vaswani, A.", "Shazeer, N.", "Parmar, N.", "Uszkoreit, J.", "Jones, L.", "Gomez, A. N.", "Kaiser, L.", "Polosukhin, I."]
year: 2017
doi: "10.48550/arXiv.1706.03762"
journal: "Advances in Neural Information Processing Systems (NeurIPS 2017)"
open_access_url: "https://arxiv.org/pdf/1706.03762"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, transformer, attention, architectuur]
---

# Attention Is All You Need

## Samenvatting
Dit baanbrekende paper introduceert de Transformer-architectuur, een nieuw neuraal netwerkmodel dat volledig gebaseerd is op aandachtsmechanismen (attention mechanisms) en afziet van recurrence en convoluties. De architectuur bestaat uit een encoder-decoder structuur met gestapelde lagen van multi-head self-attention en positie-gewijze feed-forward netwerken. Positional encoding wordt gebruikt om de volgorde van de sequentie te behouden. Het model werd getest op machinevertaling (WMT 2014 Engels-Duits en Engels-Frans) en behaalde nieuwe state-of-the-art resultaten: 28,4 BLEU op Engels-Duits en 41,8 BLEU op Engels-Frans. De training duurde slechts 3,5 dag op acht GPU's, wat aanzienlijk minder is dan eerdere modellen. Het model generaliseert ook goed naar andere taken, zoals constituency parsing.

## Sleutelconclusies
- Een pure attention-gebaseerde architectuur kan recurrente en convolutionele netwerken overtreffen op sequence-to-sequence taken
- Multi-head attention maakt het mogelijk om informatie uit verschillende representatie-subruimten op verschillende posities tegelijkertijd te verwerken
- De Transformer is aanzienlijk sneller te trainen dan RNN/LSTM-gebaseerde modellen door parallellisatie

## Methodologie
Het model werd getraind en geevalueerd op twee standaard machinevertaaltaken (WMT 2014). Training gebruikte het Adam-optimalisatiealgoritme met een aangepast leersnelheidschema (warmup + decay). Regularisatie via dropout en label smoothing. Evaluatie via BLEU-score. Vergelijking met bestaande state-of-the-art modellen inclusief ensembles.

## Data & Techniek

### Gebruikte technieken
Multi-head self-attention, scaled dot-product attention, positional encoding (sinusvormig), residual connections, layer normalization, position-wise feed-forward networks, encoder-decoder architectuur, beam search voor inferentie.

### Inputdata
WMT 2014 Engels-Duits (4,5 miljoen zinnenparen) en WMT 2014 Engels-Frans (36 miljoen zinnenparen). Tokens gecodeerd via byte-pair encoding (BPE) met gedeelde vocabulaires.

### Preprocessing
Byte-pair encoding (BPE) tokenisatie. Gedeeld bron-doel vocabulaire van ~37.000 tokens voor Engels-Duits. Zinnen gegroepeerd op approximatieve sequentielengte in batches.

### Preprocessing-problemen & oplossingen
_Niet expliciet vermeld_. BPE lost het probleem van out-of-vocabulary woorden op door zeldzame woorden op te splitsen in subwoordeenheden.

### Datapipeline & modelinput
Invoer bestaat uit tokensequenties omgezet naar embeddings (dimensie 512), waaraan sinusvormige positional encodings worden toegevoegd. Het model verwacht tensors van vorm (batch_size x sequentielengte x d_model). De encoder verwerkt de bronsequentie; de decoder genereert autoregressief de doelsequentie.

## Beperkingen
- Het model heeft O(n^2) complexiteit in de sequentielengte door self-attention, wat problemen geeft bij zeer lange sequenties
- Positional encoding is beperkt in het vastleggen van complexe positierelaties
- Op het moment van publicatie alleen getest op NLP-taken (vertaling en parsing)

## Gerelateerde bronnen
- [[devlin_2019_bert]] — bouwt direct voort op de Transformer-encoder voor bidirectionele pre-training
- [[dosovitskiy_2020_vision_transformer]] — past de Transformer-architectuur toe op beeldherkenning
- [[li_2019_logsparse_transformer_time_series]] — past de Transformer aan voor tijdreeksvoorspelling, lost O(n^2) geheugenprobleem op
- [[wu_2020_deep_transformer_influenza]] — past de Transformer direct toe op tijdreeksdata

## Bronvermelding (APA 7e editie)
Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems*, *30*, 5998-6008. https://doi.org/10.48550/arXiv.1706.03762
