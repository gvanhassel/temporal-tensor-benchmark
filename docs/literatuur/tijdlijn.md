# Tijdlijn: Van Transformer naar Temporele 3D-Tensordata

Dit document toont de evolutie van de Transformer-architectuur en hoe deze zich vertakt heeft
van NLP naar tijdreeksen, event-sequenties, tabulaire data en synthetische benchmarks.

## Visueel overzicht

```
2017  TRANSFORMER (Vaswani et al.)
      │ "Attention Is All You Need"
      │ Self-attention vervangt recurrence volledig
      │
      ├──────────────────────────────────────────────────────────────┐
      │                                                              │
      ▼ NLP-tak                                                      │
2019  BERT (Devlin et al.)                                           │
      │ Bidirectionele pre-training + fine-tuning                    │
      │ → Masked modeling paradigma                                  │
      │                                                              │
      │  ┌───────────────────────────────────────────────┐           │
      │  │ Invloed op pre-training strategieën:          │           │
      │  │ PatchTST (2023) gebruikt masked patching      │           │
      │  │ SAINT (2021) gebruikt contrastief pre-trainen │           │
      │  └───────────────────────────────────────────────┘           │
      │                                                              │
      ▼ Vision-tak                                                   │
2020  VISION TRANSFORMER (Dosovitskiy et al.)                        │
      │ Beelden → patches → tokens                                   │
      │ → Patchificatie-concept voor niet-tekstuele data             │
      │                                                              │
      │  ┌────────────────────────────────────────────┐              │
      │  │ Invloed op tokenisatie:                    │              │
      │  │ PatchTST: tijdreeks → patches → tokens    │              │
      │  │ FT-Transformer: features → tokens         │              │
      │  │ Crossformer: DSW embedding                 │              │
      │  └────────────────────────────────────────────┘              │
      │                                                              │
      ▼ Tijdreeks-tak (begint parallel)                              │
2019  LOGSPARSE TRANSFORMER (Li et al.) ◄────────────────────────────┘
      │ Eerste Transformer specifiek voor tijdreeksen
      │ Convolutional self-attention + LogSparse attention
      │ Probleem: O(n²) geheugen bij lange reeksen
      │
      ├─────────────────────────┐
      │                         │
      ▼                         ▼
2020  WU et al.                TRANSFORMER HAWKES PROCESS (Zuo et al.)
      │ Deep Transformer       │ Transformers voor event-sequenties
      │ voor influenza         │ Continu-tijd positional encoding
      │ (multivariate)         │
      │                        ▼
      │                   2020  SELF-ATTENTIVE HAWKES (Zhang et al.)
      │                        │ Attention direct op event data
      │                        │
      │                        ▼
      │                   2021  NEURAL TPP REVIEW (Shchur et al.)
      │                        │ Overzicht temporal point processes
      │                        │ → Basis voor event-modellering
      │                         
      ▼
2021  INFORMER (Zhou et al.) ─── AAAI 2021 Best Paper
      │ ProbSparse attention → O(L log L)
      │ Generatieve decoder voor lange voorspellingen
      │
      ├──────────────────────────────┐
      │                              │
      ▼                              ▼
2021  AUTOFORMER (Wu et al.)    2022  FEDFORMER (Zhou et al.)
      │ NeurIPS 2021                  │ ICML 2022
      │ Auto-Correlation              │ Frequentiedomein attention
      │ Seizoen-trend decompositie    │ Fourier/Wavelet basis
      │ in de architectuur            │ O(L) complexiteit
      │                              │
      └──────────┬───────────────────┘
                 │
                 ▼
2023  PATCHTST (Nie et al.) ─── ICLR 2023
      │ Combineert:
      │ • Patching (van ViT)
      │ • Channel-independence
      │ • Self-supervised pre-training (van BERT)
      │ → State-of-the-art tijdreeksvoorspelling
      │
      ├──────────────────────────────┐
      │                              │
      ▼                              ▼
2023  CROSSFORMER                 2023  DLINEAR (Zeng et al.)
      (Zhang & Yan)                    │ AAAI 2023
      │ ICLR 2023                      │ ⚠ KRITISCH PAPER:
      │ Two-Stage Attention:           │ Simpel lineair model
      │ • Cross-time                   │ overtreft alle
      │ • Cross-dimension             │ Transformer-varianten
      │ DSW embedding                  │ op forecasting
      │                              │
      │ → Meest relevant voor         │ → Essentiële baseline
      │   3D tensordata               │   voor elk experiment
      │   (2D → 3D uitbreidbaar)      │
```

## Parallelle tak: Tabulaire data & heterogene features

```
2016  RETAIN (Choi et al.) ─── NeurIPS 2016
      │ Reverse time attention voor EHR-data
      │ Twee-niveau: bezoek-niveau + variabele-niveau
      │ → Interpreteerbaarheid via attention weights
      │
      ▼
2018  HE-LSTM (Liu et al.) ─── AAAI 2018
      │ Gate-mechanisme voor heterogene event-types
      │ Verschillende event-frequenties in één model
      │
      ├──────────────────────────────┐
      │                              │
      ▼                              ▼
2020  TABTRANSFORMER              2021  FT-TRANSFORMER
      (Huang et al.)                    (Gorishniy et al.)
      │ Contextual embeddings           │ NeurIPS 2021
      │ voor categorische features      │ Feature Tokenizer:
      │                                │ numeriek + categorisch
      │                                │ → tokens
      │                                │
      └──────────┬───────────────────┘
                 │
                 ▼
2021  SAINT (Somepalli et al.)
      │ Intersample attention
      │ Contrastieve pre-training
      │ → Relaties tussen samples leren
```

