from unittest.mock import patch

import py
import pytest

from topyn import __version__
from topyn.console import run


def test_version() -> None:
    assert __version__ == "0.1.0"


def _run_system_exit(path: str, expected_code: int = 1) -> None:
    with pytest.raises(SystemExit) as e:
        run([path])
        assert e.code == expected_code


def test_wrong_types() -> None:
    import topyn.tui

    with patch.object(topyn.tui, "failed", wraps=topyn.tui.failed) as mock_out:
        _run_system_exit("tests/resources/wrong_types")

        mock_out.assert_called_with("types")


def test_missing_types() -> None:
    import topyn.tui

    with patch.object(topyn.tui, "failed", wraps=topyn.tui.failed) as mock_out:
        _run_system_exit("tests/resources/missing_types")

        mock_out.assert_called_with("types")


def test_bad_options() -> None:
    import topyn.tui

    with patch.object(topyn.tui, "failed", wraps=topyn.tui.failed) as mock_out:
        _run_system_exit("tests/resources/bad_options")

        mock_out.assert_called_with("rules")


def test_wrong_formatting() -> None:
    import topyn.tui

    with patch.object(topyn.tui, "failed", wraps=topyn.tui.failed) as mock_out:
        _run_system_exit("tests/resources/wrong_formatting")

        mock_out.assert_called_with("formatting")


def test_ok() -> None:
    import topyn.tui

    with patch.object(
        topyn.tui, "everything_is_ok", wraps=topyn.tui.everything_is_ok
    ) as mock_out:
        run(["tests/resources/ok"])
        mock_out.assert_called_once()


def test_fix(tmpdir: py.path.local) -> None:
    import topyn.tui

    tmp_file = tmpdir.join("file.py")
    tmp_file.write("def no_format     () -> None    :('Format me'     )")

    with patch.object(topyn.tui, "failed") as mock_out:
        _run_system_exit(str(tmpdir))
        mock_out.assert_called_with("formatting")

    with patch.object(
        topyn.tui, "trying_to_fix", wraps=topyn.tui.trying_to_fix
    ) as mock_out:
        run([str(tmpdir), "--fix"])
        mock_out.assert_called_once()

    with patch.object(topyn.tui, "everything_is_ok") as mock_out:
        run([str(tmpdir)])
    mock_out.assert_called_once()
