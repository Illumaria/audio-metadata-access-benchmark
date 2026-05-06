from pathlib import Path

import audioread


def get_info(path: Path) -> tuple[float, float]:
    duration, sample_rate = 0.0, 0.0

    with audioread.audio_open(path=path) as f:
        duration, sample_rate = f.duration, f.samplerate

    return duration, sample_rate
