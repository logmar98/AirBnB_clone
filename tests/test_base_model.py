#!/usr/bin/python3
"""
A Unittest model for BaseModel class
"""
import unittest
from datetime import datetime
from ..models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    This class contains unit tests for the BaseModel class.
    """

    def test_init_with_arguments(self):
        """
        Test initialization of BaseModel with arguments.
        It should raise a TypeError.
        """
        with self.assertRaises(TypeError):
            BaseModel(None)

    def test_init_without_arguments(self):
        """
        Test initialization of BaseModel without arguments.
        It should return an instance of BaseModel.
        """
        self.assertIsInstance(BaseModel(), BaseModel)

    def test_str(self):
        """
        Test the string representation of BaseModel.
        It should match the expected string format.
        """
        obj = BaseModel(id='123')
        string = ("[{}] ({}) "
                  "{{'id': '{}',"
                  "'created_at': <datetime>, 'updated_at': <datetime>}}"
                  .format(obj.__class__.__name__, obj.id, obj.id))
        self.assertEqual(str(obj), string)

    def test_save(self):
        """
        Test the save method of BaseModel.
        It should update the 'updated_at' attribute.
        """
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, old_updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method of BaseModel.
        It should return a dictionary representation with all attributes.
        """
        model = BaseModel()
        model.city = "kassala"
        model.number = int(123)
        dict_obj = model.to_dict()
        expected_dict = {
            '__class__': 'BaseModel',
            'id': model.id,
            'created_at': dict_obj['created_at'],
            'updated_at': dict_obj['updated_at'],
            'city': 'kassala',
            'number': 123
        }
        self.assertEqual(dict_obj, expected_dict)
        self.assertIsInstance(dict_obj["created_at"], str)
        self.assertIsInstance(dict_obj["updated_at"], str)
        self.assertIsInstance(dict_obj["number"], int)
        self.assertEqual(dict_obj["number"], 123)
        self.assertEqual(dict_obj["city"], "kassala")


if __name__ == '__main__':
    unittest.main()
