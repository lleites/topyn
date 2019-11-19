from pathlib import Path
from typing import List

from topyn.commands import run_command


def _config_args(config_path: Path) -> List[str]:
    return [f"--config={config_path}"]


def lint(path: str) -> None:
    run_command(path, "flake8", "rules", _config_args)
