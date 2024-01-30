#!/usr/bin/python3
"""Class Rectangle that defines a rectangle."""


class Rectangle:
    """Class Rectangle that defines a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a rectangle with specified width and height.

        Args:
            width (int): The width of the rectangle. Default is 0.
            height (int): The height of the rectangle. Default is 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join([
            str(self.print_symbol) * self.__width
            for _ in range(self.__height)
            ])

    def __repr__(self):
        """Return a string representation that can recreate the object."""
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def __eq__(self, other):
        """Check if two rectangles are equal."""
        if not isinstance(other, Rectangle):
            return False
        return (
                self.__width == other.__width and
                self.__height == other.__height
                )

        def __ne__(self, other):
            """Check if two rectangles are not equal."""
        return not self.__eq__(other)

    def __gt__(self, other):
        """Check if the current rectangle is greater than the other."""
        if not isinstance(other, Rectangle):
            raise ValueError(
                    "Can't compare Rectangle with non-Rectangle type"
                    )
            return self.area() > other.area()

    def __lt__(self, other):
        """Check if the current rectangle is less than the other."""
        if not isinstance(other, Rectangle):
            raise ValueError(
                    "Can't compare Rectangle with non-Rectangle type"
                    )
            return self.area() < other.area()

    def __ge__(self, other):
        """Check if a rectangle is greater than or equal to the another."""
        if not isinstance(other, Rectangle):
            raise ValueError(
                    "Can't compare Rectangle with non-Rectangle type"
                    )
            return self.area() >= other.area()

    def __le__(self, other):
        """Check if a rectangle is less than or equal to the another."""
        if not isinstance(other, Rectangle):
            raise ValueError(
                    "Can't compare Rectangle with non-Rectangle type"
                    )
            return self.area() <= other.area()

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the greater area, or rect_1 if equal.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Raises:
            TypeError: If either rect_1 or rect_2 is not a rectangle instance.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
