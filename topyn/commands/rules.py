from typing import List

from topyn.commands import run_command, get_config


def _extra_args(module: str) -> List[str]:
    config_path = get_config(module)
    return [f"--config={config_path.resolve()}"]


def lint(path: str) -> None:
    module = "flake8"
    pretty_name = "rules"
    extra_args = _extra_args(module)
    run_command(path, module, pretty_name, extra_args)
