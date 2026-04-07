# Temporal Tensor Benchmark

Benchmark-framework om te onderzoeken hoe goed transformer-achtige modellen temporele patronen kunnen leren uit **3D-tensordata** (subject x tijd x features), zonder de tijdsdimensie plat te slaan naar statische features.

## Probleemstelling

In traditionele data science worden tijdreeksen vaak "plat geslagen" naar features (bijv. gemiddelde omzet afgelopen 12 maanden, aantal events in kwartaal X). Hierbij gaat temporele structuur verloren.

Dit project onderzoekt of modellen die direct op de 3D-structuur werken — zoals transformers — beter presteren, en welke patronen ze wel en niet kunnen oppikken.

## Aanpak

1. **Mock data genereren** met een 3D-structuur: `[N_subjects, T_timesteps, F_features]`
2. **Gecontroleerde trends injecteren** van toenemende complexiteit:
   - Eenvoudig: als event X voorkomt → label Y
   - Gemiddeld: als numerieke variabele stijgt over tijd → label Y
   - Complex: combinaties van events, trends en interacties
3. **Modellen trainen** (transformer-gebaseerd) op de ruwe tensordata
4. **Evalueren** welke trendcomplexiteit het model kan leren

## Voorbeelddomein

Een burger bij de Belastingdienst:
- **Events over tijd:** aangifte doen, te laat betalen, deelbetaling, rechtsvorm wijzigen
- **Numerieke variabelen over tijd:** omzet, aantal werknemers, winst
- **Label:** bijv. fraudeur / niet-fraudeur

## Projectstructuur

```
temporal-tensor-benchmark/
├── src/temporal_tensor_benchmark/   # Broncode
│   ├── data/                        # Mock data generatie
│   ├── models/                      # Model architecturen
│   └── evaluation/                  # Evaluatie & visualisatie
├── tests/                           # Unit tests
├── tests/integration/               # Integratietests
├── docs/literatuur/                 # Literatuurstudie
├── notebooks/                       # Experimenten & analyse
├── .github/workflows/               # CI/CD
└── requirements.txt
```

## Installatie

```bash
pip install -r requirements.txt
```

## Tests

```bash
pytest --tb=short
```

## Licentie

MIT
