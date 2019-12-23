from pathlib import Path
from typing import List

from topyn.commands import run_command


def extra_args_function(config_path: Path, fix: bool) -> List[str]:

    extra_args = [
        "--config",
        f"{config_path}",
    ]
    if not fix:
        extra_args.append("--check")

    return extra_args


def normalize(path: str, fix: bool) -> None:
    run_command(path, "black", "formatting", extra_args_function, fix=fix)
