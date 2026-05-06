# Audio Metadata Access Benchmark

## Candidate Libraries

- `mutagen`
- `PyAV`
- `PyOgg`
- `scipy`
- `sox`

## Tested Libraries

| Library | Version | Release Date | Tested | Comment |
| --- | --- | --- | --- | --- |
| [`aubio`](https://github.com/aubio/aubio) | `0.4.9` | `27/02/2019` | ❌ | Requires building, not maintained |
| [`audiofile`](https://github.com/audeering/audiofile/) | `1.6.0` | `15/01/2026` | ❌ | Requires `mediainfo` which is hard to install, uses `soundfile` under the hood |
| [`audioread`](https://github.com/beetbox/audioread) | `3.1.0` | `26/10/2025` | ✅ | - |
| [`ffprobe`](https://ffmpeg.org/ffprobe.html) | `-` | `-` | ✅ | - |
| [`librosa`](https://github.com/librosa/librosa) | `0.11.0` | `11/03/2025` | ✅ | - |
| [`miniaudio`](https://github.com/irmen/pyminiaudio) | `1.71` | `29/04/2026` | ❌ | [Doesn't support `opus` format](https://github.com/irmen/pyminiaudio/blob/598e6fc3c923ed44122db6be4c0a405f3487e79d/miniaudio.py#L212-L223) |
| [`pedalboard`](https://github.com/spotify/pedalboard) | `0.9.22` | `02/02/2026` | ✅ | - |
| [`pydub`](https://github.com/jiaaro/pydub) | `0.25.1` | `10/03/2021` | ✅ | - |
| [`soundfile`](https://github.com/bastibe/python-soundfile) | `0.13.1` | `25/01/2025` | ✅ | - |
| [`stempeg`](https://github.com/faroit/stempeg) | `0.2.4` | `28/05/2025` | ✅ | - |
| [`tinytag`](https://github.com/tinytag/tinytag) | `2.2.1` | `15/03/2026` | ✅ | - |
| [`torchcodec`](https://github.com/meta-pytorch/torchcodec) | `0.11.1` | `14/04/2026` | ✅ | - |
