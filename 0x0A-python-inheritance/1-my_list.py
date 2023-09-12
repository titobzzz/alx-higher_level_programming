#!/usr/bin/python3
"""This module inherits from the list class"""


class MyList(list):
    """
    The class that inherits from list
    """
    def print_sorted(self):
        """
        The method prints a sorted list"""
        print(sorted(self))
