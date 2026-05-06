import os
import time

import pandas as pd
from cyclopts import App
from loguru import logger

from src import loaders
from src.constants import (
    AUDIO_DIR,
    DATAFRAME_COLUMNS,
    DEFAULT_AUDIO_EXTENSION,
    LIB_NAMES,
    RESULTS_DIR,
)
from src.utils import DataFrameWriter, list_files, plot_results

app = App()


class AudioFolder:
    def __init__(
        self,
        root: str,
        extension: str = "wav",
        lib: str = "librosa",
    ) -> None:
        self.root = os.path.expanduser(root)
        self.data = []
        self.audio_files = list_files(src_dir=self.root, src_ext=extension)
        self.loader_function = getattr(loaders, lib)

    def __getitem__(self, index: int) -> tuple[float, float]:
        return self.loader_function(self.audio_files[index])

    def __len__(self) -> int:
        return len(self.audio_files)


@app.command(name="run")
def run(
    ext: str = DEFAULT_AUDIO_EXTENSION,
) -> None:
    """Execute benchmark for a run, printing logs to stdout"""
    store = DataFrameWriter(columns=DATAFRAME_COLUMNS)

    for lib in LIB_NAMES:
        logger.info("Testing: %s" % lib)

        for root, dirs, _ in sorted(os.walk(AUDIO_DIR)):
            for audio_dir in dirs:
                duration = int(audio_dir)
                dataset = AudioFolder(
                    os.path.join(root, audio_dir),
                    lib="info_" + lib,
                    extension=ext,
                )

                start = time.monotonic()

                for _ in range(3):
                    for fp in dataset.audio_files:
                        _ = dataset.loader_function(fp)

                end = time.monotonic()
                store.append(
                    row=dict(
                        ext=ext,
                        lib=lib,
                        duration=duration,
                        time=float(end - start) / (len(dataset) * 3),
                    ),
                )

    store.df.to_csv(RESULTS_DIR / f"benchmark_metadata_{ext}.csv")


@app.command(name="plot")
def plot(ext: str = DEFAULT_AUDIO_EXTENSION) -> None:
    df = pd.read_csv(RESULTS_DIR / f"benchmark_metadata_{ext}.csv")
    plot_results(df=df)


if __name__ == "__main__":
    app()
