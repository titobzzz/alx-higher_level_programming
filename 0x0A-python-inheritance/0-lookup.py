#!/usr/bin/python3
"""This module returns the list of available attributes
    and methods of an object class
"""


def lookup(obj):
    """
    The functions looks out for all attributes and methods of an object"""
    return dir(obj)
