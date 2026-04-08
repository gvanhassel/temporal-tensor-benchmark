---
title: "Literatuuroverzicht: Feature-dimensie organisatie voor 3D temporele tensordata met mixed data types"
onderwerp: "Feature-dimensie organisatie voor 3D temporele tensordata (subject x tijd x features) met mixed data types"
aantal_bronnen: 14
type: overzicht
tags: [overzicht, literatuur, tensorrepresentatie, mixed-types, temporeel, transformer]
datum: 2026-04-07
---

# Literatuuroverzicht: Feature-dimensie organisatie voor 3D temporele tensordata met mixed data types

## Inleiding
Dit overzicht onderzoekt hoe de feature-dimensie het beste kan worden georganiseerd voor 3D temporele tensordata `(subject x tijd x features)` wanneer de features een mix zijn van events (categorisch), numerieke variabelen en categorische variabelen die over de tijd veranderen. Het concrete toepassingsdomein is overheidsdata (bijv. Belastingdienst) met burgers als subjects, tijdstappen, en per tijdstap zowel events (aangifte doen, te laat betalen) als numerieke veranderingen (omzet, werknemers). De kernvraag is: wide format (elke feature een kolom) vs. long/tokenized format (variabel aantal observaties per tijdstap) vs. hybride aanpakken.

## Samenvatting van de literatuur

De literatuur onthult **vier fundamenteel verschillende representatie-paradigma's** voor temporele data met mixed types, elk met eigen sterktes en zwaktes:

### Paradigma 1: Wide Format / Dense Matrix
**Representatie:** `(N subjects, T tijdstappen, D features)` — vaste 3D tensor.

Dit is de aanpak van **MIMIC-Extract** ([[wang_2020_mimic_extract]]), **Informer** ([[zhou_2021_informer]]), **PatchTST** ([[nie_2022_patchtst]]) en **Crossformer** ([[zhang_2023_crossformer]]). Alle features worden op elk tijdstip in een vaste vector geplaatst. Events worden binaire indicatoren (0/1), numerieke waarden worden direct opgenomen. Dit is computationeel eenvoudig maar leidt tot extreme sparsiteit: MIMIC-III heeft 89.7% missingness in wide format. De tijdreeks-Transformers (PatchTST, Crossformer, Informer) zijn ontworpen voor puur numerieke data en bieden geen native ondersteuning voor mixed types.

Het verschil tussen PatchTST (channel-independent: elke feature apart verwerkt) en Crossformer (channel-dependent: expliciete cross-feature attention via Two-Stage Attention) illustreert een belangrijke ontwerpkeuze: moeten features onafhankelijk of gezamenlijk worden verwerkt?

### Paradigma 2: Tokenized Long Format / Sequentie van Tokens
**Representatie:** Sequentie van tokens, elk een concept/event, gescheiden door speciale tokens.

Dit is de aanpak van **BEHRT** ([[li_2020_behrt]]) en **CEHR-BERT** ([[pang_2021_cehr_bert]]). Medische codes worden als NLP-tokens behandeld. CEHR-BERT voegt **Artificiële Tijd-Tokens (ATT)** toe: W_0-W_3 (weken), M_1-M_11 (maanden), LT (>1 jaar) om tijdsintervallen te coderen. Bezoekgrenzen worden gemarkeerd met VS/VE tokens. De volledige sequentie: `[VS] concept_1 concept_2 [VE] [ATT:M_3] [VS] concept_3 [VE] ...`

Dit paradigma is elegant voor puur categorische events maar heeft geen plek voor numerieke waarden. RETAIN ([[choi_2016_retain]]) gebruikt een vergelijkbare aanpak maar met multi-hot vectoren per bezoek in plaats van individuele tokens.

### Paradigma 3: Set van Observatie-Triplets
**Representatie:** `{(t_i, f_i, v_i)}` — set van (tijdstip, variabele-identifier, waarde) triplets.

Dit is de aanpak van **STraTS** ([[tipirneni_2022_strats]]), **mTAN** ([[shukla_2021_mtan]]), en **STAR** ([[lee_2026_star_set_transformer]]). Elke observatie is een triplet met continue tijdstip, categorische variabele-identifier, en numerieke waarde. De Continuous Value Embedding (CVE) van STraTS embedt scalaire waarden via een geleerd feedforward-netwerk: `FFN(x) = U * tanh(W*x + b)`.

**Dit paradigma is het meest geschikt voor ons probleem** omdat het native mixed types ondersteunt:
- Events: triplet `(tijdstip, "event_aangifte", 1.0)`
- Numerieke waarden: triplet `(tijdstip, "omzet", 150000.0)`
- De variabele-identifier `f` krijgt een lookup-table embedding
- De waarde `v` krijgt een CVE-embedding

