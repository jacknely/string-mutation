"""A collection of tests for the main application."""
from click.testing import CliRunner

from main import string_mutation


def test_main():
    """Test that main returns the expected response."""
    runner = CliRunner()
    result = runner.invoke(string_mutation, ['-s', 'test me please.'])
    assert result.exit_code == 0
    assert result.output == '.esaelp em tset\n'


def test_main_with_r():
    """Test that main returns the expected response."""
    runner = CliRunner()
    result = runner.invoke(string_mutation, ['-s', 'test me please.', '-r'])
    assert result.exit_code == 0
    assert result.output == '.esaelp em tset\n'


def test_main_with_w():
    """Test that main returns the expected response."""
    runner = CliRunner()
    result = runner.invoke(string_mutation, ['-s', 'test me please.', '-w'])
    assert result.exit_code == 0
    assert result.output == 'please. me test\n'


def test_main_program_exits_with_no_params():
    """Test that main exits with code 2."""
    runner = CliRunner()
    result = runner.invoke(string_mutation, ['-s'])
    assert result.exit_code == 2
    assert "Error: Option '-s' requires an argument.\n" in result.output


def test_main_raises_exits_with_code_2():
    """Test that main exits with code 2."""
    runner = CliRunner()
    result = runner.invoke(string_mutation, ['-s', 'test', 'me', '-r'])
    assert result.exit_code == 2
    assert 'Got unexpected extra argument (me)' in result.output