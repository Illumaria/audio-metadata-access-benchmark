from pathlib import Path

import soundfile


def get_info(path: Path) -> tuple[float, float]:
    info = soundfile.info(file=path)
    return info.duration, info.samplerate
