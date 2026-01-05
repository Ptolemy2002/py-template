# The main entry point for the uv script.
import argparse
import utils

# Put any files that are an output of the script here. "log.txt" will already exist.
OUTPUTS_DIR = utils.get_latest_outputs_dir("main")

def main() -> None:
    print(f"Outputs directory: {OUTPUTS_DIR}")
    print("Hello, World!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Basic uv template script.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=utils.get_manual()
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

    args = parser.parse_args()

    main()