from pathlib import Path
from typing import Any

import pandas as pd
import seaborn as sns
from loguru import logger

from src.constants import RESULTS_DIR


class DataFrameWriter:
    def __init__(self, columns: list[str]) -> None:
        self.df = pd.DataFrame(columns=columns)

    def append(self, row: dict[str, Any]) -> None:
        if set(self.df.columns) == set(row):
            self.df = pd.concat([self.df, pd.DataFrame([row])], ignore_index=True)


def list_files(src_dir: str, src_ext: str) -> list[Path]:
    file_iterator = Path(src_dir).rglob(pattern=f"**/*.{src_ext}")
    return list(file_iterator)


def plot_results(
    df: pd.DataFrame, path: Path = RESULTS_DIR / "benchmark_metadata.png"
) -> None:
    sns.set_style("whitegrid")

    g = sns.catplot(
        x="time",
        y="lib",
        kind="bar",
        hue="lib",
        data=df,
        aspect=1,
        legend=False,
    )
    g.set(xscale="log")
    g.despine(left=True)

    g.savefig(fname=path)
    logger.info(f"Plot saved to '{path}'")
