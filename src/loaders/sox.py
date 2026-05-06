from pathlib import Path

import sox


def get_info(path: Path) -> tuple[float, float]:
    duration = sox.file_info.duration(input_filepath=path) or 0.0
    sample_rate = sox.file_info.sample_rate(input_filepath=path)
    return duration, sample_rate
