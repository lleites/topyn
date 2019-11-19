from pathlib import Path
from typing import List

import topyn.tui as tui
from topyn.commands import run_command
from mypy.api import run


def _config_args(config_path: Path) -> List[str]:
    return ["--config-file", f"{config_path}"]


def check(path: str) -> None:
    run_command(path, "mypy", "types", _config_args, api_integration)


def api_integration(args: List[str]) -> int:
    error, _, exit_code = run(args)

    if exit_code != 0:
        tui.out(error)

    return exit_code
