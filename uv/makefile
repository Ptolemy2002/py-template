.PHONY: uv-install rmzi rm-outputs start

DATE := $(shell date '+%Y/%m/%d')
TIME := $(shell date '+%H-%M-%S')
OUTPUT_DIR = outputs/$(DATE)/$(TIME)

uv-install:
	curl -LsSf https://astral.sh/uv/install.sh | sh

rmzi:
	bash ./tools/rmzi.sh

rm-outputs:
	rm -rf ./outputs

reset: rm-outputs

start:
	mkdir -p $(OUTPUT_DIR) && \
	uv run ./main.py $(ARGS) 2>&1 | tee $(OUTPUT_DIR)/log.txt