#!/usr/bin/python3
"""Test Square"""

import unittest
import io
from models.base import Base
from models.square import Square
from random import randrange
from contextlib import redirect_stdout


class TestSquare(unittest.TestCase):
    """Tests the Square class"""

    def setUp(self):
        """instantiate class"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clears everything after each test method"""
        pass

    def test_class(self):
        """test square type"""
        self.assertEqual(str(Square), "<class 'models.square.Square'>")

    # ------------------- Test 1: inheritance -------------------
    def test_inheritance(self):
        """test if Square inherits Base"""
        self.assertTrue(issubclass(Square, Base))

    # ------------------ Test 2: __init__ func ------------------
    def test_no_args(self):
        """test __init__ witout arguments"""
        with self.assertRaises(TypeError) as e:
            r = Square()
        err = "__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(e.exception), err)

    def test_many_args(self):
        """test __init__ with many arguments"""
        with self.assertRaises(TypeError) as e:
            r = Square(1, 2, 3, 4, 5, 6)
        err = "__init__() takes from 2 to 5 positional arguments but \
7 were given"
        self.assertEqual(str(e.exception), err)

    def test_instantiation(self):
        """test instantiation"""
        r = Square(1)
        self.assertEqual(str(type(r)), "<class 'models.square.Square'>")
        self.assertTrue(isinstance(r, Base))
        d = {'_Rectangle__width': 1, '_Rectangle__height': 1,
             '_Rectangle__x': 0, '_Rectangle__y': 0}
        r_dict = r.__dict__
        self.assertTrue(isinstance(r_dict.pop('id'), int))
        self.assertDictEqual(r_dict, d)

        # testing the errors (validate_integer)
        with self.assertRaises(TypeError) as e:
            r = Square('1')
        err = "width must be an integer"
        self.assertEqual(str(e.exception), err)

        with self.assertRaises(TypeError) as e:
            r = Square(1, '2')
        err = "x must be an integer"
        self.assertEqual(str(e.exception), err)

        with self.assertRaises(TypeError) as e:
            r = Square(1, 2, '3')
        err = "y must be an integer"
        self.assertEqual(str(e.exception), err)

        with self.assertRaises(ValueError) as e:
            r = Square(0)
        err = "width must be > 0"
        self.assertEqual(str(e.exception), err)

        with self.assertRaises(ValueError) as e:
            r = Square(-1)
        err = "width must be > 0"
        self.assertEqual(str(e.exception), err)

        with self.assertRaises(ValueError) as e:
            r = Square(1, -2)
        err = "x must be >= 0"
        self.assertEqual(str(e.exception), err)

        with self.assertRaises(ValueError) as e:
            r = Square(1, 2, -3)
        err = "y must be >= 0"
        self.assertEqual(str(e.exception), err)

    def test_instantiation_keyword(self):
        """test instantiation with keywords"""
        r = Square(1, y=4, x=5)
        d = {'_Rectangle__width': 1, '_Rectangle__height': 1,
             '_Rectangle__x': 5, '_Rectangle__y': 4, '_Rectangle__id': 1}

    def test_properties(self):
        """test setters and getters"""
        r = Square(10, 20)
        r.size = 1
        r.x = 3
        r.y = 4
        d = {'_Rectangle__width': 1, '_Rectangle__height': 1,
             '_Rectangle__x': 3, '_Rectangle__y': 4}
        r_dict = r.__dict__
        self.assertTrue(isinstance(r_dict.pop('id'), int))
        self.assertEqual(r_dict, d)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
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
        r = Square(1, 2)
        attrs = ['x', 'y']
        for attr in attrs:
            err = "{} must be an integer".format(attr)
            for invalid in self.invalid_types():
                with self.assertRaises(TypeError) as e:
                    setattr(r, attr, invalid)
                self.assertEqual(str(e.exception), err)
            err = 'width must be an integer'
            for invalid in self.invalid_types():
                with self.assertRaises(TypeError) as e:
                    setattr(r, 'width', invalid)
                self.assertEqual(str(e.exception), err)

    def test_negative_w_h(self):
        """test validate_integer"""
        r = Square(1, 2)
        attrs = ['size']
        for attr in attrs:
            err = "width must be > 0"
            with self.assertRaises(ValueError) as e:
                setattr(r, attr, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), err)

    def test_negative_x_y(self):
        """test validate_integer"""
        r = Square(1, 2)
        attrs = ['x', 'y']
        for attr in attrs:
            err = "{} must be >= 0".format(attr)
            with self.assertRaises(ValueError) as e:
                setattr(r, attr, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), err)

    def test_zero(self):
        """test validate_integer"""
        r = Square(1, 2)
        attrs = ['size']
        for attr in attrs:
            err = "width must be > 0"
            with self.assertRaises(ValueError) as e:
                setattr(r, attr, 0)
            self.assertEqual(str(e.exception), err)

    # ------------------ Test 4: property ------------------
    def test_property(self):
        """test setters and getters"""
        r = Square(1, 2)
        attrs = ['width', 'height', 'x', 'y']
        for attr in attrs:
            n = randrange(10) + 1
            setattr(r, attr, n)
            self.assertEqual(getattr(r, attr), n)

    def test_property_zeros(self):
        """test setters and getters"""
        r = Square(1, 2)
        r.x = 0
        r.y = 0
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    # ----------------- Test 5: area method -----------------
    def test_area_no_args(self):
        """test area with no arguments"""
        r = Square(1, 2)
        with self.assertRaises(TypeError) as e:
            Square.area()
        err = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), err)

    def test_area_normal(self):
        """test area with radom numbers"""
        r = Square(2)
        self.assertEqual(r.area(), 4)
        w = randrange(10) + 1
        r.size = w
        self.assertEqual(r.area(), w * w)
        w = randrange(10) + 1
        r.size = w
        self.assertEqual(r.area(), w * w)
        r = Square(w, y=3, x=4)
        self.assertEqual(r.area(), w * w)
        Base._Base__nb_objects = 0
        r0 = Square(10)
        self.assertEqual(str(r0), '[Square] (1) 0/0 - 10')
        self.assertEqual(r0.size, 10)
        r0.size = 20
        self.assertEqual(r0.size, 20)

        with self.assertRaises(TypeError) as e:
            r0.size = '0'
        self.assertEqual(str(e.exception), 'width must be an integer')

        with self.assertRaises(ValueError) as e:
            r0.size = 0
        self.assertEqual(str(e.exception), 'width must be > 0')

    # ----------------- Test 6: display method -----------------
    def test_display_no_args(self):
        """test display with no args"""
        r = Square(1)
        with self.assertRaises(TypeError) as e:
            Square.display()
        err = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), err)

    def test_display_normal(self):
        """test display with different rectangles"""
        r = Square(1)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = '#\n'
        self.assertEqual(f.getvalue(), s)

        r.size = 3
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = '###\n###\n###\n'
        self.assertEqual(f.getvalue(), s)

    def test_display_x_y(self):
        """test display with x, y in mind"""
        r = Square(2, 7, 8)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """







       ##
       ##
"""
        self.assertEqual(f.getvalue(), s)

        r = Square(1, 10, 10)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """









          #
"""
        self.assertEqual(f.getvalue(), s)

        r = Square(1, 10)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """          #
"""
        self.assertEqual(f.getvalue(), s)

        r = Square(1, 0, 10)
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
        r = Square(1, 2)
        with self.assertRaises(TypeError) as e:
            Square.__str__()
        err = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), err)

    def test_str(self):
        """test str"""
        r = Square(1, 2)
        s = '[Square] (1) 2/0 - 1'
        self.assertEqual(str(r), s)

        r = Square(1, 2, 3)
        s = '[Square] (2) 2/3 - 1'
        self.assertEqual(str(r), s)

        r = Square(1, 2, 3, 4)
        s = '[Square] (4) 2/3 - 1'
        self.assertEqual(str(r), s)

    # ----------------- Test 8: update method -----------------
    def test_update_no_args(self):
        """test update with no arguments"""
        r = Square(1, 2)
        with self.assertRaises(TypeError) as e:
            Square.update()
        err = "update() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), err)

    def test_update_normal(self):
        """test update with argument orders"""
        r = Square(1, 2)
        d = r.__dict__.copy()
        r.update(20)
        d['id'] = 20
        self.assertEqual(r.__dict__, d)

        r.update(20, 30)
        d['_Rectangle__width'] = 30
        d['_Rectangle__height'] = 30
        self.assertEqual(r.__dict__, d)

        r.update(20, 30, 40)
        d['_Rectangle__x'] = 40
        self.assertEqual(r.__dict__, d)

        r.update(20, 30, 40, 50)
        d['_Rectangle__y'] = 50
        self.assertEqual(r.__dict__, d)

    def test_update_errs(self):
        """test update with argument orders, errors"""
        r = Square(1, 2)
        d = r.__dict__.copy()

        r.update(10)
        d['id'] = 10
        self.assertEqual(r.__dict__, d)

        with self.assertRaises(ValueError) as e:
            r.update(10, -1)
        err = 'width must be > 0'
        self.assertEqual(str(e.exception), err)

        with self.assertRaises(ValueError) as e:
            r.update(10, 1, -1)
        err = 'x must be >= 0'
        self.assertEqual(str(e.exception), err)

        with self.assertRaises(ValueError) as e:
            r.update(10, 1, 2, -1)
        err = 'y must be >= 0'
        self.assertEqual(str(e.exception), err)

    def test_update_kwargs(self):
        """test update with kwargs"""
        r = Square(1, 2)
        d = r.__dict__.copy()

        r.update(id=10)
        d['id'] = 10
        self.assertEqual(r.__dict__, d)

        r.update(size=20)
        d['_Rectangle__width'] = 20
        d['_Rectangle__height'] = 20
        self.assertEqual(r.__dict__, d)

        r.update(x=10)
        d['_Rectangle__x'] = 10
        self.assertEqual(r.__dict__, d)

        r.update(y=10)
        d['_Rectangle__y'] = 10
        self.assertEqual(r.__dict__, d)

    def test_update_kwargs_2(self):
        """test update with kwargs"""
        r = Square(1, 2)
        d = r.__dict__.copy()

        r.update(size=5, id=10)
        d['_Rectangle__width'] = 5
        d['_Rectangle__height'] = 5
        d['id'] = 10
        self.assertEqual(r.__dict__, d)

        r.update(y=5, size=5, id=10)
        d['_Rectangle__y'] = 5
        self.assertEqual(r.__dict__, d)

        r.update(y=5, size=5, x=5, id=10)
        d['_Rectangle__x'] = 5
        self.assertEqual(r.__dict__, d)

    # ----------------- Test 9: to_dictionary -----------------
    def test_dictionary(self):
        """test to_dictionary instantiation"""
        with self.assertRaises(TypeError) as e:
            Square.to_dictionary()
        err = "to_dictionary() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), err)

        r = Square(1)
        d = {'x': 0, 'y': 0, 'size': 1, 'id': 1}
        self.assertEqual(r.to_dictionary(), d)

        r = Square(1, 2, 3, 4)
        d = {'x': 2, 'y': 3, 'size': 1, 'id': 4}
        self.assertEqual(r.to_dictionary(), d)

        r.x = 10
        r.y = 20
        r.size = 30
        d = {'x': 10, 'y': 20, 'size': 30, 'id': 4}

        r1 = Square(1, 2, 3)
        r1_dict = r1.to_dictionary()
        r2 = Square(10, 20)
        r2.update(**r1_dict)
        self.assertEqual(str(r1), str(r2))
        self.assertNotEqual(r1, r2)


if __name__ == "__main__":
    unittest.main()
