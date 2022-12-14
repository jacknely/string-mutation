"""A collection of tests for the string mutate service."""
import pytest
from src.string_mutate import StringMutateService


@pytest.fixture()
def service():
    """A service for use in tests."""
    return StringMutateService()


@pytest.mark.parametrize(
    'string, result',
    [
        ('test', 'tset'),
        ('test1234#slkf sff', 'ffs fkls#4321tset'),
        ('1234556', '6554321')
    ]
)
def test_reverse(service, string, result):
    """Test that methods returns expected"""
    service.add_string(string)
    assert service.reverse() == result


@pytest.mark.parametrize(
    'string, result',
    [
        ('test me once', 'once me test'),
        ('I aM a Test 1', '1 Test a aM I'),
        ('11 223 4392 a', 'a 4392 223 11'),
        ('test', 'test')
    ]
)
def test_reverse_words(service, string, result):
    """Test that methods returns expected"""
    service.add_string(string)
    assert service.reverse_words() == result


def test_reverse_raise_exception(service):
    """Test that methods returns expected"""
    with pytest.raises(TypeError) as error:
        service.add_string(1)

    assert 'Input must be a str type.' in str(error)
