"""Data-module: mock-data generatie en trend-injectie."""

from temporal_tensor_benchmark.data.generator import (
    Dataset,
    DatasetConfig,
    generate_dataset,
    generate_random_tensor,
)
from temporal_tensor_benchmark.data.trends import TrendConfig, inject_trends

__all__ = [
    "Dataset",
    "DatasetConfig",
    "TrendConfig",
    "generate_dataset",
    "generate_random_tensor",
    "inject_trends",
]
