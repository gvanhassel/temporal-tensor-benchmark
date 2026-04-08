"""Tests voor de mock-data generator."""

import numpy as np
import pytest

from temporal_tensor_benchmark.data.generator import (
    Dataset,
    DatasetConfig,
    generate_dataset,
    generate_random_tensor,
)
from temporal_tensor_benchmark.data.trends import TrendConfig


class TestGenerateRandomTensor:
    """Tests voor generate_random_tensor()."""

    def test_output_shapes(self):
        ds = generate_random_tensor(
            n_subjects=100, n_timesteps=12, n_numeric_features=3,
            n_event_types=2, n_static_features=4,
        )
        assert ds.numeric.shape == (100, 12, 3)
        assert ds.events.shape == (100, 12, 2)
        assert ds.static.shape == (100, 4)
        assert ds.labels.shape == (100,)

    def test_label_distributie_50_50(self):
        ds = generate_random_tensor(n_subjects=1000, fraud_ratio=0.5)
        assert ds.labels.sum() == 500

    def test_label_distributie_custom(self):
        ds = generate_random_tensor(n_subjects=100, fraud_ratio=0.3)
        assert ds.labels.sum() == 30

    def test_events_zijn_binair(self):
        ds = generate_random_tensor(n_subjects=50, n_timesteps=10, n_event_types=3)
        unieke_waarden = np.unique(ds.events)
        assert set(unieke_waarden).issubset({0.0, 1.0})

    def test_reproduceerbaarheid_met_seed(self):
        ds1 = generate_random_tensor(n_subjects=50, seed=42)
        ds2 = generate_random_tensor(n_subjects=50, seed=42)
        np.testing.assert_array_equal(ds1.numeric, ds2.numeric)
        np.testing.assert_array_equal(ds1.events, ds2.events)
        np.testing.assert_array_equal(ds1.static, ds2.static)

    def test_andere_seed_geeft_andere_data(self):
        ds1 = generate_random_tensor(n_subjects=50, seed=42)
        ds2 = generate_random_tensor(n_subjects=50, seed=99)
        assert not np.array_equal(ds1.numeric, ds2.numeric)

    def test_tensor_3d_property(self):
        ds = generate_random_tensor(
            n_subjects=10, n_timesteps=5,
            n_numeric_features=3, n_event_types=2,
        )
        combined = ds.tensor_3d
        assert combined.shape == (10, 5, 5)  # 3 + 2

    def test_n_subjects_property(self):
        ds = generate_random_tensor(n_subjects=77)
        assert ds.n_subjects == 77

    def test_n_timesteps_property(self):
        ds = generate_random_tensor(n_timesteps=36)
        assert ds.n_timesteps == 36


class TestGenerateDataset:
    """Tests voor generate_dataset()."""

    def test_zonder_trend(self):
        config = DatasetConfig(n_subjects=50, n_timesteps=10)
        ds = generate_dataset(config)
        assert ds.numeric.shape == (50, 10, 5)
        assert ds.config is config

    def test_met_trend_level_1(self):
        config = DatasetConfig(
            n_subjects=100,
            n_timesteps=24,
            trend=TrendConfig(level=1, params={"slope": 0.2}),
        )
        ds = generate_dataset(config)
        assert ds.metadata["trend_level"] == 1

    def test_met_trend_level_0(self):
        config = DatasetConfig(
            n_subjects=50,
            trend=TrendConfig(level=0),
        )
        ds = generate_dataset(config)
        assert ds.metadata["trend_level"] == 0

    def test_config_wordt_bewaard(self):
        config = DatasetConfig(n_subjects=30, seed=99)
        ds = generate_dataset(config)
        assert ds.config.seed == 99
        assert ds.config.n_subjects == 30