STAR (2026) verbetert STraTS door structurele priors terug te brengen via attention biases: temporele nabijheid (`-|Δt|/τ`) en variable-type affiniteit (geleerde compatibiliteitsmatrix).

### Paradigma 4: Twee-Niveau Feature Tokenisatie + Temporele Sequentie
**Representatie:** Per tijdstap een getokeniseerde feature-set, over de tijd een sequentie.

Dit is de aanpak van **UniTTab** ([[luetto_2023_unittab]]) en bouwt voort op **FT-Transformer** ([[gorishniy_2021_ft_transformer]]). Elke feature — numeriek of categorisch — wordt getokeniseerd naar een d-dimensionale embedding. De FT-Transformer-formules:
- Numeriek: `T_j = b_j + x_j * W_j` (lineaire projectie)
- Categorisch: `T_j = b_j + e_j^T * W_j` (lookup-table)

UniTTab stapelt hierop een Sequence Transformer: een Field Transformer verwerkt features binnen een tijdstap, en een Sequence Transformer verwerkt de sequentie van tijdstappen. Numerieke waarden worden geëmbed via frequentie-functies (NeRF-stijl): `γ(v) = (sin(2^0πv), cos(2^0πv), ...)`.

**Dit paradigma combineert de voordelen van wide en long format**: elke tijdstap heeft een getokeniseerde feature-set (wide), maar de tokenisatie maakt mixed types native mogelijk, en variabele rij-structuren worden ondersteund via per-type projectiematrices.

### Event-sequentie modellen
**Transformer Hawkes Process** ([[zuo_2020_transformer_hawkes]]) en **SAHP** ([[zhang_2020_sahp]]) modelleren puur categorische event-sequenties op continue tijdstippen. Events worden geëmbed via type-embedding + temporele encoding (sinusoidaal of fase-verschoven). Deze modellen zijn relevant voor het event-deel van ons probleem maar ondersteunen geen bijbehorende numerieke attributen.

### Numerieke embedding-methoden
**Gorishniy et al. (2022)** ([[gorishniy_2022_numerical_embeddings]]) toont dat de keuze van numerieke embedding (lineair vs. periodiek vs. piecewise-linear) significant impact heeft op modelprestaties. Periodieke embeddings `sin(ω*x + φ)` met geleerde frequenties presteren vaak beter dan lineaire projectie.

## Belangrijkste bevindingen

### 1. De triplet-representatie (STraTS/STAR) is het meest geschikt voor mixed irregular temporal data
De triplet `(t, f, v)` representatie elimineert het sparsity-probleem van wide format, ondersteunt native mixed types, en vereist geen discretisatie of imputatie — onderbouwd door [[tipirneni_2022_strats]], [[lee_2026_star_set_transformer]], en indirect door [[shukla_2021_mtan]].

### 2. Feature tokenisatie (FT-Transformer/UniTTab) biedt de beste aanpak voor mixed-type embedding
Het tokeniseren van elke feature — numeriek via lineaire/periodieke/frequentie-projectie, categorisch via lookup-table — naar een uniforme d-dimensionale embedding is de meest effectieve strategie — onderbouwd door [[gorishniy_2021_ft_transformer]], [[luetto_2023_unittab]], en [[gorishniy_2022_numerical_embeddings]].

### 3. Twee-niveau verwerking (features + tijd) is de aanbevolen architectuur
Een Field/Feature Transformer die intra-tijdstap feature-interacties leert, gevolgd door een Sequence Transformer die temporele patronen leert, combineert de voordelen van beide dimensies — zie [[luetto_2023_unittab]].

### 4. Wide format is pragmatisch maar suboptimaal voor sparse mixed data
MIMIC-Extract ([[wang_2020_mimic_extract]]) toont dat wide format werkbaar is maar leidt tot 89.7% sparsiteit. PatchTST ([[nie_2022_patchtst]]) en Crossformer ([[zhang_2023_crossformer]]) werken goed voor dense numerieke tijdreeksen maar niet voor sparse mixed-type data.

### 5. Temporele encoding vereist speciale aandacht
Continue tijdsrepresentatie (CVE in STraTS, sinusoidale encoding in Hawkes-modellen, ATT-tokens in CEHR-BERT) is cruciaal voor irreguliere data. De keuze tussen geleerde (CVE, mTAN) en vaste (sinusoidaal) encodings is context-afhankelijk.

