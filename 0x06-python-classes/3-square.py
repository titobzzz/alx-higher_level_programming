#!/usr/bin/python3
"""
A class that gives the area of a square
"""


class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        Returns: The square of the size
        """

        return (self.__size ** 2)
