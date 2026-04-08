---
title: "Multi-Time Attention Networks for Irregularly Sampled Time Series"
authors: ["Shukla, S. N.", "Marlin, B. M."]
year: 2021
doi: ""
journal: "ICLR 2021"
open_access_url: "https://arxiv.org/abs/2101.10318"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, onregelmatig, tijdreeksen, attention, interpolatie, continue-tijd]
---

# Multi-Time Attention Networks for Irregularly Sampled Time Series (mTAN)

## Samenvatting
mTAN introduceert een leerbare continue-tijdsembedding gekoppeld aan een time-attention mechanisme voor onregelmatig gesamplede multivariate tijdreeksen. Het kernidee: leer een embedding van continue tijdswaarden en gebruik attention om geobserveerde waarden te wegen op basis van temporele nabijheid. Dit vervangt vaste kernels (bijv. RBF) door een geleerde similarity-functie. Het model kan omgaan met variabelen die op verschillende tijdstippen worden geobserveerd (asynchrone sampling) en produceert een vaste-lengte representatie ongeacht het aantal observaties. Voortbouwend op eerder werk van Shukla & Marlin (2019) over interpolation-prediction networks.

## Sleutelconclusies
- Geleerde continue-tijdsembeddings zijn flexibeler dan vaste kernels voor temporele interpolatie
- Time-attention vervangt de noodzaak voor discretisatie of imputatie
- Het model kan variabelen op verschillende tijdstippen verwerken (partieel geobserveerde vectoren)
- Presteert state-of-the-art op interpolatie- en classificatietaken met onregelmatige data

## Methodologie
Experimenten op PhysioNet Challenge 2012, MIMIC-III, en synthetische datasets. Interpolatie- en classificatietaken. Vergelijking met GRU-D, ODE-RNN, IP-Nets, latent ODE.

## Data & Techniek

### Gebruikte technieken
Time-attention mechanisme, leerbare continue-tijdsembedding (sinusoidaal + lineair), encoder-decoder architectuur.

### Inputdata
Onregelmatig gesamplede multivariate tijdreeksen: `s_dn = (t_dn, x_dn)` per dimensie d en patiënt n, met variabel aantal observaties L_dn per dimensie.

### Preprocessing
Geen vaste tijdsgrid of imputatie nodig. Observaties worden direct als (tijd, waarde) paren ingevoerd.

### Preprocessing-problemen & oplossingen
- **Asynchrone observaties**: Verschillende variabelen op verschillende tijdstippen → opgelost door per-dimensie time-attention
- **Variabel aantal observaties**: → opgelost door attention-gewogen aggregatie naar vaste dimensie

### Datapipeline & modelinput
**Continue-tijdsembedding:**
```
phi_h(t)[i] = {
    omega_0h * t + alpha_0h,     als i = 0    (lineaire term)
    sin(omega_ih * t + alpha_ih), als 0 < i < d_r  (periodieke termen)
}
```
H verschillende embeddings van dimensie d_r per tijdstip, met leerbare frequentie (omega) en fase (alpha).

**Time-attention mechanisme:**
```
kappa_h(t, t_id) = softmax(phi_h(t) * W_v^T * phi_h(t_id)^T / sqrt(d_k))
```
Berekent similarity tussen querytijd t en geobserveerde tijden t_id.

**Interpolatie:**
```
x_hat_hd(t, s) = sum_i kappa_h(t, t_id) * x_id
```
Gewogen gemiddelde van geobserveerde waarden, gewogen door temporele attention.

**Tensorshapes:**
- Time embeddings per observatie: `R^(H x d_r)`
- Interpolatie-output per querytijd: `R^J` (vaste dimensie via lineaire combinatie)
- Uiteindelijke sequentie: vaste-lengte representatie ongeacht input-irregulariteit

**Relevantie voor ons project:** mTAN biedt een elegante oplossing voor het **interpolatie-probleem**: hoe maak je van onregelmatig geobserveerde waarden een vaste representatie op gewenste tijdpunten? Dit is relevant als we events en numerieke waarden op verschillende tijdstippen hebben en toch een uniforme tijdsgrid willen. Echter, mTAN behandelt alle variabelen als numeriek — er is geen native categorische ondersteuning.

## Beperkingen
- Alle variabelen worden als numeriek behandeld
- Geen expliciete ondersteuning voor categorische features of events
- De interpolatie-aanpak is minder geschikt voor discrete events (aangifte doen is geen continue waarde)
- Complexiteit schaalt met het aantal observaties en het aantal query-tijdpunten

## Gerelateerde bronnen
- [[tipirneni_2022_strats]] — vergelijkbare triplet-aanpak maar met Transformer i.p.v. attention-interpolatie
- [[wang_2020_mimic_extract]] — MIMIC-III data pipeline (wide format output)
- [[lee_2026_star_set_transformer]] — recente verbetering van set-gebaseerde aanpak met variable-type biases

## Bronvermelding (APA 7e editie)
Shukla, S. N., & Marlin, B. M. (2021). Multi-time attention networks for irregularly sampled time series. *ICLR 2021*. https://arxiv.org/abs/2101.10318
