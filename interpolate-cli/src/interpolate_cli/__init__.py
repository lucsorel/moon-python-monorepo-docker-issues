"""CLI tool for interpolation utilities."""

from __future__ import annotations

import click

__all__ = ["main"]


@click.command()
@click.option(
    "--value",
    type=float,
    required=True,
    help="the value to interpolate, given between 0 and 1 included",
)
@click.option(
    "--output-min",
    "output_min",
    type=float,
    required=True,
    help="the minimum value of the interpolation interval",
)
@click.option(
    "--output-max",
    "output_max",
    type=float,
    required=True,
    help="the maximum value of the interpolation interval",
)
def main(value: float, output_min: float, output_max: float) -> None:
    """Entry point for the interpolate-cli."""
    if not 0 <= value <= 1:
        raise click.BadParameter("--value must be between 0 and 1 inclusive.")

    click.echo(output_min + value * (output_max - output_min))
