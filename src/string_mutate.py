"""A module for mutating strings."""


class StringMutateService:
    """A class to represent a StringMutationService."""

    def __init__(self, string: str = None) -> None:
        """Initialise a StringMutationService.

        Args:
            string: An optional string to initialise in service.

        Returns:
            An initialised StringMutationService.
        """
        self._string = string

    def add_string(self, string: str) -> None:
        """Adds a string object to service.

        Args:
            string: A string object to mutate.

        Raises:
            TypeError: If object passed is not a string.
        """
        if not isinstance(string, str):
            raise TypeError('Input must be a str type.')
        self._string = string

    def reverse(self) -> str:
        """Returns the reverse of initialised string."""
        return self._string[::-1]
