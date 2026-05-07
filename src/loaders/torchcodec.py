from pathlib import Path

import torchcodec


NAME: str = "torchcodec"
SUPPORTED_EXTENSIONS: frozenset[str] = frozenset({"opus"})


def get_info(path: Path) -> tuple[float, float]:
    info = torchcodec.decoders.AudioDecoder(source=path)
    duration = info.metadata.duration_seconds or 0.0
    sample_rate = info.metadata.sample_rate or 0.0
    return duration, sample_rate
