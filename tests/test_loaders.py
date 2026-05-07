import pytest

from src.loaders import LoaderSpec
from tests.conftest import DURATION_ABS_TOL, AudioFixture


def test_duration_and_sample_rate(
    loader_spec: LoaderSpec,
    audio_fixture: AudioFixture,
) -> None:
    if audio_fixture.ext not in loader_spec.extensions:
        pytest.skip(f"{loader_spec.name} does not support .{audio_fixture.ext}")

    duration, sample_rate = loader_spec.get_info(audio_fixture.path)

    assert sample_rate == audio_fixture.sample_rate
    assert duration == pytest.approx(
        audio_fixture.duration,
        abs=DURATION_ABS_TOL[audio_fixture.ext],
    )
