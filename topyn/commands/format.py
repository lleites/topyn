from pathlib import Path
from typing import List, Callable

from topyn.commands import run_command


def extra_args_function(fix: bool) -> Callable[[Path], List[str]]:
    def _extra(config_path: Path) -> List[str]:
        extra_args = [
            "--config",
            f"{config_path}",
        ]
        if not fix:
            extra_args.append("--check")
        return extra_args

    return _extra


def normalize(path: str, fix: bool) -> None:
    run_command(path, "black", "formatting", extra_args_function(fix))