### 6. Channel-independence vs. channel-dependence is een open vraag
PatchTST toont dat onafhankelijke verwerking van features verrassend effectief is, maar Crossformer toont dat expliciete cross-feature attention waarde toevoegt. STAR's variable-type bias matrix is een elegante middenweg.

## Kennislacunes & aanbevelingen

1. **Geen enkel model combineert alle benodigde componenten**: Er is geen off-the-shelf architectuur die mixed types + temporele sequenties + event-sequenties + numerieke tijdreeksen combineert. UniTTab komt het dichtst in de buurt maar mist continue tijdsrepresentatie en expliciete event-modellering.

2. **Schaalbaarheid van triplet-representatie**: STraTS schaalt kwadratisch met het aantal observaties. Bij subjects met zeer veel events (duizenden per jaar) is windowing of subsampling nodig.

3. **Combinatie van event-modellen en tijdreeks-modellen**: THP/SAHP voor events en PatchTST/Crossformer voor numerieke tijdreeksen zijn gescheiden werelden. Een geïntegreerd model dat beide verwerkt ontbreekt.

4. **Validatie buiten medische domeinen**: Vrijwel alle mixed-type temporele modellen zijn getest op klinische data (MIMIC-III, PhysioNet). Validatie op administratieve/overheidsdata ontbreekt.

5. **Multi-categorische features**: De triplet-representatie behandelt waarden als scalair — multi-categorische features (bijv. sector met 20 opties) vereisen aparte embedding-strategieën.

## Conclusie

**Aanbevolen representatie voor ons project:** Een hybride aanpak die de **triplet/set-representatie van STraTS** combineert met de **feature tokenisatie van FT-Transformer/UniTTab**. Concreet:

1. **Per observatie**: een triplet `(tijdstip, feature_type, waarde)` waarbij feature_type een geleerde embedding krijgt en waarde via CVE of periodieke embedding wordt gecodeerd
2. **Optioneel**: groepeer observaties per tijdstap en verwerk intra-tijdstap interacties via een Field Transformer (UniTTab-stijl)
3. **Temporele verwerking**: Sequence Transformer met attention biases voor temporele nabijheid en variable-type affiniteit (STAR-stijl)

Dit combineert de flexibiliteit van long format (geen sparsity, variabel aantal observaties) met de rijke representatiecapaciteit van feature tokenisatie (mixed types native ondersteund).

## Gebruikte bronnen

### Wetenschappelijke bronnen

**Tijdreeks-Transformers (wide format, numeriek):**
1. [[nie_2022_patchtst]] — Nie et al. (2023) — Channel-independent patching Transformer
2. [[zhang_2023_crossformer]] — Zhang & Yan (2023) — Cross-dimension dependency Transformer
3. [[zhou_2021_informer]] — Zhou et al. (2021) — Efficient Transformer voor lange sequenties

**Tabular Feature Tokenisatie (mixed types, geen temporeel):**
4. [[gorishniy_2021_ft_transformer]] — Gorishniy et al. (2021) — FT-Transformer met Feature Tokenizer
5. [[huang_2020_tabtransformer]] — Huang et al. (2020) — TabTransformer voor categorische embeddings
6. [[gorishniy_2022_numerical_embeddings]] — Gorishniy et al. (2022) — Numerieke embedding-methoden

**EHR-modellen (events/codes, tokenized):**
7. [[choi_2016_retain]] — Choi et al. (2016) — RETAIN met multi-hot encoding
8. [[li_2020_behrt]] — Li et al. (2020) — BEHRT: BERT voor medische codes
9. [[pang_2021_cehr_bert]] — Pang et al. (2021) — CEHR-BERT met artificiële tijd-tokens

**Irregulair temporeel + mixed types (triplet/set):**
10. [[tipirneni_2022_strats]] — Tipirneni & Reddy (2022) — STraTS: triplet-representatie + CVE
11. [[shukla_2021_mtan]] — Shukla & Marlin (2021) — Multi-Time Attention Networks
12. [[lee_2026_star_set_transformer]] — Lee et al. (2026) — STAR: attention biases voor sets

**Event-sequentie modellen (Hawkes-processen):**
13. [[zuo_2020_transformer_hawkes]] — Zuo et al. (2020) — Transformer Hawkes Process
14. [[zhang_2020_sahp]] — Zhang et al. (2020) — Self-Attentive Hawkes Process

**Heterogene temporele tabular data (mixed types + temporeel):**
15. [[luetto_2023_unittab]] — Luetto et al. (2025) — UniTTab: twee-niveau Transformer

**Data-pipelines (preprocessing):**
16. [[wang_2020_mimic_extract]] — Wang et al. (2020) — MIMIC-Extract pipeline
