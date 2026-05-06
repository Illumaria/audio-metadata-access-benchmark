from pathlib import Path

from scipy.io import wavfile


def get_info(path: Path) -> tuple[float, float]:
    sample_rate, data = wavfile.read(filename=path, mmap=False)
    duration = data.shape[0] / sample_rate
    return duration, sample_rate


def get_info_mmap(path: Path) -> tuple[float, float]:
    sample_rate, data = wavfile.read(filename=path, mmap=True)
    duration = data.shape[0] / sample_rate
    return duration, sample_rate
