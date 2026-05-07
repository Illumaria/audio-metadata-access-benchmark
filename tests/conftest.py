import tomllib
from dataclasses import dataclass
from pathlib import Path

import pytest

from src.constants import PROJECT_DIR
from src.loaders import LOADERS, LoaderSpec


FIXTURES_DIR: Path = PROJECT_DIR / "tests" / "fixtures"
AUDIO_DIR: Path = FIXTURES_DIR / "audio"
MANIFEST_PATH: Path = FIXTURES_DIR / "manifest.toml"

# Absolute tolerance for the duration assertion, per file extension.
# Lossy/frame-based formats round to frame boundaries, so libs disagree by
# tens of milliseconds. Lossless formats are sample-exact.
DURATION_ABS_TOL: dict[str, float] = {
    "opus": 0.05,
    "mp3": 0.05,
    "aac": 0.05,
    "m4a": 0.05,
    "ogg": 0.05,
    "wav": 1e-6,
    "flac": 1e-6,
    "aiff": 1e-6,
}


@dataclass(frozen=True)
class AudioFixture:
    path: Path
    duration: float
    sample_rate: int
    ext: str


def _load_manifest() -> list[AudioFixture]:
    if not MANIFEST_PATH.exists():
        return []

    with MANIFEST_PATH.open("rb") as f:
        data = tomllib.load(f)

    fixtures: list[AudioFixture] = []
    for entry in data.get("fixtures", []):
        path = AUDIO_DIR / entry["file"]
        fixtures.append(
            AudioFixture(
                path=path,
                duration=float(entry["duration"]),
                sample_rate=int(entry["sample_rate"]),
                ext=path.suffix.lstrip("."),
            )
        )
    return fixtures


@pytest.fixture(
    params=list(LOADERS.values()),
    ids=lambda spec: spec.name,
)
def loader_spec(request: pytest.FixtureRequest) -> LoaderSpec:
    return request.param


@pytest.fixture(
    params=_load_manifest(),
    ids=lambda fx: fx.path.name,
)
def audio_fixture(request: pytest.FixtureRequest) -> AudioFixture:
    fx: AudioFixture = request.param
    if not fx.path.exists():
        pytest.skip(f"fixture file missing: {fx.path}")
    return fx
