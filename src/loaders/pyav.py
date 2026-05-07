from pathlib import Path

import av


NAME: str = "pyav"
SUPPORTED_EXTENSIONS: frozenset[str] = frozenset({"opus"})


def get_info(path: Path) -> tuple[float, float]:
    container = av.open(file=path)
    stream = container.streams.audio[0]

    sample_rate = stream.codec_context.sample_rate or 0.0

    duration_samples = stream.duration or 0.0
    time_base = stream.time_base or 0.0
    duration = duration_samples * float(time_base)

    return duration, sample_rate
