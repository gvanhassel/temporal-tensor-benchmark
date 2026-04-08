# Literatuurstudie — Temporal Tensor Benchmark

## Onderzoeksvragen

### Hoofdvraag
Hoe goed kunnen transformer-gebaseerde modellen patronen leren uit 3D-tensordata (subject x tijd x features) zonder feature engineering op de tijdsdimensie?

### Deelvragen

1. **Welke modelarchitecturen zijn geschikt voor 3D temporele tensordata?**
2. **Hoe worden event-sequenties en numerieke tijdreeksen gecombineerd in één model?**
3. **Welke benchmarks bestaan er voor temporele patroonherkenning?**
4. **Hoe genereer je synthetische temporele data met controleerbare complexiteit?**
5. **Hoe meet je welke patronen een model wel/niet heeft geleerd?**

## Structuur

```
docs/literatuur/
├── README.md                    # Dit bestand
├── tijdlijn.md                  # Tijdlijn-overzicht met alle verbindingen
├── papers/                      # 31 individuele paper-notities
│   ├── vaswani_2017_attention_is_all_you_need.md
│   ├── ...
│   └── vallarino_2025_hybrid_fraud_detection.md
└── overzichten/                 # 4 deeloverzichten per thema
    ├── overzicht_transformers_3d_temporele_tensordata.md
    ├── overzicht_transformer_architecturen_tijdreeksen.md
    ├── overzicht_transformers_event_sequenties_classificatie.md
    └── overzicht_synthetische_tijdreeksgeneratie_benchmarking.md
```

## Papers per thema

### 1. Fundament: Transformer-architectuur & aftakkingen (5 papers)
| Paper | Jaar | Kernbijdrage |
|-------|------|-------------|
| [Vaswani et al.](papers/vaswani_2017_attention_is_all_you_need.md) | 2017 | Originele Transformer — self-attention vervangt recurrence |
| [Devlin et al.](papers/devlin_2019_bert.md) | 2019 | BERT — bidirectionele pre-training + fine-tuning paradigma |
| [Dosovitskiy et al.](papers/dosovitskiy_2020_vision_transformer.md) | 2020 | Vision Transformer — patchificatie voor niet-tekstuele data |
| [Li et al.](papers/li_2019_logsparse_transformer_time_series.md) | 2019 | LogSparse Transformer — eerste aanpassing voor tijdreeksen |
| [Wu et al.](papers/wu_2020_deep_transformer_influenza.md) | 2020 | Deep Transformer — multivariate tijdreeks toepassing |

### 2. Transformer-architecturen voor tijdreeksen (6 papers)
| Paper | Jaar | Kernbijdrage |
|-------|------|-------------|
| [Zhou et al.](papers/zhou_2021_informer.md) | 2021 | Informer — ProbSparse attention, O(L log L) |
| [Wu et al.](papers/wu_2021_autoformer.md) | 2021 | Autoformer — Auto-Correlation, seizoen-trend decompositie |
| [Zhou et al.](papers/zhou_2022_fedformer.md) | 2022 | FEDformer — frequentiedomein-attention (Fourier/Wavelet) |
| [Nie et al.](papers/nie_2023_patchtst.md) | 2023 | PatchTST — patching + channel-independence + pre-training |
| [Zhang & Yan](papers/zhang_2023_crossformer.md) | 2023 | Crossformer — Two-Stage Attention (cross-time + cross-dimension) |
| [Zeng et al.](papers/zeng_2023_dlinear.md) | 2023 | DLinear — kritisch: simpel lineair model overtreft transformers |

### 3. Event-sequenties & heterogene temporele data (8 papers)
| Paper | Jaar | Kernbijdrage |
|-------|------|-------------|
| [Choi et al.](papers/choi_2016_retain.md) | 2016 | RETAIN — twee-niveau reverse time attention voor EHR |
| [Liu et al.](papers/liu_2018_heterogeneous_temporal_events.md) | 2018 | HE-LSTM — gate-mechanisme voor heterogene event-types |
| [Zuo et al.](papers/zuo_2020_transformer_hawkes_process.md) | 2020 | Transformer Hawkes Process — transformers voor event sequences |
| [Zhang et al.](papers/zhang_2020_self_attentive_hawkes.md) | 2020 | Self-Attentive Hawkes Process — attention voor event data |
| [Shchur et al.](papers/shchur_2021_neural_tpp_review.md) | 2021 | Review neural temporal point processes |
| [Huang et al.](papers/huang_2020_tabtransformer.md) | 2020 | TabTransformer — contextual embeddings voor tabular data |
| [Gorishniy et al.](papers/gorishniy_2021_ft_transformer.md) | 2021 | FT-Transformer — tokenisatie numeriek + categorisch |
| [Somepalli et al.](papers/somepalli_2021_saint.md) | 2021 | SAINT — intersample attention + contrastieve pre-training |

### 4. Fraudedetectie met sequentiële data (3 papers)
| Paper | Jaar | Kernbijdrage |
|-------|------|-------------|
| [Zhang et al.](papers/zhang_2018_sequential_fraud_detection.md) | 2018 | RNN + Markov Transition Field voor online fraude |
| [Min et al.](papers/min_2021_explainable_fraud_clustering.md) | 2021 | Bi-LSTM met time attention voor verklaarbare fraudedetectie |
| [Vallarino](papers/vallarino_2025_hybrid_fraud_detection.md) | 2025 | Mixture-of-Experts (RNN + Transformer + Autoencoder) |

### 5. Synthetische data & benchmarking (9 papers)
| Paper | Jaar | Kernbijdrage |
|-------|------|-------------|
| [Bandt & Pompe](papers/bandt_2002_permutation_entropy.md) | 2002 | Permutatie-entropie als complexiteitsmaat |
| [Bagnall et al.](papers/bagnall_2018_uea_multivariate.md) | 2018 | UEA multivariate tijdreeksclassificatie archief |
| [Dau et al.](papers/dau_2019_ucr_archive.md) | 2019 | UCR Time Series Archive — standaard benchmark |
| [Ismail Fawaz et al.](papers/ismail_fawaz_2019_dl_tsc_review.md) | 2019 | Review deep learning voor tijdreeksclassificatie |
| [Yoon et al.](papers/yoon_2019_timegan.md) | 2019 | TimeGAN — GAN voor tijdreeksgeneratie |
| [Kang et al.](papers/kang_2020_gratis.md) | 2020 | GRATIS — controleerbare tijdreeksgeneratie |
| [Lin et al.](papers/lin_2020_doppelganger.md) | 2020 | DoppelGANger — GAN voor multivariate tijdreeksen |
| [Yuan et al.](papers/yuan_2024_diffusion_ts.md) | 2024 | Diffusion-TS — diffusiemodel overtreft GANs |
| [Tan et al.](papers/tan_2025_syntsbench.md) | 2025 | SynTSBench — benchmark met programmeerbare patronen |
