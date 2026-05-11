from click.testing import CliRunner
from interpolate_cli_dep import main

def test_interpolate_cli():
    runner = CliRunner()
    result = runner.invoke(main, ['--value', '0.5', '--output-min', '10.0', '--output-max', '20.0'])
    assert result.exit_code == 0
    assert result.output == '15.0\n'
