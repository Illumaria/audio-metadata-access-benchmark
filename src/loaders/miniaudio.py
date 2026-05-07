from pathlib import Path

import miniaudio


NAME: str = "miniaudio"
SUPPORTED_EXTENSIONS: frozenset[str] = frozenset({})


def get_info(path: Path) -> tuple[float, float]:
    info = miniaudio.get_file_info(filename=str(path))
    return info.duration, info.sample_rate
