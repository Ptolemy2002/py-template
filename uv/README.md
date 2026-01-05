# {{ tmplr.project_title }}
{{ tmplr.project_description }}

## To Start
1. Ensure `uv` is installed. If not, run `make uv-install` to do so. Note that this does not automatically add the installation location to your `PATH`, so you must do that yourself.
2. In the root directory of the repository, execute the `make start ARGS="..."` command. `uv` will be invoked, creating a virtual environment, installing dependencies, and running the code in `main.py`.

## Requirements
**Minimum Python Version:** {{ tmplr.python_version }}

**Python Dependencies:**
* `colorama` - for cross-platform colored terminal text.

**Linux Dependencies:**
* `colorized-logs` - for removing ANSI color codes from log files.
* `moreutils` - for the `sponge` command used in log file processing.