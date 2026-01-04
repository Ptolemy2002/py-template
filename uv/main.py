import argparse

def main():
    print("Hello, World!")


if __name__ == "__main__":
    man = "No manual available."
    try:
        with open("man.txt", "r") as f:
            man = f.read()
    except FileNotFoundError:
        # Just go with the default message
        pass

    parser = argparse.ArgumentParser(
        description="Basic uv template script.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=man
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

    main()