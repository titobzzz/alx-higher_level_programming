#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Creatsa a square object"""

    def __init__(self, size):
        """
        Initializatio of a new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
