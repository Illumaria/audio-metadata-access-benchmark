import json
import subprocess
from pathlib import Path


def get_info(path: Path) -> tuple[float, float]:
    """Return duration in seconds and sample rate. Raises on failure."""
    cmd = [
        "ffprobe",
        "-v",
        "quiet",
        "-print_format",
        "json",
        "-show_streams",
        str(path),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
    info = json.loads(result.stdout)

    for stream in info.get("streams", []):
        if stream.get("codec_type") == "audio":
            sample_rate = int(stream.get("sample_rate", 48000))
            dur_str = stream.get("duration")
            if dur_str:
                duration = float(dur_str)
            else:
                # fallback: use container-level duration
                duration = float(info.get("format", {}).get("duration", 0))
            return duration, sample_rate

    raise RuntimeError(f"No audio stream found in {path}")
