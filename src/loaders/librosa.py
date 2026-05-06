from pathlib import Path

import librosa


def get_info(path: Path) -> tuple[float, float]:
    duration = librosa.get_duration(path=path)
    sample_rate = librosa.get_samplerate(path=str(path))
    return duration, sample_rate
