.PHONY: uv-install rmzi rm-outputs start

DATE := $(shell date '+%Y/%m/%d')
TIME := $(shell date '+%H-%M-%S')
MAIN_OUTPUT_DIR = outputs/main/$(DATE)/$(TIME)

uv-install:
	curl -LsSf https://astral.sh/uv/install.sh | sh

rmzi:
	bash ./tools/rmzi.sh

rm-outputs:
	rm -rf ./outputs

reset: rm-outputs

start:
	mkdir -p $(MAIN_OUTPUT_DIR) && \
	uv run ./main.py $(ARGS) 2>&1 | tee $(MAIN_OUTPUT_DIR)/log.txt