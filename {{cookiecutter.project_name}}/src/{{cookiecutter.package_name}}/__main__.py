"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """{{cookiecutter.friendly_name}}."""


if __name__ == "__main__":
    main(prog_name="{{cookiecutter.package_name}}")  # pragma: no cover
