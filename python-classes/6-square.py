#!/usr/bin/python3
"""Create a square"""


class Square:
    """
    Defining a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize variables."""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """returns size."""
        return self.__size

    @size.setter
    def size(self, size):
        """comparing  size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def __init__(self, size=0, position=(0, 0)):
        """Initializing the data."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size to a value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
