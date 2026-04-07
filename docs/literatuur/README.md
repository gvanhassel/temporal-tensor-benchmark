# Literatuurstudie — Temporal Tensor Benchmark

## Onderzoeksvragen

### Hoofdvraag
Hoe goed kunnen transformer-gebaseerde modellen patronen leren uit 3D-tensordata (subject x tijd x features) zonder feature engineering op de tijdsdimensie?

### Deelvragen

1. **Welke modelarchitecturen zijn geschikt voor 3D temporele tensordata?**
   - Transformers voor tijdreeksen (PatchTST, Informer, Autoformer, etc.)
   - Sequence-to-label modellen met attention
   - Vergelijking met traditionele aanpakken (LSTM, GRU, 1D-CNN)

2. **Hoe worden event-sequenties en numerieke tijdreeksen gecombineerd in één model?**
   - Mixed-type embeddings (categorisch + numeriek)
   - Multi-modal temporele architecturen
   - Tokenisatiestrategieën voor heterogene tijdreeksen

3. **Welke benchmarks bestaan er voor temporele patroonherkenning?**
   - UEA/UCR tijdreeksclassificatie
   - Bestaande synthetische benchmarks
   - Vergelijkbare fraud-detection / anomaly-detection benchmarks

4. **Hoe genereer je synthetische temporele data met controleerbare complexiteit?**
   - Data-generatie frameworks (TimeGAN, DoppelGANger)
   - Handmatige trend-injectie methoden
   - Complexiteitsmaten voor temporele patronen

5. **Hoe meet je welke patronen een model wel/niet heeft geleerd?**
   - Attention-visualisatie en interpretability
   - Ablation studies op geïnjecteerde trends
   - Probing classifiers

## Papers

Gevonden papers worden opgeslagen in deze map als Markdown-notities met het format:
`{auteur}_{jaar}_{korte_titel}.md`

Elke notitie bevat:
- Referentie (APA)
- Kernidee (max 3 zinnen)
- Relevantie voor dit project
- Bruikbare methoden/inzichten
- Link naar paper
