DATE := $(shell date '+%Y/%m/%d')
TIME := $(shell date '+%H-%M-%S')
OUTPUT_DIR = outputs/$(DATE)/$(TIME)

uv-install:
	curl -LsSf https://astral.sh/uv/install.sh | sh

rmzi:
	bash ./tools/rmzi.sh

start:
	mkdir -p $(OUTPUT_DIR) && \
	uv run ./main.py 2>&1 | tee $(OUTPUT_DIR)/log.txt