from typing import List

import topyn.tui as tui
from topyn.commands import run_command, get_config
from mypy.api import run


def _extra_args(module: str) -> List[str]:
    config_path = get_config(module)
    return ["--config-file", str(config_path.resolve())]


def check(path: str) -> None:
    module = "mypy"
    pretty_name = "types"
    extra_args = _extra_args(module)
    run_command(
        path,
        module,
        pretty_name,
        extra_args,
        api_integration=api_integration,
    )


def api_integration(args: List[str]) -> int:
    error, _, exit_code = run(args)

    if exit_code != 0:
        tui.out(error)

    return exit_code
