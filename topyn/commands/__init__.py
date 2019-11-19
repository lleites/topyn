import sys
from runpy import run_module
from typing import List, Callable
from pathlib import Path

import topyn.tui as tui


def run_command(
    path: str,
    module: str,
    pretty_name: str,
    extra_args: Callable[[Path], List[str]],
    api_integration: Callable[[List[str]], int] = None,
) -> None:
    tui.running(pretty_name)
    config_path = _get_config(__file__, module)
    if api_integration:
        exit_code = api_integration([path, *extra_args(config_path)])
    else:
        exit_code = _call_module(module, ["", path, *extra_args(config_path)])

    if exit_code != 0:
        tui.failed(pretty_name)
        sys.exit(exit_code)


def _call_module(module_name: str, args: List[str]) -> int:
    exit_code = 0
    sys.argv = args

    try:
        run_module(
            module_name, run_name="__main__", alter_sys=True,
        )
    except SystemExit as e:
        exit_code = e.code

    return exit_code


def _get_config(command_path: str, module_name: str) -> Path:
    return Path(command_path).parent.parent / "configs" / f"{module_name}.toml"
