# Audio Metadata Access Benchmark

## Accepted Libraries
- [`audioread`](https://github.com/beetbox/audioread)
- [`ffprobe`](https://ffmpeg.org/ffprobe.html)
- [`librosa`](https://github.com/librosa/librosa)
- [`pedalboard`](https://github.com/spotify/pedalboard)
- [`pydub`](https://github.com/jiaaro/pydub)
- [`soundfile`](https://github.com/bastibe/python-soundfile)
- [`stempeg`](https://github.com/faroit/stempeg)
- [`tinytag`](https://github.com/tinytag/tinytag)
- [`torchcodec`](https://github.com/meta-pytorch/torchcodec)

## Candidate Libraries
- `aubio`
- `mutagen`
- `PyAV`
- `PyOgg`
- `scipy`
- `sox`

## Rejected Libraries
- [`audiofile`](https://github.com/audeering/audiofile/): requires `mediainfo` which is too much hussle to install
- [`miniaudio`](https://github.com/irmen/pyminiaudio): doesn't support `opus` format
