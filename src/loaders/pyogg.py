from pathlib import Path

import pyogg


def get_info(path: Path) -> tuple[float, float]:
    opus_file = pyogg.OpusFile(path)

    sample_rate = opus_file.frequency
    duration = opus_file.as_array().shape[0] / sample_rate

    return duration, sample_rate
