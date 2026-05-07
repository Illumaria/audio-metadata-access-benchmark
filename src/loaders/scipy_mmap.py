from pathlib import Path

from scipy.io import wavfile


NAME: str = "scipy_mmap"
SUPPORTED_EXTENSIONS: frozenset[str] = frozenset({"wav"})


def get_info(path: Path) -> tuple[float, float]:
    sample_rate, data = wavfile.read(filename=path, mmap=True)
    duration = data.shape[0] / sample_rate
    return duration, sample_rate
