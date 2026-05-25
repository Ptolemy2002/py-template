from typing import TypedDict, Literal, NotRequired, Any, Callable, Sequence, cast, Unpack
from argparse import ArgumentParser, Action, RawDescriptionHelpFormatter

# Manually typing valid ArgParse inputs so that we can use them with type safety
CLIAction = Literal[
    # Simply store the value provided by the user
    "store",
    # Store the value in the "const" parameter if the flag is present
    "store_const",
    # Store the boolean True if the flag is present
    "store_true",
    # Store the boolean False if the flag is present
    "store_false",

    # Keep a running list that gets appended to each time the flag appears
    "append",
    "append_const",

    # Like "append", but for flags that can have multiple values (e.g. --foo 1 2 3)
    "extend",

    # Count the number of times the flag appears
    "count",

    # Print help and exit if the flag is present
    "help",

    # Print the version and exit if the flag is present
    "version",
] | Action # A subclass of the built-in "Action" class that can be used for custom actions

CLINArgs = int | Literal[
    # 0 or 1 argument. The value of const is used if 0 arguments are provided,
    # but the flag is present. If the flag is not present, the value of default is used.
    "?",

    # 0 or more arguments. The value of const is used if 0 arguments are provided,
    # but the flag is present. If the flag is not present, the value of default is used.
    "*",

    # 1 or more arguments. The value of default is used if the flag is not present.
    "+"
]

class CLIArgumentDef(TypedDict):
    flags: list[str]

    action: NotRequired[CLIAction]
    nargs: NotRequired[CLINArgs]
    const: NotRequired[Any]
    
    # Processed through `type` if it is a string
    # argparse.SUPPRESS means no attribute is added
    # if the flag is not present.
    default: NotRequired[Any]

    # throw argparse.ArgumentTypeError or ValueError or TypeError if the value is invalid.
    type: NotRequired[Callable[[str], Any]]

    choices: NotRequired[Sequence[Any]]
    required: NotRequired[bool]
    help: NotRequired[str]

    # Name the argument for usage strings
    metavar: NotRequired[str]

    # Name the attribute this argument will be stored in. By default, this is derived from the flags.
    dest: NotRequired[str]

    deprecated: NotRequired[bool]

def has_arg(parser: ArgumentParser, arg: str) -> bool:
    """Returns True if the parser has an argument named arg."""
    for action in parser._actions:
        if arg in action.option_strings:
            return True
    return False

def try_add_arg(parser: ArgumentParser, arg_def: CLIArgumentDef) -> bool:
    """Tries to add an argument to the parser. Returns True if successful, False if the argument already exists."""
    for flag in arg_def["flags"]:
        if has_arg(parser, flag):
            return False
    
    # Extract only valid add_argument parameters
    invalid_keys = {"flags"}
    kwargs = {k: v for k, v in arg_def.items() if k not in invalid_keys}
    
    parser.add_argument(*arg_def["flags"], **cast(Any, kwargs))

    return True

class GetOrCreateArgParserOptions(TypedDict):
    arg_defs: NotRequired[list[CLIArgumentDef]]
    description: NotRequired[str]

parsers: dict[str, ArgumentParser] = {}
def get_or_create_arg_parser(name: str = "global", **kwargs: Unpack[GetOrCreateArgParserOptions]) -> ArgumentParser:
    global parsers

    arg_defs = kwargs.get("arg_defs", [])
    description = kwargs.get("description", "Basic uv template script.")

    if name not in parsers:
        parsers[name] = ArgumentParser(
            description=description,
            formatter_class=RawDescriptionHelpFormatter
        )

        parser = parsers[name]
        
        for arg_def in arg_defs:
            try_add_arg(parser, arg_def)
    
    return parsers[name]

def parse_args(og_args: list[str], name: str = "global", **kwargs: Unpack[GetOrCreateArgParserOptions]):
    arg_parser = get_or_create_arg_parser(name, **kwargs)
    args = arg_parser.parse_args(og_args)
    return args