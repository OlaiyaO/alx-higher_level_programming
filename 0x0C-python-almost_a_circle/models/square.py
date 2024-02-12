#!/usr/bin/python3
"""Module for Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializer"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id,
                self.x,
                self.y,
                self.width)
    
    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.validate_int_value("width", value)
        self.validate_positive_value("width", value)
        self.width = value

    def update(self, *args, **kwargs):
        """Updates the instance attributes"""
        if args:
            attr_names = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attr_names[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
