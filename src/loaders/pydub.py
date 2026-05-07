from pathlib import Path

import pydub


NAME: str = "pydub"
SUPPORTED_EXTENSIONS: frozenset[str] = frozenset({"opus"})


def get_info(path: Path) -> tuple[float, float]:
    info = pydub.AudioSegment.from_file(file=path)
    return info.duration_seconds, info.frame_rate
