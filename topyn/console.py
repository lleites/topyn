import argparse
from typing import List, Optional

import topyn.commands.rules as rules
import topyn.commands.format as format_
import topyn.commands.types as types

import topyn
import topyn.tui as tui


def run(args: Optional[List[str]] = None) -> None:

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="Typed Opinionated PYthon Normalizer",
    )
    parser.add_argument(
        "path", help="path to topynize", type=str, default=".", nargs="?"
    )
    parser.add_argument("--fix", help="try to fix my code", action="store_true")
    parser.add_argument(
        "--version", action="version", version=topyn.__version__
    )

    parsed_args = parser.parse_args(args=args)

    path = parsed_args.path
    fix = parsed_args.fix

    if parsed_args.fix:
        tui.trying_to_fix()

    format_.normalize(path, fix)
    rules.lint(path)
    types.check(path)

    tui.everything_is_ok()
