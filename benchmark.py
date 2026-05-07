import os
import time

import pandas as pd
from cyclopts import App
from loguru import logger

from src.constants import (
    AUDIO_DIR,
    DATAFRAME_COLUMNS,
    DEFAULT_AUDIO_EXTENSION,
    RESULTS_DIR,
)
from src.loaders import LOADERS, LoaderSpec
from src.utils import DataFrameWriter, list_files, plot_results

app = App()


class AudioFolder:
    def __init__(
        self,
        root: str,
        loader: LoaderSpec,
        extension: str = "wav",
    ) -> None:
        self.root = os.path.expanduser(root)
        self.audio_files = list_files(src_dir=self.root, src_ext=extension)
        self.loader = loader

    def __getitem__(self, index: int) -> tuple[float, float]:
        return self.loader.get_info(self.audio_files[index])

    def __len__(self) -> int:
        return len(self.audio_files)


@app.command(name="run")
def run(
    ext: str = DEFAULT_AUDIO_EXTENSION,
) -> None:
    """Execute benchmark for a run, printing logs to stdout"""
    store = DataFrameWriter(columns=DATAFRAME_COLUMNS)

    for loader in LOADERS.values():
        if ext not in loader.extensions:
            logger.info("Skipping %s (does not support .%s)" % (loader.name, ext))
            continue

        logger.info("Testing: %s" % loader.name)

        for root, dirs, _ in sorted(os.walk(AUDIO_DIR)):
            for audio_dir in dirs:
                duration = int(audio_dir)
                dataset = AudioFolder(
                    os.path.join(root, audio_dir),
                    loader=loader,
                    extension=ext,
                )

                start = time.monotonic()

                for _ in range(3):
                    for fp in dataset.audio_files:
                        _ = dataset.loader.get_info(fp)

                end = time.monotonic()
                store.append(
                    row=dict(
                        ext=ext,
                        lib=loader.name,
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
