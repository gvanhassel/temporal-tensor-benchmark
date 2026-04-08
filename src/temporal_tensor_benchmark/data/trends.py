"""Trend-injectie voor mock-data: 5 complexiteitsniveaus.

Level 0: Geen trend (random baseline)
Level 1: Enkele numerieke trend (bijv. lineaire stijging in feature X)
Level 2: Enkel event-patroon (bijv. herhaald event Y)
Level 3: Combinatie numeriek + event
Level 4: Conditioneel patroon (als A én B dan fraude)
Level 5: Temporeel conditioneel (A gevolgd door B binnen N tijdstappen)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

import numpy as np

if TYPE_CHECKING:
    from temporal_tensor_benchmark.data.generator import Dataset


@dataclass
class TrendConfig:
    """Configuratie voor trend-injectie."""

    level: int  # 0-5
    params: dict[str, Any] = field(default_factory=dict)


def inject_trends(dataset: "Dataset", trend_config: TrendConfig) -> None:
    """Injecteer trends in de fraude-subjecten van een dataset (in-place).

    Parameters
    ----------
    dataset : Dataset
        De dataset waarin trends worden geïnjecteerd.
    trend_config : TrendConfig
        Configuratie met level en parameters.
    """
    injectors = {
        0: _inject_level_0,
        1: _inject_level_1_numeric_trend,
        2: _inject_level_2_event_pattern,
        3: _inject_level_3_combined,
        4: _inject_level_4_conditional,
        5: _inject_level_5_temporal_conditional,
    }

    if trend_config.level not in injectors:
        raise ValueError(
            f"Ongeldig trend-level: {trend_config.level}. Kies 0-5."
        )

    injectors[trend_config.level](dataset, trend_config.params)
    dataset.metadata["trend_level"] = trend_config.level
    dataset.metadata["trend_params"] = trend_config.params


def _fraud_mask(dataset: "Dataset") -> np.ndarray:
    """Retourneer boolean mask van fraude-subjecten."""
    return dataset.labels == 1


def _inject_level_0(dataset: "Dataset", params: dict[str, Any]) -> None:
    """Level 0: geen trend — data blijft random."""
    dataset.metadata["description"] = "Level 0: geen trend (random baseline)"


def _inject_level_1_numeric_trend(
    dataset: "Dataset", params: dict[str, Any]
) -> None:
    """Level 1: lineaire trend in één numerieke feature voor fraude-subjecten.

    Parameters (in params dict):
        feature_idx (int): Index van de feature. Default: 0.
        slope (float): Steilheid van de trend per tijdstap. Default: 0.1.
        noise_std (float): Ruis op de trend. Default: 0.05.
    """
    feature_idx = params.get("feature_idx", 0)
    slope = params.get("slope", 0.1)
    noise_std = params.get("noise_std", 0.05)

    mask = _fraud_mask(dataset)
    n_fraud = mask.sum()
    T = dataset.n_timesteps

    # Lineaire trend: slope * t + ruis
    rng = np.random.default_rng(params.get("seed", 123))
    trend = slope * np.arange(T) + rng.normal(0, noise_std, (n_fraud, T))

    dataset.numeric[mask, :, feature_idx] += trend

    dataset.metadata["description"] = (
        f"Level 1: lineaire trend (slope={slope}) in feature {feature_idx} "
        f"voor fraude-subjecten"
    )


def _inject_level_2_event_pattern(
    dataset: "Dataset", params: dict[str, Any]
) -> None:
    """Level 2: herhaald event-patroon voor fraude-subjecten.

    Parameters (in params dict):
        event_idx (int): Index van het event-type. Default: 0.
        min_occurrences (int): Minimaal aantal events dat wordt geïnjecteerd. Default: 5.
        window_size (int): Tijdsvenster waarin events worden geplaatst. Default: hele reeks.
    """
    event_idx = params.get("event_idx", 0)
    min_occurrences = params.get("min_occurrences", 5)

    mask = _fraud_mask(dataset)
    T = dataset.n_timesteps
    window_size = params.get("window_size", T)

    rng = np.random.default_rng(params.get("seed", 234))

    for i in np.where(mask)[0]:
        # Kies random tijdstappen binnen het venster
        event_times = rng.choice(
            min(window_size, T), size=min_occurrences, replace=False
        )
        dataset.events[i, event_times, event_idx] = 1.0

    dataset.metadata["description"] = (
        f"Level 2: herhaald event {event_idx} (min {min_occurrences}x) "
        f"in venster van {window_size} tijdstappen voor fraude-subjecten"
    )


def _inject_level_3_combined(
    dataset: "Dataset", params: dict[str, Any]
) -> None:
    """Level 3: combinatie van numerieke trend + event-patroon.

    Parameters (in params dict):
        numeric_params (dict): Parameters voor level 1. Default: standaard level 1.
        event_params (dict): Parameters voor level 2. Default: standaard level 2.
    """
    numeric_params = params.get("numeric_params", {})
    event_params = params.get("event_params", {})

    _inject_level_1_numeric_trend(dataset, numeric_params)
    _inject_level_2_event_pattern(dataset, event_params)

    dataset.metadata["description"] = (
        "Level 3: combinatie numerieke trend + event-patroon voor fraude-subjecten"
    )


def _inject_level_4_conditional(
    dataset: "Dataset", params: dict[str, Any]
) -> None:
    """Level 4: conditioneel patroon — fraude alleen als conditie A én B waar zijn.

    Parameters (in params dict):
        feature_a_idx (int): Numerieke feature A. Default: 0.
        feature_b_idx (int): Numerieke feature B. Default: 1.
        threshold_a (float): Drempel voor stijging in A. Default: 0.08.
        threshold_b (float): Drempel voor daling in B. Default: -0.06.
    """
    feature_a_idx = params.get("feature_a_idx", 0)
    feature_b_idx = params.get("feature_b_idx", 1)
    slope_a = params.get("slope_a", 0.08)
    slope_b = params.get("slope_b", -0.06)
    noise_std = params.get("noise_std", 0.05)

    mask = _fraud_mask(dataset)
    n_fraud = mask.sum()
    T = dataset.n_timesteps

    rng = np.random.default_rng(params.get("seed", 345))

    # Conditie A: stijgende trend in feature A
    trend_a = slope_a * np.arange(T) + rng.normal(0, noise_std, (n_fraud, T))
    dataset.numeric[mask, :, feature_a_idx] += trend_a

    # Conditie B: dalende trend in feature B
    trend_b = slope_b * np.arange(T) + rng.normal(0, noise_std, (n_fraud, T))
    dataset.numeric[mask, :, feature_b_idx] += trend_b

    dataset.metadata["description"] = (
        f"Level 4: conditioneel patroon — stijging feature {feature_a_idx} "
        f"(slope={slope_a}) EN daling feature {feature_b_idx} (slope={slope_b}) "
        f"voor fraude-subjecten"
    )


def _inject_level_5_temporal_conditional(
    dataset: "Dataset", params: dict[str, Any]
) -> None:
    """Level 5: temporeel conditioneel — event A gevolgd door event B binnen N stappen.

    Parameters (in params dict):
        event_a_idx (int): Index van event A. Default: 0.
        event_b_idx (int): Index van event B. Default: 1.
        max_gap (int): Maximaal aantal tijdstappen tussen A en B. Default: 3.
        n_sequences (int): Aantal A→B sequenties per subject. Default: 2.
        numeric_feature_idx (int): Extra numerieke trend feature. Default: 0.
        numeric_slope (float): Slope van extra trend. Default: 0.05.
    """
    event_a_idx = params.get("event_a_idx", 0)
    event_b_idx = params.get("event_b_idx", 1)
    max_gap = params.get("max_gap", 3)
    n_sequences = params.get("n_sequences", 2)
    numeric_feature_idx = params.get("numeric_feature_idx", 0)
    numeric_slope = params.get("numeric_slope", 0.05)
    noise_std = params.get("noise_std", 0.03)

    mask = _fraud_mask(dataset)
    T = dataset.n_timesteps

    rng = np.random.default_rng(params.get("seed", 456))

    for i in np.where(mask)[0]:
        for _ in range(n_sequences):
            # Kies tijdstap voor event A, met ruimte voor gap + event B
            t_a = rng.integers(0, max(1, T - max_gap - 1))
            gap = rng.integers(1, max_gap + 1)
            t_b = min(t_a + gap, T - 1)

            dataset.events[i, t_a, event_a_idx] = 1.0
            dataset.events[i, t_b, event_b_idx] = 1.0

    # Voeg ook een subtiele numerieke trend toe
    n_fraud = mask.sum()
    trend = numeric_slope * np.arange(T) + rng.normal(
        0, noise_std, (n_fraud, T)
    )
    dataset.numeric[mask, :, numeric_feature_idx] += trend

    dataset.metadata["description"] = (
        f"Level 5: temporeel conditioneel — event {event_a_idx} gevolgd door "
        f"event {event_b_idx} binnen {max_gap} stappen ({n_sequences}x per subject) "
        f"+ subtiele numerieke trend in feature {numeric_feature_idx}"
    )
