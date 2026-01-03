.PHONY: uv-install rmzi rm-outputs rm-pycache rm-venv reset start

DATE := $(shell date '+%Y/%m/%d')
TIME := $(shell date '+%H-%M-%S')

MAIN_OUTPUT_DIR = outputs/main/$(DATE)/$(TIME)
FULL_ARGS = $(ARGS)

uv-install:
	curl -LsSf https://astral.sh/uv/install.sh | sh

rmzi:
	bash ./tools/rmzi.sh

rm-outputs:
	rm -rf ./outputs

rm-pycache:
	rm -rf __pycache__ **/__pycache__

rm-venv:
	rm -rf .venv

reset: rmzi rm-outputs rm-pycache rm-venv

start:
	mkdir -p $(MAIN_OUTPUT_DIR) && \
	uv run ./main.py $(FULL_ARGS) 2>&1 | tee $(MAIN_OUTPUT_DIR)/log.txt

# Alternative start example (put both following lines together):
# start_with_first_arg: FULL_ARGS = first_arg $(ARGS)
# start_with_first_arg: start