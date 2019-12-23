from typing import List

from topyn.commands import get_config, run_command


def _extra_args(fix: bool, module: str) -> List[str]:

    config_path = get_config(module)
    extra_args = ["--settings-path", str(config_path.parent.resolve()), "-rc"]
    if not fix:
        extra_args.append("--check-only")

    return extra_args


def sort(path: str, fix: bool) -> None:
    module = "isort"
    pretty_name = "sorting imports"
    extra_args = _extra_args(fix, module)
    run_command(path, module, pretty_name, extra_args)
