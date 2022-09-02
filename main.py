"""A string mutation application."""
from src.string_mutate import StringMutateService


def string_mutation():
    """Mutate a string using the string mutate module."""
    service = StringMutateService()
    service.add_string('test_string')
    reversed_string = service.reverse()

    print(reversed_string)


if __name__ == '__main__':
    string_mutation()
