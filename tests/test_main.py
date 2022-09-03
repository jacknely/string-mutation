"""A collection of tests for the main application."""
from click.testing import CliRunner

from main import string_mutation


def test_main():
    """Test that main returns the expected response."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open('input.txt', 'w') as file:
            file.write(
                """I am a test file full of lots of words for testing"""
            )

        result = runner.invoke(string_mutation, ['input.txt'])
        assert result.exit_code == 0
        assert result.output == (
            'gnitset rof sdrow fo stol fo lluf elif tset a ma I\n'
        )


def test_main_with_r():
    """Test that main returns the expected response."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open('input.txt', 'w') as file:
            file.write(
                """I am a test file full of lots of words for testing"""
            )

        result = runner.invoke(string_mutation, ['input.txt', '-r'])
        assert result.exit_code == 0
        assert result.output == (
            'gnitset rof sdrow fo stol fo lluf elif tset a ma I\n'
        )


def test_main_with_w():
    """Test that main returns the expected response."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open('input.txt', 'w') as file:
            file.write(
                """I am a test file full of lots of words for testing"""
            )

        result = runner.invoke(string_mutation, ['input.txt', '-w'])
        assert result.exit_code == 0
        assert result.output == (
            'testing for words of lots of full file test a am I\n'
        )


def test_main_program_exits_with_no_params():
    """Test that main exits with code 2."""
    runner = CliRunner()
    result = runner.invoke(string_mutation, [])
    assert result.exit_code == 2
    assert "Error: Missing argument 'FILE'.\n" in result.output


def test_main_raises_exits_with_code_2():
    """Test that main exits with code 2."""
    runner = CliRunner()
    result = runner.invoke(string_mutation, ['test', 'me', '-r'])
    assert result.exit_code == 2
    assert "Error: Invalid value for 'FILE'" in result.output
