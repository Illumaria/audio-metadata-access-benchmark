from pathlib import Path

import tinytag


def get_info(path: Path) -> tuple[float, float]:
    info = tinytag.TinyTag.get(filename=path)
    duration = info.duration or 0.0
    sample_rate = info.samplerate or 0.0
    return duration, sample_rate
