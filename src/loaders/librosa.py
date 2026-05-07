from pathlib import Path

import librosa


NAME: str = "librosa"
SUPPORTED_EXTENSIONS: frozenset[str] = frozenset({"opus"})


def get_info(path: Path) -> tuple[float, float]:
    duration = librosa.get_duration(path=path)
    sample_rate = librosa.get_samplerate(path=str(path))
    return duration, sample_rate
