from pathlib import Path

import soundfile


NAME: str = "soundfile"
SUPPORTED_EXTENSIONS: frozenset[str] = frozenset({"opus"})


def get_info(path: Path) -> tuple[float, float]:
    info = soundfile.info(file=path)
    return info.duration, info.samplerate
