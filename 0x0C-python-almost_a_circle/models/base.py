#!/usr/bin/python3
"""Defines a base model class."""

import json
import csv
import turtle


class Base:
    """Base model.

    This Represent the "base" for alll other classes in the project 0x0C*.

    Private Class Attributes:

        __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __inti__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
