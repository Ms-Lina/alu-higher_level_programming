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
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
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
         raise ValueError("height must be >= 0")
        self.__height = value
    
             def area(self):
                 """Defining area"""
                 return self.__width * self.__height

    def perimeter(self):
        """Perimeter of  rectngle"""
        if self.__width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)


    def __str__(self):
        """string representation of the triangle using the '#'..."""
        if self.__width == 0 or self.__height == 0:
            return ""
         else:
            rect = ''
            for i in range(self.__height):
                for x in range(self.__width):
                    rect = rect + '#'

                rect += '\n'
            return rect[:-1]