## Parallelle tak: Fraudedetectie

```
2018  ZHANG et al. ─── KDD Workshop
      │ RNN + Markov Transition Field
      │ Sequentiële patronen in transacties
      │
      ▼
2021  MIN et al. ─── AAAI Workshop
      │ Bi-LSTM + time attention
      │ Verklaarbare fraudedetectie
      │
      ▼
2025  VALLARINO ─── arXiv
      │ Mixture-of-Experts
      │ RNN + Transformer + Autoencoder
      │ → Huidige state-of-the-art
```

## Parallelle tak: Synthetische data & benchmarking

```
2002  PERMUTATIE-ENTROPIE (Bandt & Pompe)
      │ Complexiteitsmaat voor tijdreeksen
      │ → Objectieve moeilijkheidsgraad
      │
      ▼
2018  UEA ARCHIVE (Bagnall et al.)     2019  UCR ARCHIVE (Dau et al.)
      │ 30 multivariate datasets              │ 128 univariate datasets
      │                                      │ Standaard benchmark
      │                                      │
      └──────────┬───────────────────────────┘
                 │
                 ▼
2019  DEEP LEARNING TSC REVIEW (Ismail Fawaz et al.)
      │ Systematisch overzicht DL voor tijdreeksclassificatie
      │ ResNet en FCN als baselines
      │
      ├──────────────────────────────┐
      │                              │
      ▼                              ▼
2019  TIMEGAN (Yoon et al.)     2020  DOPPELGANGER (Lin et al.)
      │ NeurIPS 2019                  │ GAN voor multivariate
      │ GAN + autoregressive          │ tijdreeksen met metadata
      │ voor tijdreeksgeneratie       │
      │                              │
      └──────────┬───────────────────┘
                 │
                 ▼
2020  GRATIS (Kang et al.)
      │ Controleerbare generatie
      │ Mixture autoregressive modellen
      │ Systematisch varieerbare parameters
      │
      ▼
2024  DIFFUSION-TS (Yuan et al.) ─── ICLR 2024
      │ Diffusiemodel overtreft GANs
      │ Seizoen-trend decompositie + Fourier loss
      │
      ▼
2025  SYNTSBENCH (Tan et al.) ─── NeurIPS 2025
      │ ⭐ MEEST RELEVANT VOOR DIT PROJECT
      │ Benchmark met programmeerbare patronen
      │ Toenemende complexiteit
      │ → Exact ons doel: welke patronen kan DL leren?
```

## Convergentie: wat dit project nodig heeft

De literatuur convergeert naar een architectuur die elementen combineert uit meerdere takken:

```
                    ┌─────────────────────────────────────┐
                    │   TEMPORAL TENSOR BENCHMARK MODEL   │
                    │   (subject x tijd x features)       │
                    └─────────────┬───────────────────────┘
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
              ▼                   ▼                   ▼
     Feature Tokenizer    Temporele Encoder    Cross-Subject
     (FT-Transformer)     (PatchTST-stijl)    Attention
              │                   │            (SAINT-stijl)
              │                   │                   │
              ▼                   ▼                   ▼
     Numeriek+categorisch  Patching over      Relaties tussen
     per tijdstip → tokens tijdstappen        subjects leren
              │                   │                   │
              └───────────────────┼───────────────────┘
                                  │
                    ┌─────────────▼───────────────────────┐
                    │   Multi-dimensionale Attention       │
                    │   (Crossformer Two-Stage → 3-Stage)  │
                    │   1. Cross-time attention            │
                    │   2. Cross-feature attention         │
                    │   3. Cross-subject attention         │
                    └─────────────┬───────────────────────┘
                                  │
                    ┌─────────────▼───────────────────────┐
                    │   Classificatie-head                 │
                    │   + DLinear als baseline             │
                    └─────────────────────────────────────┘
```

## Kennislacunes (open onderzoeksvragen)

1. **Geen bestaand model combineert alle drie dimensies** — Crossformer doet 2D (tijd x features), maar de subject-dimensie ontbreekt
2. **Pre-training voor 3D tensors is ononderzocht** — masked time-step, masked feature, en masked subject prediction zijn open vragen
3. **Positional encoding voor 3D structuren** — sinusvormige encodings werken voor 1D, maar 3D vereist nieuwe aanpakken
4. **Event-integratie met numerieke tijdreeksen** — THP/SAHP werken met pure events, FT-Transformer met pure tabular; de combinatie is schaars
5. **Complexiteitsmeting** — permutatie-entropie werkt voor 1D; uitbreiding naar multivariate 3D patronen is open

## Aanbevolen leesroute

1. Start: [Vaswani 2017](papers/vaswani_2017_attention_is_all_you_need.md) → begrijp self-attention
2. Dan: [PatchTST 2023](papers/nie_2023_patchtst.md) → hoe transformers werken op tijdreeksen
3. Dan: [Crossformer 2023](papers/zhang_2023_crossformer.md) → multi-dimensionale attention
4. Dan: [FT-Transformer 2021](papers/gorishniy_2021_ft_transformer.md) → mixed features tokeniseren
5. Dan: [DLinear 2023](papers/zeng_2023_dlinear.md) → kritisch perspectief, baseline nodig
6. Dan: [SynTSBench 2025](papers/tan_2025_syntsbench.md) → benchmarking methodologie
7. Tot slot: [GRATIS 2020](papers/kang_2020_gratis.md) + [Permutatie-entropie 2002](papers/bandt_2002_permutation_entropy.md) → data generatie
