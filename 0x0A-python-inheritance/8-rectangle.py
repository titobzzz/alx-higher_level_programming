#!/usr/bin/python3
"""Inherits from baseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    The class to define rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """
        Intialiation method for a new Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
