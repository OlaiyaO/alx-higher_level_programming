#!/usr/bin/python3
"""Unittests for base.py.

Unittest classes:
    TestBaseInstantiation: Tests for the instantiation of the Base itself.
    TestToJSONString: Tests for the Base.to_json_string() method.
    TestFromJSONString: Tests for the Base.from_json_string() method.
    TestSaveToFile: Tests for the Base.save_to_file() method.
    TestLoadFromFile: Tests for the Base.load_from_file() method.
    TestCreateInstance: Tests for the Base.create() method.
    TestSaveToFileCSV: Tests for the Base.save_to_file_csv() method.
    TestLoadFromFileCSV: Tests for the Base.load_from_file_csv() method.
    TestDraw: Tests for the Base.draw() method.
"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstantiation(unittest.TestCase):
    """Tests for ensuring proper instantiation of the Base class."""

    def test_base_no_arg(self):
        instance1 = Base()
        instance2 = Base()
        self.assertEqual(instance1.identifier, instance2.identifier - 1)

    def test_three_base_instances(self):
        instance1 = Base()
        instance2 = Base()
        instance3 = Base()
        self.assertEqual(instance1.identifier, instance3.identifier - 2)

    def test_none_id(self):
        instance1 = Base(None)
        instance2 = Base(None)
        self.assertEqual(instance1.identifier, instance2.identifier - 1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).identifier)

    def test_number_of_instances_after_unique_id(self):
        instance1 = Base()
        instance2 = Base(12)
        instance3 = Base()
        self.assertEqual(instance1.identifier, instance3.identifier - 1)

    def test_id_mutable(self):
        instance = Base(12)
        instance.identifier = 15
        self.assertEqual(15, instance.identifier)

    def test_private_number_of_instances(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__number_of_instances)

    def test_string_id(self):
        self.assertEqual("hello", Base("hello").identifier)

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).identifier)

    def test_complex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).identifier)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).identifier)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).identifier)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).identifier)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).identifier)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).identifier)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).identifier)

    def test_range_id(self):
        self.assertEqual(range(5), Base(range(5)).identifier)

    def test_bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').identifier)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).identifier)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).identifier)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).identifier)

    def test_nan_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).identifier)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

class TestToJSONString(unittest.TestCase):
    """Tests for validating the to_json_string method of the Base class."""

    def test_rectangle_to_json_string_type(self):
        rect = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([rect.to_dictionary()])))

    def test_rectangle_to_json_string_single_dict(self):
        rect = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([rect.to_dictionary()])) == 53)

    def test_rectangle_to_json_string_two_dicts(self):
        rect1 = Rectangle(2, 3, 5, 19, 2)
        rect2 = Rectangle(4, 2, 4, 1, 12)
        dict_list = [rect1.to_dictionary(), rect2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(dict_list)) == 106)

    def test_square_to_json_string_type(self):
        sqr = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([sqr.to_dictionary()])))

    def test_square_to_json_string_single_dict(self):
        sqr = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([sqr.to_dictionary()])) == 39)

    def test_square_to_json_string_two_dicts(self):
        sqr1 = Square(10, 2, 3, 4)
        sqr2 = Square(4, 5, 21, 2)
        dict_list = [sqr1.to_dictionary(), sqr2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(dict_list)) == 78)

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

class TestFromJSONString(unittest.TestCase):
    """Tests for validating the from_json_string method of the Base class."""

    def test_json_string_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_json_string_single_rectangle(self):
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_json_string_multiple_rectangles(self):
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_json_string_single_square(self):
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_json_string_multiple_squares(self):
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_json_string_with_None_input(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_json_string_with_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_json_string_with_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_json_string_with_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)

class TestSaveToFile(unittest.TestCase):
    """Tests for verifying the save_to_file method of the Base class."""

    @classmethod
    def tearDownClass(cls):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass
        try:
            os.remove("Base.json")
        except FileNotFoundError:
            pass

    def test_save_to_file_single_rectangle(self):
        rect = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([rect])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 53)

    def test_save_to_file_multiple_rectangles(self):
        rect1 = Rectangle(10, 7, 2, 8, 5)
        rect2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([rect1, rect2])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 105)

    def test_save_to_file_single_square(self):
        sqr = Square(10, 7, 2, 8)
        Square.save_to_file([sqr])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 39)

    def test_save_to_file_multiple_squares(self):
        sqr1 = Square(10, 7, 2, 8)
        sqr2 = Square(8, 1, 2, 3)
        Square.save_to_file([sqr1, sqr2])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 77)

    def test_save_to_file_with_class_name_for_filename(self):
        sqr = Square(10, 7, 2, 8)
        Base.save_to_file([sqr])
        with open("Base.json", "r") as file:
            self.assertTrue(len(file.read()) == 39)

    def test_save_to_file_overwrite_existing_file(self):
        sqr = Square(9, 2, 39, 2)
        Square.save_to_file([sqr])
        sqr = Square(10, 7, 2, 8)
        Square.save_to_file([sqr])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 39)

    def test_save_to_file_with_None_input(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_save_to_file_with_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_save_to_file_with_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_with_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)

class TestLoadFromFile(unittest.TestCase):
    """Tests for verifying the load_from_file method of the Base class."""

    @classmethod
    def tearDownClass(cls):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass
   def test_load_file_first_rectangle(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rect1, rect2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(rect1), str(list_rectangles_output[0]))

    def test_load_file_second_rectangle(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rect1, rect2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(rect2), str(list_rectangles_output[1]))

    def test_load_file_rectangle_types(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rect1, rect2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(isinstance(obj, Rectangle) for obj in output))

    def test_load_file_first_square(self):
        sqr1 = Square(5, 1, 3, 3)
        sqr2 = Square(9, 5, 2, 3)
        Square.save_to_file([sqr1, sqr2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(sqr1), str(list_squares_output[0]))

    def test_load_file_second_square(self):
        sqr1 = Square(5, 1, 3, 3)
        sqr2 = Square(9, 5, 2, 3)
        Square.save_to_file([sqr1, sqr2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(sqr2), str(list_squares_output[1]))

    def test_load_file_square_types(self):
        sqr1 = Square(5, 1, 3, 3)
        sqr2 = Square(9, 5, 2, 3)
        Square.save_to_file([sqr1, sqr2])
        output = Square.load_from_file()
        self.assertTrue(all(isinstance(obj, Square) for obj in output))

    def test_load_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_file_with_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)
 
class TestCreateInstance(unittest.TestCase):
    """Tests for verifying the create method of the Base class."""

    def test_create_rectangle_original(self):
        rect1 = Rectangle(3, 5, 1, 2, 7)
        rect1_dict = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dict)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rect1))

    def test_create_rectangle_new(self):
        rect1 = Rectangle(3, 5, 1, 2, 7)
        rect1_dict = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dict)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rect2))

    def test_create_rectangle_identity(self):
        rect1 = Rectangle(3, 5, 1, 2, 7)
        rect1_dict = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dict)
        self.assertIsNot(rect1, rect2)

    def test_create_rectangle_equality(self):
        rect1 = Rectangle(3, 5, 1, 2, 7)
        rect1_dict = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dict)
        self.assertNotEqual(rect1, rect2)

    def test_create_square_original(self):
        sqr1 = Square(3, 5, 1, 7)
        sqr1_dict = sqr1.to_dictionary()
        sqr2 = Square.create(**sqr1_dict)
        self.assertEqual("[Square] (7) 5/1 - 3", str(sqr1))

    def test_create_square_new(self):
        sqr1 = Square(3, 5, 1, 7)
        sqr1_dict = sqr1.to_dictionary()
        sqr2 = Square.create(**sqr1_dict)
        self.assertEqual("[Square] (7) 5/1 - 3", str(sqr2))

    def test_create_square_identity(self):
        sqr1 = Square(3, 5, 1, 7)
        sqr1_dict = sqr1.to_dictionary()
        sqr2 = Square.create(**sqr1_dict)
        self.assertIsNot(sqr1, sqr2)

    def test_create_square_equality(self):
        sqr1 = Square(3, 5, 1, 7)
        sqr1_dict = sqr1.to_dictionary()
        sqr2 = Square.create(**sqr1_dict)
        self.assertNotEqual(sqr1, sqr2)

class TestSaveToFileCSV(unittest.TestCase):
    """Tests for verifying the save_to_file_csv method of the Base class."""

    @classmethod
    def tearDownClass(cls):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.csv")
        except FileNotFoundError:
            pass
        try:
            os.remove("Base.csv")
        except FileNotFoundError:
            pass

    def test_save_one_rectangle_csv(self):
        rect = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([rect])
        with open("Rectangle.csv", "r") as file:
            self.assertTrue("5,10,7,2,8", file.read())

    def test_save_two_rectangles_csv(self):
        rect1 = Rectangle(10, 7, 2, 8, 5)
        rect2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([rect1, rect2])
        with open("Rectangle.csv", "r") as file:
            self.assertTrue("5,10,7,2,8\n3,2,4,1,2", file.read())

    def test_save_one_square_csv(self):
        sqr = Square(10, 7, 2, 8)
        Square.save_to_file_csv([sqr])
        with open("Square.csv", "r") as file:
            self.assertTrue("8,10,7,2", file.read())

    def test_save_two_squares_csv(self):
        sqr1 = Square(10, 7, 2, 8)
        sqr2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([sqr1, sqr2])
        with open("Square.csv", "r") as file:
            self.assertTrue("8,10,7,2\n3,8,1,2", file.read())

    def test_save_cls_name_csv(self):
        sqr = Square(10, 7, 2, 8)
        Base.save_to_file_csv([sqr])
        with open("Base.csv", "r") as file:
            self.assertTrue("8,10,7,2", file.read())

    def test_save_overwrite_csv(self):
        sqr = Square(9, 2, 39, 2)
        Square.save_to_file_csv([sqr])
        sqr = Square(10, 7, 2, 8)
        Square.save_to_file_csv([sqr])
        with open("Square.csv", "r") as file:
            self.assertTrue("8,10,7,2", file.read())

    def test_save_None_csv(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as file:
            self.assertEqual("[]", file.read())

    def test_save_empty_list_csv(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as file:
            self.assertEqual("[]", file.read())

    def test_save_no_args_csv(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_multiple_args_csv(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)

class TestLoadFromFileCSV(unittest.TestCase):
    """Tests for verifying the load_from_file_csv method of Base class."""

    @classmethod
    def tearDownClass(cls):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.csv")
        except FileNotFoundError:
            pass

    def test_load_one_rectangle_csv(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rect1, rect2])
        output = Rectangle.load_from_file_csv()
        self.assertEqual(str(rect1), str(output[0]))

    def test_load_two_rectangles_csv(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rect1, rect2])
        output = Rectangle.load_from_file_csv()
        self.assertEqual(str(rect2), str(output[1]))

    def test_load_rectangle_types_csv(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rect1, rect2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(isinstance(obj, Rectangle) for obj in output))

    def test_load_one_square_csv(self):
        sqr1 = Square(5, 1, 3, 3)
        sqr2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([sqr1, sqr2])
        output = Square.load_from_file_csv()
        self.assertEqual(str(sqr1), str(output[0]))

    def test_load_two_squares_csv(self):
        sqr1 = Square(5, 1, 3, 3)
        sqr2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([sqr1, sqr2])
        output = Square.load_from_file_csv()
        self.assertEqual(str(sqr2), str(output[1]))

    def test_load_square_types_csv(self):
        sqr1 = Square(5, 1, 3, 3)
        sqr2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([sqr1, sqr2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(isinstance(obj, Square) for obj in output))

    def test_load_no_file_csv(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_more_than_one_arg_csv(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)

if __name__ == "__main__":
    unittest.main()
