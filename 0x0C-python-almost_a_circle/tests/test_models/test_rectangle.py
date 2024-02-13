#!/usr/bin/python3
"""Unittests for models/rectangle.py.

Unittest classes:
    TestRectangleInstantiation: Tests for instantiating a Rectangle object.
    TestRectangleWidth: Tests for the width attribute of the Rectangle.
    TestRectangleHeight: Tests for the height attribute of the Rectangle.
    TestRectangle_X: Tests for the x attribute of the Rectangle.
    TestRectangle_Y: Tests for the y attribute of the Rectangle.
    TestRectangleInitializationOrder: Tests to ensure the correct order
                                of attribute initialization.
    TestRectangleArea: Tests for calculating the area of the Rectangle.
    TestRectangleUpdateArgs: Tests for updating Rectangle attributes
                                using positional arguments.
    TestRectangleUpdateKwargs: Tests for updating Rectangle attributes
                                using keyword arguments.
    TestRectangleToDictionary: Tests for converting a
                                Rectangle object to a dictionary format.
"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangleInstantiation(unittest.TestCase):
    """Unit tests for instantiation of the Rectangle class."""

    def test_rect_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args_for_rect(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg_for_rect(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args_for_rect(self):
        rect1 = Rectangle(10, 2)
        rect2 = Rectangle(2, 10)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_three_args_for_rect(self):
        rect1 = Rectangle(2, 2, 4)
        rect2 = Rectangle(4, 4, 2)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_four_args_for_rect(self):
        rect1 = Rectangle(1, 2, 3, 4)
        rect2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_five_args_for_rect(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_more_than_five_args_for_rect(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private_for_rect(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private_for_rect(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private_for_rect(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private_for_rect(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width_getter_for_rect(self):
        rect = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, rect.width)

    def test_width_setter_for_rect(self):
        rect = Rectangle(5, 7, 7, 5, 1)
        rect.width = 10
        self.assertEqual(10, rect.width)

    def test_height_getter_for_rect(self):
        rect = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, rect.height)

    def test_height_setter_for_rect(self):
        rect = Rectangle(5, 7, 7, 5, 1)
        rect.height = 10
        self.assertEqual(10, rect.height)

    def test_x_getter_for_rect(self):
        rect = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, rect.x)

    def test_x_setter_for_rect(self):
        rect = Rectangle(5, 7, 7, 5, 1)
        rect.x = 10
        self.assertEqual(10, rect.x)

    def test_y_getter_for_rect(self):
        rect = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, rect.y)

    def test_y_setter_for_rect(self):
        rect = Rectangle(5, 7, 7, 5, 1)
        rect.y = 10
        self.assertEqual(10, rect.y)


class TestRectWidth(unittest.TestCase):
    """Unit tests for Rectangle width attribute initialization."""

    def test_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 2)

    def test_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 1)

    def test_complex(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(5), 2)

    def test_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1, "b": 2}, 2)

    def test_bool(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)

    def test_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)

    def test_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 2)

    def test_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 2)

    def test_frozenset(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 2, 3, 1}), 2)

    def test_range(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(5), 2)

    def test_bytes(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'Python', 2)

    def test_bytearray(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'abcdefg'), 2)

    def test_memoryview(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'abcedfg'), 2)

    def test_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 2)

    def test_nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 2)

    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)


class TestRectHeight(unittest.TestCase):
    """Unit tests for Rectangle height attribute initialization."""

    def test_none(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_str(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid")

    def test_float(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 5.5)

    def test_complex(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, complex(5))

    def test_dict(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"a": 1, "b": 2})

    def test_list(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [1, 2, 3])

    def test_set(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {1, 2, 3})

    def test_tuple(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (1, 2, 3))

    def test_frozenset(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, frozenset({1, 2, 3, 1}))

    def test_range(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, range(5))

    def test_bytes(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, b'Python')

    def test_bytearray(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, bytearray(b'abcdefg'))

    def test_memoryview(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, memoryview(b'abcedfg'))

    def test_inf(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('inf'))

    def test_nan(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('nan'))

    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)

    def test_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)


class TestRectX(unittest.TestCase):
    """Unit tests for Rectangle x attribute initialization."""

    def test_none(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def test_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid", 2)

    def test_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 5.5, 9)

    def test_complex(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, complex(5))

    def test_dict(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {"a": 1, "b": 2}, 2)

    def test_bool(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, True, 2)

    def test_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2, 3], 2)

    def test_set(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {1, 2, 3}, 2)

    def test_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, (1, 2, 3), 2)

    def test_frozenset(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, frozenset({1, 2, 3, 1}))

    def test_range(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, range(5))

    def test_bytes(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, b'Python')

    def test_bytearray(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, bytearray(b'abcdefg'))

    def test_memoryview(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, memoryview(b'abcedfg'))

    def test_inf(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('inf'), 2)

    def test_nan(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('nan'), 2)

    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 3, -1, 0)


class TestRectY(unittest.TestCase):
    """Unit tests for Rectangle y attribute initialization."""

    def test_none(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, "invalid")

    def test_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 5.5)

    def test_complex(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, complex(5))

    def test_dict(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {"a": 1, "b": 2})

    def test_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, [1, 2, 3])

    def test_set(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {1, 2, 3})

    def test_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, (1, 2, 3))

    def test_frozenset(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, frozenset({1, 2, 3, 1}))

    def test_range(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, range(5))

    def test_bytes(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, b'Python')

    def test_bytearray(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, bytearray(b'abcdefg'))

    def test_memoryview(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, memoryview(b'abcedfg'))

    def test_inf(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float('inf'))

    def test_nan(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float('nan'))

    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 5, 0, -1)


class TestRectInitOrder(unittest.TestCase):
    """Unit tests for Rectangle attribute initialization order."""

    def test_width_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", "invalid height")

    def test_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, "invalid x")

    def test_width_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, 3, "invalid y")

    def test_height_before_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", "invalid x")

    def test_height_before_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", 2, "invalid y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid x", "invalid y")


class TestRectangleArea(unittest.TestCase):
    """Unit tests for the area method of the Rectangle class."""

    def test_area_small_rectangle(self):
        """Test area calculation for a small rectangle."""
        rectangle = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(20, rectangle.area())

    def test_area_large_rectangle(self):
        """Test area calculation for a large rectangle."""
        rectangle = Rectangle(9999, 9999, 0, 0, 1)
        self.assertEqual(99980001, rectangle.area())

    def test_area_changed_attributes(self):
        """Test area calculation after changing rectangle attributes."""
        rectangle = Rectangle(2, 10, 1, 1, 1)
        rectangle.width = 7
        rectangle.height = 14
        self.assertEqual(98, rectangle.area())

    def test_area_with_extra_arg(self):
        """Test area calculation with an extra argument."""
        rectangle = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError) as context:
            rectangle.area(1)
        self.assertEqual(
            "area() takes 1 positional argument but 2 were given",
            str(context.exception)
        )


class TestRectangleStrDisplay(unittest.TestCase):
    """Unit tests for the __str__ and display methods of the Rectangle class."""

    @staticmethod
    def capture_stdout(rect, method):
        """Capture and return text printed to stdout.

        Args:
            rect (Rectangle): The Rectangle to print to stdout.
            method (str): The method to run on rect.
        Returns:
            The text printed to stdout by calling method on rect.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    # Test __str__ method
    def test_str_print_width_height(self):
        rect = Rectangle(4, 6)
        capture = TestRectangleStrDisplay.capture_stdout(rect, "print")
        correct_output = "[Rectangle] ({}) 0/0 - 4/6\n".format(rect.id)
        self.assertEqual(correct_output, capture.getvalue())

    def test_str_width_height_x(self):
        rect = Rectangle(5, 5, 1)
        correct_output = "[Rectangle] ({}) 1/0 - 5/5".format(rect.id)
        self.assertEqual(correct_output, rect.__str__())

    def test_str_width_height_x_y(self):
        rect = Rectangle(1, 8, 2, 4)
        correct_output = "[Rectangle] ({}) 2/4 - 1/8".format(rect.id)
        self.assertEqual(correct_output, str(rect))

    def test_str_width_height_x_y_id(self):
        rect = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(rect))

    def test_str_changed_attributes(self):
        rect = Rectangle(7, 7, 0, 0, [4])
        rect.width = 15
        rect.height = 1
        rect.x = 8
        rect.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(rect))

    def test_str_one_arg(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            rect.__str__(1)

    # Test display method
    def test_display_width_height(self):
        rect = Rectangle(2, 3, 0, 0, 0)
        capture = TestRectangleStrDisplay.capture_stdout(rect, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def test_display_width_height_x(self):
        rect = Rectangle(3, 2, 1, 0, 1)
        capture = TestRectangleStrDisplay.capture_stdout(rect, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())

    def test_display_width_height_y(self):
        rect = Rectangle(4, 5, 0, 1, 0)
        capture = TestRectangleStrDisplay.capture_stdout(rect, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_width_height_x_y(self):
        rect = Rectangle(2, 4, 3, 2, 0)
        capture = TestRectangleStrDisplay.capture_stdout(rect, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        rect = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            rect.display(1)


class TestRectangleUpdateArgs(unittest.TestCase):
    """Unit tests for the update_args method of the Rectangle class."""

    # Test args
    def test_zero_args(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(rect))

    def test_one_arg(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(rect))

    def test_two_args(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(rect))

    def test_three_args(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(rect))

    def test_four_args(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(rect))

    def test_five_args(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(rect))

    def test_more_than_five_args(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(89, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(rect))

    def test_none_id(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(None)
        correct_output = "[Rectangle] ({}) 10/10 - 10/10".format(rect.id)
        self.assertEqual(correct_output, str(rect))

    def test_none_id_and_more_args(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(None, 4, 5, 2)
        correct_output = "[Rectangle] ({}) 2/10 - 4/5".format(rect.id)
        self.assertEqual(correct_output, str(rect))

    def test_twice_update(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(89, 2, 3, 4, 5, 6)
        rect.update(6, 5, 4, 3, 2, 89)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(rect))

    def test_invalid_width_type(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect.update(89, "invalid")

    def test_width_zero(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect.update(89, 0)

    def test_width_negative(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect.update(89, -5)

    def test_invalid_height_type(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect.update(89, 2, "invalid")

    def test_height_zero(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect.update(89, 1, 0)

    def test_height_negative(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect.update(89, 1, -5)

    def test_invalid_x_type(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect.update(89, 2, 3, "invalid")

    def test_x_negative(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rect.update(89, 1, 2, -6)

    def test_invalid_y(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect.update(89, 2, 3, 4, "invalid")

    def test_y_negative(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rect.update(89, 1, 2, 3, -6)

    def test_width_before_height(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect.update(89, "invalid", "invalid")

    def test_width_before_x(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect.update(89, "invalid", 1, "invalid")

    def test_width_before_y(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect.update(89, "invalid", 1, 2, "invalid")

    def test_height_before_x(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect.update(89, 1, "invalid", "invalid")

    def test_height_before_y(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect.update(89, 1, "invalid", 1, "invalid")

    def test_x_before_y(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect.update(89, 1, 2, "invalid", "invalid")



class TestRectangleUpdateKwargs(unittest.TestCase):
    """Unit tests for the update_kwargs method of the Rectangle class."""

    def test_one_arg(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(rect))

    def test_two_args(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(rect))

    def test_three_args(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(rect))

    def test_four_args(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(rect))

    def test_five_args(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(rect))

    def test_none_id(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(id=None)
        correct_output = "[Rectangle] ({}) 10/10 - 10/10".format(rect.id)
        self.assertEqual(correct_output, str(rect))

    def test_none_id_and_more(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(id=None, height=7, y=9)
        correct_output = "[Rectangle] ({}) 10/9 - 10/7".format(rect.id)
        self.assertEqual(correct_output, str(rect))

    def test_twice_update(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(id=89, x=1, height=2)
        rect.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(rect))

    def test_invalid_width_type(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width should be an integer"):
            rect.update(width="invalid")

    def test_width_zero(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width should be greater than zero"):
            rect.update(width=0)

    def test_width_negative(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width should be greater than zero"):
            rect.update(width=-5)

    def test_invalid_height_type(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height should be an integer"):
            rect.update(height="invalid")

    def test_height_zero(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height should be greater than zero"):
            rect.update(height=0)

    def test_height_negative(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height should be greater than zero"):
            rect.update(height=-5)

    def test_invalid_x_type(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x should be an integer"):
            rect.update(x="invalid")

    def test_x_negative(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x should be greater than or equal to zero"):
            rect.update(x=-5)

    def test_invalid_y_type(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y should be an integer"):
            rect.update(y="invalid")

    def test_y_negative(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y should be greater than or equal to zero"):
            rect.update(y=-5)

    def test_args_and_kwargs(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(89, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(rect))

    def test_wrong_keys(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(rect))

    def test_some_wrong_keys(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(height=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(rect))


class TestRectangleToDictionary(unittest.TestCase):
    """Unit tests for the to_dictionary method of the Rectangle class."""

    def test_output(self):
        rect = Rectangle(10, 2, 1, 9, 5)
        correct_output = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct_output, rect.to_dictionary())

    def test_no_object_changes(self):
        rect1 = Rectangle(10, 2, 1, 9, 5)
        rect2 = Rectangle(5, 9, 1, 2, 10)
        rect2.update(**rect1.to_dictionary())
        self.assertNotEqual(rect1, rect2)

    def test_arg(self):
        rect = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            rect.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
