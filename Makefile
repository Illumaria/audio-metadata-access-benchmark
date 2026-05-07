docker-build:
	docker-buildx build --platform linux/amd64 --load -t audio-benchmark:latest .

docker-generate-audio:
	docker run --platform linux/amd64 --rm --volume ./audio:/app/audio audio-benchmark:latest /bin/bash generate_audio.sh

docker-run-it:
	docker run --platform linux/amd64 --rm --volume ./audio:/app/audio -it audio-benchmark:latest /bin/bash

docker-run:
	docker run --platform linux/amd64 --rm --volume ./audio:/app/audio -it audio-benchmark:latest python benchmark.py --ext opus

run:
	uv run benchmark.py run --ext opus

plot:
	uv run benchmark.py plot

test:
	uv run pytest -v
