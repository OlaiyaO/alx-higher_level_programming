#!/usr/bin/python3
"""Module for Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializer"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """String representation of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id,
                self.x,
                self.y,
                self.width,
                self.height)

    def update(self, *args, **kwargs):
        """Updates the instance attributes"""
        if args:
            attr_names = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attr_names[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        self.validate_int_value("width", value)
        self.validate_positive_value("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        self.validate_int_value("height", value)
        self.validate_positive_value("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        self.validate_int_value("x", value)
        self.validate_negative_value("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        self.validate_int_value("y", value)
        self.validate_negative_value("y", value)
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Prints the rectangle with # characters"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def validate_int_value(self, attr, value):
        """Validates if value is an integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attr))

    def validate_positive_value(self, attr, value):
        """Validates if value is positive or zero"""
        if value < 0:
            raise ValueError("{} must be > 0".format(attr))

    def validate_negative_value(self, attr, value):
        """Validates if value is negative or zero"""
        if value < 0:
            raise ValueError("{} must be >= 0".format(attr))
