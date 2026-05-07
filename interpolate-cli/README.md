# interpolate-cli

`interpolate-cli` is a command-line interface for interpolation operations, built on top of `interpolate-lib`.

## Installation

Install the package with `uv` or your preferred package manager after configuring the repository:

```bash
uv install
```

## Usage

Run the CLI with the required interpolation options:

```bash
python -m interpolate-cli --value 0.5 --output-min 10.0 --output-max 20.0
uv run interpolate-cli --value 0.5 --output-min 10.0 --output-max 20.0
moon r cli:cli -- --value 0.25  --output-min 10.0 --output-max 18.0
```

Example output:

```text
value=0.5, output_min=10.0, output_max=20.0
```

## CLI arguments

- `--value` – the value to interpolate, given between 0 and 1 included
- `--output-min` – the minimum value of the interpolation interval
- `--output-max` – the maximum value of the interpolation interval

## Project layout

- `src/interpolate_cli/` – CLI source package
- `pyproject.toml` – package metadata and dependencies
