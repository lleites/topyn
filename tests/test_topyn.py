from unittest.mock import patch

import py
import pytest
from _pytest.capture import CaptureFixture
from topyn import __version__
from topyn.console import run


def test_version() -> None:
    assert __version__ == "0.7.0.dev"


def _run_system_exit(path: str) -> None:
    with pytest.raises(SystemExit) as e:
        run([path])


def test_wrong_types(capsys: CaptureFixture) -> None:
    import topyn.tui

    with patch.object(topyn.tui, "failed", wraps=topyn.tui.failed) as mock_out:
        _run_system_exit("tests/resources/wrong_types")

        mock_out.assert_called_with("types")
        captured = capsys.readouterr()
        assert "Incompatible return value type" in captured.out


def test_missing_types(capsys: CaptureFixture) -> None:
    import topyn.tui

    with patch.object(topyn.tui, "failed", wraps=topyn.tui.failed) as mock_out:
        _run_system_exit("tests/resources/missing_types")

        mock_out.assert_called_with("types")
        captured = capsys.readouterr()
        assert "missing a return type annotation" in captured.out


def test_bad_rules(capsys: CaptureFixture) -> None:
    import topyn.tui

    with patch.object(topyn.tui, "failed", wraps=topyn.tui.failed) as mock_out:
        _run_system_exit("tests/resources/bad_rules")

        mock_out.assert_called_with("rules")
        captured = capsys.readouterr()
        assert "print found" in captured.out


def test_incorrect_naming(capsys: CaptureFixture) -> None:
    import topyn.tui

    with patch.object(topyn.tui, "failed", wraps=topyn.tui.failed) as mock_out:
        _run_system_exit("tests/resources/incorrect_naming")

        mock_out.assert_called_with("rules")
        captured = capsys.readouterr()
        assert "N802 function name 'iLikeCamelCase' should be lowercase" in captured.out


def test_bugbear(capsys: CaptureFixture) -> None:
    import topyn.tui

    with patch.object(topyn.tui, "failed", wraps=topyn.tui.failed) as mock_out:
        _run_system_exit("tests/resources/mutable_default_parameter")

        mock_out.assert_called_with("rules")
        captured = capsys.readouterr()
        assert "B006 Do not use mutable data structures for argument defaults" in captured.out


def test_comprehensions(capsys: CaptureFixture) -> None:
    import topyn.tui

    with patch.object(topyn.tui, "failed", wraps=topyn.tui.failed) as mock_out:
        _run_system_exit("tests/resources/unnecesary_list_call")

        mock_out.assert_called_with("rules")
        captured = capsys.readouterr()
        assert "C413 Unnecessary list call around sorted()." in captured.out


def test_wrong_formatting(capsys: CaptureFixture) -> None:
    import topyn.tui

    with patch.object(topyn.tui, "failed", wraps=topyn.tui.failed) as mock_out:
        _run_system_exit("tests/resources/wrong_formatting")

        mock_out.assert_called_with("formatting")
        captured = capsys.readouterr()
        assert "would reformat" in captured.err


def test_ok(capsys: CaptureFixture) -> None:
    import topyn.tui

    with patch.object(topyn.tui, "everything_is_ok", wraps=topyn.tui.everything_is_ok) as mock_out:
        run(["tests/resources/ok"])
        mock_out.assert_called_once()
        assert "All done! ✨ 🍰 ✨\n1 file would be left unchanged.\n" == capsys.readouterr().err


def test_fix(tmpdir: py.path.local) -> None:
    import topyn.tui

    tmp_file = tmpdir.join("file.py")
    tmp_file.write("def no_format     () -> None    :('Format me'     )")

    with patch.object(topyn.tui, "failed") as mock_out:
        _run_system_exit(str(tmpdir))
        mock_out.assert_called_with("formatting")

    with patch.object(topyn.tui, "trying_to_fix", wraps=topyn.tui.trying_to_fix) as mock_out:
        run([str(tmpdir), "--fix"])
        mock_out.assert_called_once()

    with patch.object(topyn.tui, "everything_is_ok") as mock_out:
        run([str(tmpdir)])
    mock_out.assert_called_once()


def test_fix_rules(tmpdir: py.path.local) -> None:
    import topyn.tui

    tmp_file = tmpdir.join("file.py")
    tmp_file.write("import os\n\nsome_code = 42\n")

    with patch.object(topyn.tui, "failed") as mock_out:
        _run_system_exit(str(tmpdir))
        mock_out.assert_called_with("rules")

    with patch.object(topyn.tui, "trying_to_fix", wraps=topyn.tui.trying_to_fix) as mock_out:
        run([str(tmpdir), "--fix"])
        mock_out.assert_called_once()

    with patch.object(topyn.tui, "everything_is_ok") as mock_out:
        run([str(tmpdir)])
    mock_out.assert_called_once()


def test_module_exec() -> None:
    import topyn.console

    with patch.object(topyn.console, "run") as mock_run:
        # noinspection PyUnresolvedReferences
        import topyn.__main__

        mock_run.assert_called_once()
