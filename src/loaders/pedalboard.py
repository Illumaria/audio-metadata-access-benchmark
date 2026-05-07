from pathlib import Path

import pedalboard


NAME: str = "pedalboard"
SUPPORTED_EXTENSIONS: frozenset[str] = frozenset({"opus"})


def get_info(path: Path) -> tuple[float, float]:
    with pedalboard.io.AudioFile(filename=str(path)) as f:
        return f.duration, f.samplerate
