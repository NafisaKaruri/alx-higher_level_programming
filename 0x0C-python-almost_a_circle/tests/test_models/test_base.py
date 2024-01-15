#!/usr/bin/python3
"""Test Base"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """tests the base class"""
    def setUp(self):
        """instantiation"""
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """clear everything each test case"""
        pass

    def test_nb_objects_private(self):
        """checks if nb is private"""
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_nb_objects_initialize(self):
        """checks if nb starts from 0"""
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_instantiation(self):
        """test istantiation"""
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {'id': 1})
        self.assertEqual(b.id, 1)

    def test_init_no_args(self):
        """test the init method with no args"""
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        err = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), err)

    def test_init_many_args(self):
        """test the init method with extra args"""
        with self.assertRaises(TypeError) as e:
            Base.__init__(self, 1, 2)
        err = "__init__() takes from 1 to 2 positional arguments but 3 \
               were given"

    def test_ids(self):
        """test ids"""
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_ids_2(self):
        """test ids cont"""
        b = Base()
        b = Base('hello')
        b = Base(1)
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_id_int(self):
        """test id as int"""
        b = Base(100)
        self.assertEqual(b.id, 100)

    def test_id_string(self):
        """test id as string"""
        b = Base('hehe')
        self.assertEqual(b.id, 'hehe')

    def test_id_keyword(self):
        """test id with keyword"""
        b = Base(id=100)
        self.assertEqual(b.id, 100)

    def test_to_json_string(self):
        """test to_json_string method"""
        with self.assertRaises(TypeError) as e:
            Base.to_json_string()
        err = "to_json_string() missing 1 required positional argument: \
'list_dictionaries'"
        self.assertEqual(str(e.exception), err)

        self.assertEqual(Base.to_json_string(None), '[]')
        self.assertEqual(Base.to_json_string([]), '[]')

        d = [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]
        self.assertEqual(len(Base.to_json_string(d)), len(str(d)))

        d = [{"hello": 1}]
        self.assertEqual(Base.to_json_string(d), '[{"hello": 1}]')

        d = [{"hello": 1}, {"world": 2}]
        self.assertEqual(Base.to_json_string(d),
                         '[{"hello": 1}, {"world": 2}]')

        d = [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8},
             {"x": 25, "width": 13, "id": 10, "height": 347, "y": 34}]
        self.assertEqual(len(Base.to_json_string(d)), len(str(d)))

        d = [{}, {}]
        self.assertEqual(Base.to_json_string(d), '[{}, {}]')

        r = Rectangle(1, 2, 3, 4)
        d = r.to_dictionary()
        json_d = Base.to_json_string([d])
        d = str([d])
        self.assertEqual(d.replace("'", '"'), json_d)

        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(5, 6, 7, 8)
        d = [r1.to_dictionary(), r2.to_dictionary()]
        json_d = Base.to_json_string([d])
        d = str([d])
        self.assertEqual(d.replace("'", '"'), json_d)

        r = Square(1, 2, 3)
        d = r.to_dictionary()
        json_d = Base.to_json_string([d])
        d = str([d])
        self.assertEqual(d.replace("'", '"'), json_d)

        r1 = Square(1, 2, 3)
        r2 = Square(4, 5, 6)
        d = [r1.to_dictionary(), r2.to_dictionary()]
        json_d = Base.to_json_string([d])
        d = str([d])
        self.assertEqual(d.replace("'", '"'), json_d)

    def test_save_to_file(self):
        """test save_to_file"""
        import os
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(5, 6)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(len(f.read()), 104)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(f.read(), "[]")

        try:
            os.remove("Rectangle.json")
        except:
            pass
        Rectangle.save_to_file([])
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(f.read(), "[]")

        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(len(f.read()), 52)

        Square.save_to_file(None)
        with open("Square.json", 'r') as f:
            self.assertEqual(f.read(), "[]")

        try:
            os.remove("Square.json")
        except:
            pass
        Square.save_to_file([])
        with open("Square.json", 'r') as f:
            self.assertEqual(f.read(), "[]")

        r = Square(1)
        Square.save_to_file([r])
        with open("Square.json", 'r') as f:
            self.assertEqual(len(f.read()), 38)

    def test_from_json(self):
        """test from_json_string"""
        with self.assertRaises(TypeError) as e:
            Base.from_json_string()
        err = "from_json_string() missing 1 required positional argument\
: 'json_string'"
        self.assertEqual(str(e.exception), err)
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(''), [])

        d = [{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5},
             {"x": 10, "y": 20, "width": 30, "id": 40, "height": 50}]
        s = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5},\
{"x": 10, "y": 20, "width": 30, "id": 40, "height": 50}]'
        self.assertEqual(Base.from_json_string(s), d)

        d = [{}, {}]
        s = '[{}, {}]'
        self.assertEqual(Base.from_json_string(s), d)

        d = [{}]
        s = '[{}]'
        self.assertEqual(Base.from_json_string(s), d)

        d = [{"eh": 1}]
        s = '[{"eh": 1}]'
        self.assertEqual(Base.from_json_string(s), d)

    def test_create(self):
        """test create"""
        r = Rectangle(1, 2, 3)
        d = r.to_dictionary()
        r1 = Rectangle.create(**d)
        self.assertEqual(str(r), str(r1))
        self.assertFalse(r == r1)
        self.assertFalse(r is r1)

    def test_load_from_file(self):
        """test load_from_file"""
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(5, 6)
        f = [r1, r2]
        Rectangle.save_to_file(f)
        output = Rectangle.load_from_file()
        self.assertNotEqual(id(f[0]), id(output[0]))
        self.assertNotEqual(id(f[1]), id(output[1]))
        self.assertEqual(str(f[0]), str(output[0]))
        self.assertEqual(str(f[1]), str(output[1]))

        r1 = Square(1)
        r2 = Square(2, 3, 4)
        f = [r1, r2]
        Square.save_to_file(f)
        output = Square.load_from_file()
        self.assertNotEqual(id(f[0]), id(output[0]))
        self.assertNotEqual(id(f[1]), id(output[1]))
        self.assertEqual(str(f[0]), str(output[0]))
        self.assertEqual(str(f[1]), str(output[1]))


if __name__ == "__main__":
    unittest.main()
