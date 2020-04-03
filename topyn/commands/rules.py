from typing import List

from topyn.commands import run_command, get_config

PRETTY_NAME = "rules"


def _extra_args(module: str) -> List[str]:
    config_path = get_config(module)
    return [f"--config={config_path.resolve()}"]


def lint(path: str) -> None:
    module = "flake8"
    extra_args = _extra_args(module)
    run_command(path, module, PRETTY_NAME, extra_args)


def clean(path: str) -> None:
    module = "autoflake"
    extra_args = ["--in-place", "--recursive", "--remove-all-unused-imports"]
    run_command(path, module, PRETTY_NAME, extra_args, fix=True)
