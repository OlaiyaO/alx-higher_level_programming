#!/usr/bin/python3
"""Module for Base class"""
import json
import csv
import turtle


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializer"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts dictionary to JSON string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r', encoding='utf-8') as f:
                return [
                        cls.create(**dic)
                        for dic in cls.from_json_string(f.read())
                        ]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                obj_list = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(obj_list))

    @staticmethod
    def from_json_string(json_string):
        """Converts JSON string to list of dictionaries"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Create a dummy instance
        elif cls.__name__ == "Square":
            dummy = cls(1)  # Create a dummy instance
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save CSV representation of list of objects to file"""
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if list_objs:
                for obj in list_objs:
                    if cls.__name__ == 'Rectangle':
                        writer.writerow([
                            obj.id,
                            obj.width,
                            obj.height,
                            obj.x,
                            obj.y
                            ])
                    elif cls.__name__ == 'Square':
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Return list of instances from CSV file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode='r', newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                objs = []
                for row in reader:
                    if cls.__name__ == 'Rectangle':
                        obj = cls(
                                int(row[1]),
                                int(row[2]),
                                int(row[3]),
                                int(row[4]),
                                int(row[0])
                                )

                    elif cls.__name__ == 'Square':
                        obj = cls(
                                int(row[1]),
                                int(row[2]),
                                int(row[3]),
                                int(row[0])
                                )
                    objs.append(obj)
                return objs
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares using Turtle graphics"""
        turtle.speed(0)
        turtle.delay(0)
        for rectangle in list_rectangles:
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.pendown()
            for _ in range(2):
                turtle.forward(rectangle.width)
                turtle.left(90)
                turtle.forward(rectangle.height)
                turtle.left(90)
        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.left(90)
        turtle.done()
