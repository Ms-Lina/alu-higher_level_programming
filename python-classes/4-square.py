#!/usr/bin/python3

class Square:

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self)
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        square_area = self.__size ** 2
        return square_area
