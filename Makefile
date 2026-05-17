.DEFAULT_GOAL := all

setup: scripts/downloader.py
	python3 scripts/downloader.py --all

all: scripts/jetple.py
	python3 scripts/jetple.py --all

web: scripts/jetple.py
	python3 scripts/jetple.py --all --disable-nerd-fonts --ext woff2

clean:
	rm -rf out/ scripts/__pycache__/ tmp/
