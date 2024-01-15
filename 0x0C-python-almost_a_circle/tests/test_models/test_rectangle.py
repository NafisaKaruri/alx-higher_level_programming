#!/usr/bin/python3
"""Test Rectangle"""

import unittest
import io
from models.base import Base
from models.rectangle import Rectangle
from random import randrange
from contextlib import redirect_stdout


class TestRectangle(unittest.TestCase):
    """Tests the Rectangle class"""

    def setUp(self):
        """instantiate class"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clears everything after each test method"""
        pass

    # ------------------- Test 1: inheritance -------------------
    def test_inheritance(self):
        """test if Rectangle inherits Base"""
        self.assertTrue(issubclass(Rectangle, Base))

    # ------------------ Test 2: __init__ func ------------------
    def test_no_args(self):
        """test __init__ witout arguments"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle()
        err = "__init__() missing 2 required positional arguments: 'width' \
and 'height'"
        self.assertEqual(str(e.exception), err)

    def test_one_arg(self):
        """test __init__ with one argument"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1)
        err = "__init__() missing 1 required positional argument: 'height'"
        self.assertEqual(str(e.exception), err)

    def test_many_args(self):
        """test __init__ with many arguments"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, 3, 4, 5, 6)
        err = "__init__() takes from 3 to 6 positional arguments but \
7 were given"
        self.assertEqual(str(e.exception), err)

    def test_instantiation(self):
        """test instantiation"""
        r = Rectangle(1, 2)
        self.assertEqual(str(type(r)), "<class 'models.rectangle.Rectangle'>")
        self.assertTrue(isinstance(r, Base))
        d = {'_Rectangle__width': 1, '_Rectangle__height': 2,
            '_Rectangle__x': 0, '_Rectangle__y': 0}
        r_dict = r.__dict__
        self.assertTrue(isinstance(r_dict.pop('id'), int))
        self.assertDictEqual(r_dict, d)

        # testing the errors (validate_integer)
        with self.assertRaises(TypeError) as e:
            r = Rectangle('1', 2)
        err = "width must be an integer"
        self.assertEqual(str(e.exception), err)

        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, '2')
        err = "height must be an integer"
        self.assertEqual(str(e.exception), err)

        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, '3')
        err = "x must be an integer"
        self.assertEqual(str(e.exception), err)

        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, 3, '4')
        err = "y must be an integer"
        self.assertEqual(str(e.exception), err)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(0, 2)
        err = "width must be > 0"
        self.assertEqual(str(e.exception), err)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(-1, 2)
        err = "width must be > 0"
        self.assertEqual(str(e.exception), err)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 0)
        err = "height must be > 0"
        self.assertEqual(str(e.exception), err)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, -2)
        err = "height must be > 0"
        self.assertEqual(str(e.exception), err)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, -3)
        err = "x must be >= 0"
        self.assertEqual(str(e.exception), err)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, 3, -4)
        err = "y must be >= 0"
        self.assertEqual(str(e.exception), err)

    def test_instantiation_keyword(self):
        """test instantiation with keywords"""
        r = Rectangle(1, 2, y=4, x=5)
        d = {'_Rectangle__width': 1, '_Rectangle__height': 2,
            '_Rectangle__x': 5, '_Rectangle__y': 4, '_Rectangle__id': 1}

    def test_properties(self):
        """test setters and getters"""
        r = Rectangle(10, 20)
        r.width = 1
        r.height = 2
        r.x = 3
        r.y = 4
        d = {'_Rectangle__width': 1, '_Rectangle__height': 2,
                '_Rectangle__x': 3, '_Rectangle__y': 4}
        r_dict = r.__dict__
        self.assertTrue(isinstance(r_dict.pop('id'), int))
        self.assertEqual(r_dict, d)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    # ------------------ Test 3: invalid types ------------------
    def invalid_types(self):
        """tuple of invalid types to test"""
        t = (1.2, -1.2, float('inf'), float('-inf'), True, False, 'hello',
                (1, 2), [1, 2], {1, 2}, {1: 2}, None)
        return t

    def test_invalid_types(self):
        """test validate_integer"""
        r = Rectangle(1, 2)
        attrs = ['width', 'height', 'x', 'y']
        for attr in attrs:
            err = "{} must be an integer".format(attr)
            for invalid in self.invalid_types():
                with self.assertRaises(TypeError) as e:
                    setattr(r, attr, invalid)
                self.assertEqual(str(e.exception), err)

    def test_negative_w_h(self):
        """test validate_integer"""
        r = Rectangle(1, 2)
        attrs = ['width', 'height']
        for attr in attrs:
            err = "{} must be > 0".format(attr)
            with self.assertRaises(ValueError) as e:
                setattr(r, attr, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), err)

    def test_negative_x_y(self):
        """test validate_integer"""
        r = Rectangle(1, 2)
        attrs = ['x', 'y']
        for attr in attrs:
            err = "{} must be >= 0".format(attr)
            with self.assertRaises(ValueError) as e:
                setattr(r, attr, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), err)

    def test_zero(self):
        """test validate_integer"""
        r = Rectangle(1, 2)
        attrs = ['width', 'height']
        for attr in attrs:
            err = "{} must be > 0".format(attr)
            with self.assertRaises(ValueError) as e:
                setattr(r, attr, 0)
            self.assertEqual(str(e.exception), err)

    # ------------------ Test 4: property ------------------
    def test_property(self):
        """test setters and getters"""
        r = Rectangle(1, 2)
        attrs = ['width', 'height', 'x', 'y']
        for attr in attrs:
            n = randrange(10) + 1
            setattr(r, attr, n)
            self.assertEqual(getattr(r, attr), n)

    def test_property_zeros(self):
        """test setters and getters"""
        r = Rectangle(1, 2)
        r.x = 0
        r.y = 0
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    # ----------------- Test 5: area method -----------------
    def test_area_no_args(self):
        """test area with no arguments"""
        r = Rectangle(1, 2)
        with self.assertRaises(TypeError) as e:
            Rectangle.area()
        err = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), err)

    def test_area_normal(self):
        """test area with radom numbers"""
        r = Rectangle(1, 2)
        self.assertEqual(r.area(), 2)
        w = randrange(10) + 1
        h = randrange(10) + 1
        r.width = w
        r.height = h
        self.assertEqual(r.area(), w * h)
        w = randrange(10) + 1
        h = randrange(10) + 1
        r.width = w
        r.height = h
        self.assertEqual(r.area(), w * h)
        r = Rectangle(w, h, y=3, x=4)
        self.assertEqual(r.area(), w * h)
        r0 = Rectangle(2, 10)
        self.assertEqual(r0.area(), 20)
        r1 = Rectangle(3, 10, 0, 0, 1)
        self.assertEqual(r1.area(), 30)

    # ----------------- Test 6: display method -----------------
    def test_display_no_args(self):
        """test display with no args"""
        r = Rectangle(1, 2)
        with self.assertRaises(TypeError) as e:
            Rectangle.display()
        err = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), err)

    def test_display_normal(self):
        """test display with different rectangles"""
        r = Rectangle(1, 1)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = '#\n'
        self.assertEqual(f.getvalue(), s)

        r.width = 3
        r.height = 5
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = '###\n###\n###\n###\n###\n'
        self.assertEqual(f.getvalue(), s)

        r = Rectangle(2, 3)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = '##\n##\n##\n'
        self.assertEqual(f.getvalue(), s)

    def test_display_x_y(self):
        """test display with x, y in mind"""
        r = Rectangle(2, 3, 7, 8)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """







       ##
       ##
       ##
