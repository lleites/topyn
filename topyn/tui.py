import click


def out(msg: str) -> None:
    click.echo(msg)


def trying_to_fix() -> None:
    out("Trying to fix your code 🤞")


def checking(pretty_name: str) -> None:
    out(f"➡️ Checking {pretty_name} ...")


def fixing(pretty_name: str) -> None:
    out(f"➡️ Fixing {pretty_name} ...")


def failed(pretty_name: str) -> None:
    out(f"🔴 Sadly, {pretty_name} failed 😢")


def everything_is_ok() -> None:
    out("✅ Everything is OK! 😎")
