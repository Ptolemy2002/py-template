# The main entry point for the uv script.
import argparse
import utils.output as output_utils
import sys
from warnings import warn

# Put any files that are an output of the script here. "log.txt" will already exist.
OUTPUTS_DIR = output_utils.get_latest_outputs_dir("main")

def main() -> None:
    print(f"Outputs directory: {OUTPUTS_DIR}")
    print("Hello, World!")


parser: argparse.ArgumentParser | None = None
def get_arg_parser() -> argparse.ArgumentParser:
    global parser

    if parser is None:
        parser = argparse.ArgumentParser(
            description="Basic uv template script.",
            formatter_class=argparse.RawDescriptionHelpFormatter
        )

        parser.add_argument(
            "--usage", "-u",
            action="store_true",
            help="Print usage instructions and examples, then exit."
        )

        parser.add_argument(
            "--manual", "-m",
            action="store_true",
            help="Print detailed manual, then exit."
        )

        """
        parser.add_argument(
            "arg",
            type=str,
            default="default_value",
            nargs="?",
            help="An example argument."
        )
        """
    
    return parser

def parse_args(og_args: list[str]):
    arg_parser = get_arg_parser()
    args = arg_parser.parse_args(og_args)

    if args.usage:
        arg_parser.print_usage()
        exit(0)

    if args.manual:
        print(output_utils.get_manual())
        exit(0)

    return args


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main()