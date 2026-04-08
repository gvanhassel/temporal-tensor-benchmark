"""Tests voor trend-injectie functies."""

import numpy as np
import pytest

from temporal_tensor_benchmark.data.generator import generate_random_tensor
from temporal_tensor_benchmark.data.trends import TrendConfig, inject_trends


class TestLevel0GeenTrend:
    """Level 0: geen trend — data blijft random."""

    def test_data_ongewijzigd(self):
        ds = generate_random_tensor(n_subjects=100, seed=42)
        numeric_voor = ds.numeric.copy()
        inject_trends(ds, TrendConfig(level=0))
        np.testing.assert_array_equal(ds.numeric, numeric_voor)

    def test_metadata_bevat_level(self):
        ds = generate_random_tensor(n_subjects=50)
        inject_trends(ds, TrendConfig(level=0))
        assert ds.metadata["trend_level"] == 0


class TestLevel1NumeriekeTrend:
    """Level 1: lineaire trend in één numerieke feature."""

    def test_fraude_subjecten_hebben_hogere_waarden_aan_einde(self):
        ds = generate_random_tensor(
            n_subjects=200, n_timesteps=24, n_numeric_features=3, seed=42
        )
        inject_trends(ds, TrendConfig(level=1, params={"feature_idx": 0, "slope": 0.2}))

        fraud_mask = ds.labels == 1
        # Gemiddelde van feature 0 op laatste tijdstap vs. eerste
        fraud_begin = ds.numeric[fraud_mask, :3, 0].mean()
        fraud_einde = ds.numeric[fraud_mask, -3:, 0].mean()
        assert fraud_einde > fraud_begin

    def test_niet_fraude_subjecten_onveranderd(self):
        ds1 = generate_random_tensor(n_subjects=100, seed=42)
        ds2 = generate_random_tensor(n_subjects=100, seed=42)
        inject_trends(ds1, TrendConfig(level=1, params={"feature_idx": 0}))

        not_fraud = ds1.labels == 0
        np.testing.assert_array_equal(
            ds1.numeric[not_fraud], ds2.numeric[not_fraud]
        )

    def test_andere_features_onveranderd(self):
        ds1 = generate_random_tensor(
            n_subjects=100, n_numeric_features=3, seed=42
        )
        ds2 = generate_random_tensor(
            n_subjects=100, n_numeric_features=3, seed=42
        )
        inject_trends(ds1, TrendConfig(level=1, params={"feature_idx": 0}))

        fraud = ds1.labels == 1
        # Feature 1 en 2 moeten ongewijzigd zijn
        np.testing.assert_array_equal(
            ds1.numeric[fraud, :, 1:], ds2.numeric[fraud, :, 1:]
        )

    def test_metadata_beschrijving(self):
        ds = generate_random_tensor(n_subjects=50)
        inject_trends(ds, TrendConfig(level=1))
        assert ds.metadata["trend_level"] == 1
        assert "Level 1" in ds.metadata["description"]


class TestLevel2EventPatroon:
    """Level 2: herhaald event-patroon voor fraude-subjecten."""

    def test_fraude_heeft_meer_events(self):
        ds = generate_random_tensor(
            n_subjects=200, n_timesteps=24, n_event_types=3, seed=42
        )
        inject_trends(
            ds,
            TrendConfig(level=2, params={"event_idx": 0, "min_occurrences": 8}),
        )

        fraud = ds.labels == 1
        not_fraud = ds.labels == 0

        gemiddeld_fraud = ds.events[fraud, :, 0].sum(axis=1).mean()
        gemiddeld_niet_fraud = ds.events[not_fraud, :, 0].sum(axis=1).mean()
        assert gemiddeld_fraud > gemiddeld_niet_fraud

    def test_minimaal_aantal_events_geplaatst(self):
        ds = generate_random_tensor(
            n_subjects=50, n_timesteps=20, n_event_types=2, seed=42
        )
        inject_trends(
            ds,
            TrendConfig(level=2, params={"event_idx": 0, "min_occurrences": 6}),
        )
        fraud = ds.labels == 1
        for i in np.where(fraud)[0]:
            # Minstens 6 events (kan meer zijn door bestaande random events)
            assert ds.events[i, :, 0].sum() >= 6

    def test_andere_event_types_onveranderd(self):
        ds1 = generate_random_tensor(
            n_subjects=100, n_event_types=3, seed=42
        )
        ds2 = generate_random_tensor(
            n_subjects=100, n_event_types=3, seed=42
        )
        inject_trends(ds1, TrendConfig(level=2, params={"event_idx": 0}))

        # Event type 1 en 2 moeten ongewijzigd zijn
        np.testing.assert_array_equal(ds1.events[:, :, 1:], ds2.events[:, :, 1:])


