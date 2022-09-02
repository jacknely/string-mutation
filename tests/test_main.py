"""A collection of tests for the main application."""
from main import string_mutation


def test_main(capsys):
    """Test that main returns the expected response."""
    string_mutation()
    captured = capsys.readouterr()
    assert captured.out.strip() == 'gnirts_tset'
