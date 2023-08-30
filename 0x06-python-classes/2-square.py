#!/usr/bin/python3
"""
A class that checks the validity of a squres size
"""


class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """Initializing this square class
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
