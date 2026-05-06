"""
Some of the code taken from:
https://github.com/aubio/aubio/blob/master/python/demos/demo_reading_speed.py
"""

from __future__ import annotations

from pathlib import Path

import sox
from mutagen.oggopus import OggOpus
from scipy.io import wavfile


def load_scipy(path: Path):
    sample_rate, sig = wavfile.read(filename=path)
    sig = sig.astype("float32") / 32767
    return sig


def load_scipy_mmap(path: Path):
    sample_rate, sig = wavfile.read(filename=path, mmap=True)
    sig = sig.astype("float32") / 32767
    return sig


# def info_aubio(path: Path):
#     with aubio.source(path) as f:
#         return f.duration, f.samplerate
#     return info


def info_mutagen(path: Path):
    opus = OggOpus(path)
    duration = opus.info.length
    # Opus always decodes at 48 kHz regardless of input sample rate.
    sample_rate = int(getattr(opus.info, "sample_rate", 48000) or 48000)
    return duration, sample_rate


def info_sox(path: Path):
    return (
        sox.file_info.duration(input_filepath=path),
        int(sox.file_info.sample_rate(input_filepath=path)),
    )
