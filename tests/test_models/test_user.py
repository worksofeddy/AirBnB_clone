#!/usr/bin/python3
'''
unittest cases for the class User
'''
import os
import models
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    '''
    Tests the User Class
    '''
    def setUp(self):
        # Creates a temporary test file for saving data
        self.test_file = "test_file.json"
        models.storage.__file_path = self.test_file
        models.storage.save()

    def tearDown(self):
        # Remove the test file created during testing
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_attributes_initialization(self):
        # Creates a new user instance
        test_user = User()
        # Checks if the attributes are empty strings
        self.assertEqual(test_user.email, "")
        self.assertEqual(test_user.password, "")
        self.assertEqual(test_user.first_name, "")
        self.assertEqual(test_user.last_name, "")

    def test_user_inheriting_from_base_model(self):
        test_user = User()
        # Checking if the user is a subclass of basemodel
        self.assertTrue(issubclass(User, BaseModel))

    def test_attributes_assignment(self):
        test_user = User()
        # Sets the attributes of the User Instance"
        test_user.email = "Johnnie@example.com"
        test_user.password = "password123"
        test_user.first_name = "Johnnie"
        test_user.last_name = "Done"
        # Get the string representation of the user instance
        user_str = str(test_user)
        # Check if the attributes is present in the string representation
        self.assertIn("User", user_str)
        self.assertIn("Johnnie@example.com", user_str)
        self.assertIn("Johnnie", user_str)
        self.assertIn("Done", user_str)

    def test_user_to_dict_method(self):
        test_user = User()
        # Sets the attributes of the User Instance"
        test_user.email = "Johnnie@example.com"
        test_user.first_name = "Johnnie"
        test_user.last_name = "Done"
        test_user.save()
        # Dictionary representation of the user instance
        user_dict = test_user.to_dict()
        # Check if the keys match the set value
        self.assertEqual(user_dict['email'], "Johnnie@example.com")
        self.assertEqual(user_dict['first_name'], "Johnnie")
        self.assertEqual(user_dict['last_name'], "Done")

    def test_user_instance_creation(self):
        # Creates a new user with arguments
        test_user = User(email="Johnnie@example.com", password="password123",
                    first_name="Johnnie", last_name="Done")
        # Check if the attributes are set correctly
        self.assertEqual(test_user.email, "Johnnie@example.com")
        self.assertEqual(test_user.password, "password123")
        self.assertEqual(test_user.first_name, "Johnnie")
        self.assertEqual(test_user.last_name, "Done")

    def test_user_instance_to_dict(self):
        # Creates a new user with arguments
        test_user = User(email="Johnnie@example.com", password="password123",
                    first_name="Johnnie", last_name="Done")
        # Converts the user instance to a dictionary
        user_dict = test_user.to_dict()
        # Check if the attributes are set correctly
        self.assertEqual(user_dict['email'], "Johnnie@example.com")
        self.assertEqual(user_dict['password'], "password123")
        self.assertEqual(user_dict['first_name'], "Johnnie")
        self.assertEqual(user_dict['last_name'], "Done")

    def test_user_id_generation(self):
        # Create two users
        test_user = User()
        user2 = User()
        # Ensure that the ids are unique
        self.assertNotEqual(test_user.id, user2.id)


if __name__ == '__main__':
    unittest.main()
