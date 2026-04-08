---
title: "Self-Attentive Hawkes Process"
authors: ["Zhang, Q.", "Lipani, A.", "Kirnap, O.", "Yilmaz, E."]
year: 2020
doi: ""
journal: "ICML 2020"
open_access_url: "https://arxiv.org/abs/1907.07561"
type: wetenschappelijk
tags: [literatuur, wetenschappelijk, event-sequentie, hawkes-proces, self-attention, continue-intensiteit]
---

# Self-Attentive Hawkes Process (SAHP)

## Samenvatting
SAHP past self-attention toe op Hawkes-processen met een innovatieve temporele encoding: in plaats van standaard positie-embeddings gebruikt SAHP **Time Shifted Positional Encoding** waarbij de werkelijke tijdsintervallen als faseverschuivingen in sinusodale functies worden gecodeerd. De intensiteitsfunctie wordt gemodelleerd met geleerde parameters (basis-intensiteit mu, piek-intensiteit eta, en verval-snelheid gamma) die via een niet-lineaire transformatie van de attention-gewogen geschiedenis worden berekend. Het model ondersteunt zowel excitatie als inhibitie van event-types.

## Sleutelconclusies
- Tijds-bewuste positie-encoding (fase-verschuiving op basis van werkelijke tijdsintervallen) is effectiever dan standaard positie-encoding
- De intensiteitsfunctie combineert basis-, piek- en verval-parameters geleerd via attention
- Attention-gewichten zijn direct interpreteerbaar: ze tonen type-naar-type event-invloeden
- Eerste werk dat self-attention succesvol toepast op Hawkes-processen

## Methodologie
Experimenten op synthetische data, MIMIC-II, financiële data. Vergelijking met RMTPP, NHP, en andere neurale puntproces-modellen.

## Data & Techniek

### Gebruikte technieken
Self-attention met time-shifted positional encoding, parametrische intensiteitsfunctie (mu, eta, gamma).

### Inputdata
Event-sequenties: reeksen van `(event_type v_i, tijdstip t_i)` paren. Long format.

### Preprocessing
Chronologische ordening van events. Event-types als categorische variabelen.

### Preprocessing-problemen & oplossingen
_Niet vermeld_

### Datapipeline & modelinput
**Concrete embedding-formules:**

**Event-type embedding:**
```
tp_v = e_v * W_E  — one-hot naar dense embedding
```

**Time Shifted Positional Encoding:**
```
pe(v_i, t_i)[k] = sin(omega_k * i + w_k * t_i)
```
Waarbij omega_k de frequentie is, i de positie, en w_k de tijdstip t_i omzet naar een faseverschuiving. Dit codeert ZOWEL de positie in de sequentie ALS het werkelijke tijdsinterval.

**Gecombineerde embedding:**
```
x_i = tp_v + pe(v_i, t_i)  ∈ R^d
```

**Intensiteitsfunctie:**
```
lambda_u(t) = softplus(mu + (eta - mu) * exp(-gamma * (t - t_i)))
```
Met mu (basis), eta (piek) en gamma (verval) geleerd via attention-gewogen transformatie.

**Relevantie voor ons project:** SAHP's tijds-bewuste encoding is relevant als we events met onregelmatige tijdsintervallen willen modelleren. De faseverschuiving-aanpak biedt een elegante manier om de afstand tussen events te coderen. Net als THP is het beperkt tot categorische event-types zonder numerieke attributen.

## Beperkingen
- Alleen categorische events — geen numerieke marks of attributen
- Geen ondersteuning voor continue variabelen naast events
- Beperkt tot puntprocessen — geen gecombineerde modellering van events + tijdreeksen

## Gerelateerde bronnen
- [[zuo_2020_transformer_hawkes]] — vergelijkbaar maar met standaard sinusodale encoding
- [[tipirneni_2022_strats]] — combineert events en numerieke waarden in triplet-representatie
- [[choi_2016_retain]] — EHR event-sequentie modellering

## Bronvermelding (APA 7e editie)
Zhang, Q., Lipani, A., Kirnap, O., & Yilmaz, E. (2020). Self-attentive Hawkes process. *Proceedings of the 37th International Conference on Machine Learning (ICML)*, 11183-11193. https://arxiv.org/abs/1907.07561
