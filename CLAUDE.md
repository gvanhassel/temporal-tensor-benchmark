# Projectcontext

## Taal

Projectdocumentatie is in het Nederlands.

## Ontwikkeling & GitHub Issues — Werkwijze

Elke codewijziging is gekoppeld aan een GitHub issue. Dit is de vaste werkwijze:

### 1. Issue eerst
Voordat er code wordt geschreven of gewijzigd, bestaat er altijd een issue. Maak het aan via:
```
gh issue create --title "..." --body "..." --label "..."
```

**Labels:**
| Label | Wanneer |
|-------|---------|
| `bug` | Iets werkt niet zoals verwacht |
| `enhancement` | Nieuwe functionaliteit |
| `refactor` | Code verbeteren zonder gedragswijziging |
| `documentation` | Alleen documentatie |
| `research` | Onderzoek of verkenning, nog geen code |
| `chore` | Onderhoud, dependencies, CI/CD |

### 2. Branch per issue
Werk op een branch die verwijst naar het issue.

**Naamconventie:** `issue-{nummer}-{korte-beschrijving}`

**Belangrijk:**
- Werk **nooit** direct op `main` — altijd via een branch
- Elke nieuwe programmeeropdracht → nieuw issue → nieuwe branch

### 3. Conventional Commits
Elk commit-bericht volgt de [Conventional Commits](https://www.conventionalcommits.org/) standaard:

```
<type>(<scope>): <omschrijving>

[optionele body]

[optionele footer, bijv. Closes #42]
```

**Types:**
| Type | Gebruik |
|------|---------|
| `fix:` | Bugfix — verhoogt patch-versie (1.0.**1**) |
| `feat:` | Nieuwe feature — verhoogt minor-versie (1.**1**.0) |
| `refactor:` | Herstructurering zonder gedragswijziging |
| `test:` | Alleen tests toevoegen of aanpassen |
| `docs:` | Alleen documentatie |
| `chore:` | Onderhoud, build, CI/CD |
| `ci:` | Wijzigingen aan pipelines of workflows |
| `BREAKING CHANGE:` | In de footer: verhoogt major-versie (**2**.0.0) |

### 4. Pull Request naar main
Na afronding: maak een PR aan die het issue sluit. Gebruik `Closes #42` in de PR-beschrijving of het laatste commit-bericht.

PR-titel volgt ook Conventional Commits: `feat(scope): omschrijving (#42)`

---

## Testen — Werkwijze

Elke functie of methode die wordt geschreven, krijgt direct een bijbehorende test.

### Pytest — unit tests
- Elke functie krijgt direct een `pytest`-test in `tests/`
- Bestandsnaamconventie: `test_{modulenaam}.py`
- Testfunctienamen beschrijven het gedrag: `test_bereken_totaal_geeft_nul_bij_lege_lijst()`
- Dek minimaal af: het happy path, edge cases, en ongeldige invoer

### Integratietests
- Schrijf een integratietest zodra twee of meer componenten samenwerken
- Integratietests staan in `tests/integration/`

### Committen en mergen
- **Committen met falende tests is toegestaan** — gebruik dan WIP-commit: `wip(#42): module half af, tests falen nog`
- **Mergen naar `main` met falende tests is niet toegestaan** — afgedwongen via GitHub Actions

---

## Projectomschrijving

Benchmark-framework om te onderzoeken hoe goed transformer-gebaseerde modellen temporele patronen kunnen leren uit 3D-tensordata (subject × tijd × features), zonder de tijdsdimensie plat te slaan naar statische features.

## Technische stack

- **Taal:** Python 3.11+
- **ML framework:** PyTorch
- **Testing:** pytest
- **CI:** GitHub Actions (`.github/workflows/ci.yml`)
- **Package:** installeerbaar via `pip install -e .` (pyproject.toml)

## Projectstructuur

```
src/temporal_tensor_benchmark/     # Broncode
├── data/                          # Mock data generatie
├── models/                        # Model architecturen
└── evaluation/                    # Evaluatie & visualisatie
tests/                             # Unit tests (pytest)
tests/integration/                 # Integratietests
docs/literatuur/                   # Literatuurstudie
├── papers/                        # 31 individuele paper-notities
├── overzichten/                   # 4 thematische deeloverzichten
└── tijdlijn.md                    # Tijdlijn transformer-evolutie
notebooks/                         # Experimenten & analyse
```

## Commando's

```bash
# Dependencies installeren
pip install -r requirements.txt
pip install -e .

# Tests draaien
pytest --tb=short
```

## Literatuurstudie

31 papers in `docs/literatuur/papers/`, georganiseerd in 5 thema's:
1. Fundament (Transformer, BERT, ViT)
2. Tijdreeks-architecturen (Informer, PatchTST, Crossformer)
3. Event sequences & heterogene data (THP, FT-Transformer, SAINT)
4. Fraudedetectie (sequentiële patronen)
5. Synthetische data & benchmarking (TimeGAN, SynTSBench)

Zie `docs/literatuur/tijdlijn.md` voor de volledige evolutie-tijdlijn.