class TestLevel3Combinatie:
    """Level 3: combinatie numeriek + event."""

    def test_beide_patronen_aanwezig(self):
        ds = generate_random_tensor(
            n_subjects=200, n_timesteps=24,
            n_numeric_features=3, n_event_types=3, seed=42,
        )
        inject_trends(
            ds,
            TrendConfig(
                level=3,
                params={
                    "numeric_params": {"feature_idx": 0, "slope": 0.15},
                    "event_params": {"event_idx": 1, "min_occurrences": 6},
                },
            ),
        )

        fraud = ds.labels == 1
        not_fraud = ds.labels == 0

        # Numerieke trend aanwezig
        fraud_einde = ds.numeric[fraud, -3:, 0].mean()
        fraud_begin = ds.numeric[fraud, :3, 0].mean()
        assert fraud_einde > fraud_begin

        # Event-patroon aanwezig
        events_fraud = ds.events[fraud, :, 1].sum(axis=1).mean()
        events_niet_fraud = ds.events[not_fraud, :, 1].sum(axis=1).mean()
        assert events_fraud > events_niet_fraud


class TestLevel4Conditioneel:
    """Level 4: conditioneel — stijging A én daling B."""

    def test_feature_a_stijgt_feature_b_daalt(self):
        ds = generate_random_tensor(
            n_subjects=200, n_timesteps=24, n_numeric_features=3, seed=42
        )
        inject_trends(
            ds,
            TrendConfig(
                level=4,
                params={
                    "feature_a_idx": 0,
                    "feature_b_idx": 1,
                    "slope_a": 0.15,
                    "slope_b": -0.12,
                },
            ),
        )

        fraud = ds.labels == 1
        # Feature A stijgt
        a_begin = ds.numeric[fraud, :3, 0].mean()
        a_einde = ds.numeric[fraud, -3:, 0].mean()
        assert a_einde > a_begin

        # Feature B daalt
        b_begin = ds.numeric[fraud, :3, 1].mean()
        b_einde = ds.numeric[fraud, -3:, 1].mean()
        assert b_einde < b_begin


class TestLevel5TemporalConditional:
    """Level 5: temporeel conditioneel — event A gevolgd door event B."""

    def test_event_sequenties_aanwezig_bij_fraude(self):
        ds = generate_random_tensor(
            n_subjects=200, n_timesteps=24, n_event_types=3, seed=42
        )
        inject_trends(
            ds,
            TrendConfig(
                level=5,
                params={
                    "event_a_idx": 0,
                    "event_b_idx": 1,
                    "max_gap": 3,
                    "n_sequences": 3,
                },
            ),
        )

        fraud = ds.labels == 1
        # Fraude-subjecten moeten meer event A en B hebben
        events_a_fraud = ds.events[fraud, :, 0].sum(axis=1).mean()
        events_a_niet_fraud = ds.events[~fraud, :, 0].sum(axis=1).mean()
        assert events_a_fraud > events_a_niet_fraud

    def test_numerieke_trend_ook_aanwezig(self):
        ds = generate_random_tensor(
            n_subjects=200, n_timesteps=24, n_numeric_features=3, seed=42
        )
        inject_trends(
            ds,
            TrendConfig(
                level=5,
                params={"numeric_feature_idx": 2, "numeric_slope": 0.1},
            ),
        )

        fraud = ds.labels == 1
        begin = ds.numeric[fraud, :3, 2].mean()
        einde = ds.numeric[fraud, -3:, 2].mean()
        assert einde > begin

    def test_metadata_beschrijving(self):
        ds = generate_random_tensor(n_subjects=50)
        inject_trends(ds, TrendConfig(level=5))
        assert ds.metadata["trend_level"] == 5
        assert "Level 5" in ds.metadata["description"]


class TestOngeldigLevel:
    """Test voor ongeldig trend-level."""

    def test_level_buiten_bereik_geeft_fout(self):
        ds = generate_random_tensor(n_subjects=10)
        with pytest.raises(ValueError, match="Ongeldig trend-level"):
            inject_trends(ds, TrendConfig(level=99))
