# {{ tmplr.project_title }}
{{ tmplr.project_description }}

## To Start
1. Ensure `uv` is installed. If not, run `make uv-install` to do so. Note that this does not automatically add the installation location to your `PATH`, so you must do that yourself.
2. In the root directory of the repository, execute the `make start` command. `uv` will be invoked, creating a virtual environment, installing dependencies, and running the code in `main.py`.

## Other Commands
* `make rmzi` - Remove all `Zone.Identifier` files from the repository. These are often created by Windows when files are downloaded from the internet.

## Requirements
**Minimum Python Version:** {{ tmplr.python_version }}

**Dependencies:**
* N/A