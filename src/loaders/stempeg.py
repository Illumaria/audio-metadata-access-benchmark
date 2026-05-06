from pathlib import Path

import stempeg


def get_info(path: Path) -> tuple[float, float]:
    info = stempeg.Info(filename=path)
    duration = info.duration(0)
    sample_rate = info.sample_rate(0)
    return duration, sample_rate