"""
        self.assertEqual(f.getvalue(), s)

        r = Rectangle(1, 1, 10, 10)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """









          #
"""
        self.assertEqual(f.getvalue(), s)

        r = Rectangle(1, 1, 10)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """          #
"""
        self.assertEqual(f.getvalue(), s)

        r = Rectangle(1, 1, 0, 10)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """









#
"""
        self.assertEqual(f.getvalue(), s)

    # ----------------- Test 7: __str__ method -----------------
    def test_str_no_args(self):
        """test str with no args"""
        r = Rectangle(1, 2)
        with self.assertRaises(TypeError) as e:
            Rectangle.__str__()
        err = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), err)

    def test_str(self):
        """test str"""
        r = Rectangle(1, 2)
        s = '[Rectangle] (1) 0/0 - 1/2'
        self.assertEqual(str(r), s)

        r = Rectangle(1, 2, 3)
        s = '[Rectangle] (2) 3/0 - 1/2'
        self.assertEqual(str(r), s)

        r = Rectangle(1, 2, 3, 4)
        s = '[Rectangle] (3) 3/4 - 1/2'
        self.assertEqual(str(r), s)

        Base._Base__nb_objects = 0
        r1 = Rectangle(1, 2, 3, 4, 20)
        s = '[Rectangle] (20) 3/4 - 1/2'
        self.assertEqual(str(r1), s)

        r2 = Rectangle(1, 1, 1)
        s = '[Rectangle] (1) 1/0 - 1/1'
        self.assertEqual(str(r2), s)

if __name__ == "__main__":
    unittest.main()
