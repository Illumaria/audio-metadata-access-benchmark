from pathlib import Path


PROJECT_DIR: Path = Path(__name__).resolve().parent
AUDIO_DIR: Path = PROJECT_DIR / "data" / "audio"
RESULTS_DIR: Path = PROJECT_DIR / "data" / "results"

DEFAULT_AUDIO_EXTENSION: str = "opus"

LIB_NAMES: list[str] = [
    "audioread",
    "ffprobe",
    "librosa",
    "mutagen",
    "pedalboard",
    "pyav",
    "pydub",
    "soundfile",
    "sox",
    "stempeg",
    "tinytag",
    "torchcodec",
]

DATAFRAME_COLUMNS: list[str] = [
    "ext",
    "lib",
    "duration",
    "time",
]
