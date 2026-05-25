# The main entry point for the uv script.
import utils.output as output_utils
from utils.argparse import get_or_create_arg_parser, parse_args
import sys
from warnings import warn

# Put any files that are an output of the script here. "log.txt" will be written here after the script is done
# if run with make.
OUTPUTS_DIR = output_utils.get_latest_outputs_dir("main")

def main() -> None:
    print("Hello, World!")


if __name__ == "__main__":
    print(f"Outputs directory: {OUTPUTS_DIR}")
    print(f"Run with make: {output_utils.RUN_WITH_MAKE}")
    parser = get_or_create_arg_parser(
        "global",
        description="Basic uv template script.",
        arg_defs=[
            {
                "flags": ["--usage", "-u"],
                "action": "store_true",
                "help": "Print usage instructions and examples, then exit."
            },
            {
                "flags": ["--manual", "-m"],
                "action": "store_true",
                "help": "Print detailed manual, then exit."
            },

            # {
            #    "flags": ["arg"],
            #    "type": str,
            #    "default": "default_value",
            #    "nargs": "?",
            #    "help": "An example argument."
            # }
        ]
    )

    args = parse_args(sys.argv[1:], name="global")

    if args.usage:
        parser.print_usage()
        exit(0)

    if args.manual:
        print(output_utils.get_manual())
        exit(0)

    main()