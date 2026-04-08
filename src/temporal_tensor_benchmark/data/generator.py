"""Mock-data generator voor 3D-tensordata (subject x tijd x features).

Genereert datasets met de structuur:
    - numeric: np.ndarray [N_subjects, T_timesteps, F_numeric]
    - events:  np.ndarray [N_subjects, T_timesteps, F_events]
    - static:  np.ndarray [N_subjects, F_static]
    - labels:  np.ndarray [N_subjects]  (0 of 1)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import numpy as np

from temporal_tensor_benchmark.data.trends import TrendConfig, inject_trends


@dataclass
class DatasetConfig:
    """Configuratie voor het genereren van een dataset."""

    n_subjects: int = 1000
    n_timesteps: int = 24
    n_numeric_features: int = 5
    n_event_types: int = 4
    n_static_features: int = 3
    fraud_ratio: float = 0.5
    seed: int | None = 42
    trend: TrendConfig | None = None


@dataclass
class Dataset:
    """Container voor een gegenereerde dataset."""

    numeric: np.ndarray  # (N, T, F_num)
    events: np.ndarray  # (N, T, F_evt)
    static: np.ndarray  # (N, F_static)
    labels: np.ndarray  # (N,)
    config: DatasetConfig
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def n_subjects(self) -> int:
        return self.numeric.shape[0]

    @property
    def n_timesteps(self) -> int:
        return self.numeric.shape[1]

    @property
    def tensor_3d(self) -> np.ndarray:
        """Gecombineerde 3D-tensor: numeric + events → (N, T, F_num + F_evt)."""
        return np.concatenate([self.numeric, self.events], axis=2)


def generate_random_tensor(
    n_subjects: int = 1000,
    n_timesteps: int = 24,
    n_numeric_features: int = 5,
    n_event_types: int = 4,
    n_static_features: int = 3,
    fraud_ratio: float = 0.5,
    seed: int | None = 42,
) -> Dataset:
    """Genereer volledig willekeurige 3D-tensordata zonder trends.

    Parameters
    ----------
    n_subjects : int
        Aantal subjecten (bijv. burgers/bedrijven).
    n_timesteps : int
        Aantal tijdstappen per subject.
    n_numeric_features : int
        Aantal numerieke features per tijdstap.
    n_event_types : int
        Aantal event-typen per tijdstap (binair).
    n_static_features : int
        Aantal statische (niet-tijdsgebonden) features.
    fraud_ratio : float
        Fractie van subjecten met label 1 (fraude).
    seed : int | None
        Random seed voor reproduceerbaarheid.

    Returns
    -------
    Dataset
        Gegenereerde dataset met random data en ~50/50 labels.
    """
    rng = np.random.default_rng(seed)

    numeric = rng.standard_normal((n_subjects, n_timesteps, n_numeric_features))
    events = rng.binomial(1, 0.15, (n_subjects, n_timesteps, n_event_types)).astype(
        np.float32
    )
    static = rng.standard_normal((n_subjects, n_static_features))

    n_fraud = int(n_subjects * fraud_ratio)
    labels = np.zeros(n_subjects, dtype=np.int64)
    labels[:n_fraud] = 1
    rng.shuffle(labels)

    config = DatasetConfig(
        n_subjects=n_subjects,
        n_timesteps=n_timesteps,
        n_numeric_features=n_numeric_features,
        n_event_types=n_event_types,
        n_static_features=n_static_features,
        fraud_ratio=fraud_ratio,
        seed=seed,
    )

    return Dataset(
        numeric=numeric,
        events=events,
        static=static,
        labels=labels,
        config=config,
        metadata={"trend_level": 0, "description": "volledig random, geen trends"},
    )


def generate_dataset(config: DatasetConfig) -> Dataset:
    """Genereer een dataset op basis van een DatasetConfig, inclusief optionele trends.

    Parameters
    ----------
    config : DatasetConfig
        Volledige configuratie inclusief optionele trend.

    Returns
    -------
    Dataset
        Gegenereerde dataset, met trends geïnjecteerd als config.trend is ingesteld.
    """
    dataset = generate_random_tensor(
        n_subjects=config.n_subjects,
        n_timesteps=config.n_timesteps,
        n_numeric_features=config.n_numeric_features,
        n_event_types=config.n_event_types,
        n_static_features=config.n_static_features,
        fraud_ratio=config.fraud_ratio,
        seed=config.seed,
    )
    dataset.config = config

    if config.trend is not None:
        inject_trends(dataset, config.trend)

    return dataset
