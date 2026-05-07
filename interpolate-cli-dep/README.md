# interpolate-cli-dep

`interpolate-cli-dep` is a command-line interface for interpolation operations, built on top of `interpolate-lib`.

## Installation

Install the package with `uv` or your preferred package manager after configuring the repository:

```bash
uv install
```

## Usage

Run the CLI with the required interpolation options:

```bash
python -m interpolate-cli-dep --value 0.5 --output-min 10.0 --output-max 20.0
uv run interpolate-cli-dep --value 0.5 --output-min 10.0 --output-max 20.0
moon r cli-dep:cli -- --value 0.25  --output-min 10.0 --output-max 18.0
```

## CLI arguments

- `--value` – the value to interpolate, given between 0 and 1 included
- `--output-min` – the minimum value of the interpolation interval
- `--output-max` – the maximum value of the interpolation interval

## Project layout

- `src/interpolate_cli_dep/` – CLI source package
- `pyproject.toml` – package metadata and dependencies
