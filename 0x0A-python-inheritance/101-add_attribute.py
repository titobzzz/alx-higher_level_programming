#!/usr/bin/python3
"""
This module defines a function that adds attributes to objects"""


def add_attribute(obj, att, value):
    """
    This will add a new attribute to an object if possible
   @arg: 
   * obj : RThe class to add new attribut
    *att: attribute to be added
    *value: value to be printed when attribute is called 
   """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
