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
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieving height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting height value"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            
             def area(self):
                 """Defining area"""
                 return self.__width * self.__height

    def perimeter(self):
        """Perimeter of  rectngle"""
        if self.__width == 0 or self.height == 0:
            return 0
        return 2 * (self.__width + self.__height)
