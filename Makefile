build:
	docker-buildx build --platform linux/amd64 --load -t audio-benchmark:latest .

generate-audio:
	docker run --platform linux/amd64 --rm --volume ./audio:/app/audio audio-benchmark:latest /bin/bash generate_audio.sh

run-it:
	docker run --platform linux/amd64 --rm --volume ./audio:/app/audio -it audio-benchmark:latest /bin/bash

run:
	docker run --platform linux/amd64 --rm --volume ./audio:/app/audio -it audio-benchmark:latest python benchmark.py --ext opus
