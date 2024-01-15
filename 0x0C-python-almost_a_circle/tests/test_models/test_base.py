#!/usr/bin/python3
"""Test Base"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


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
