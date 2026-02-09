.PHONY: dep-install uv-install rmzi rm-lock rm-outputs rm-pycache rm-venv reset start help make-help

DATE := $(shell date '+%Y/%m/%d')
TIME := $(shell date '+%H-%M-%S')

MAIN_OUTPUT_DIR = src/outputs/main/$(DATE)/$(TIME)
FULL_ARGS = $(ARGS)

dep-install:
	apt install colorized-logs moreutils -y

uv-install:
	curl -LsSf https://astral.sh/uv/install.sh | sh

rmzi:
	bash ./tools/rmzi.sh

rm-lock:
	rm -f ./uv.lock

rm-outputs:
	rm -rf ./src/outputs

rm-pycache:
	rm -rf __pycache__ **/__pycache__

rm-venv:
	rm -rf .venv

reset: rmzi rm-lock rm-outputs rm-pycache rm-venv

start:
	mkdir -p $(MAIN_OUTPUT_DIR) && \
	uv run ./src/main.py $(FULL_ARGS) 2>&1 | tee $(MAIN_OUTPUT_DIR)/log.txt
	(cat $(MAIN_OUTPUT_DIR)/log.txt | ansi2txt) | sponge $(MAIN_OUTPUT_DIR)/log.txt

help: FULL_ARGS = --help $(ARGS)
help: start

make-help:
	cat ./make-man.txt