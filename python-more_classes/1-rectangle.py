#!/usr/bin/python3
""" Creating a rectangle"""


class Rectangle:
    """defining rectangle"""

    def __init__(self, width=0, height=0):
        """initializing  rectangle"""
         self.width = width
         self.height = height

    @property
    def width(self):
        """Retrieving width value"""
         return self.__width

    @width.setter
    def width(self, value):
        """setting width value"""
         if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
            self.__width = value

    @property
    def height(self):
        """Retrieving height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting height value"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
            self.__height = value
