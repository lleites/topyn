from typing import List

from topyn.commands import run_command, get_config


def _extra_args(fix: bool, module: str) -> List[str]:

    config_path = get_config(module)
    extra_args = [
        "--config",
        str(config_path.resolve()),
    ]
    if not fix:
        extra_args.append("--check")

    return extra_args


def normalize(path: str, fix: bool) -> None:
    module = "black"
    pretty_name = "formatting"
    extra_args = _extra_args(fix, module)
    run_command(path, module, pretty_name, extra_args, fix)
