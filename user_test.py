import unittest

from  user import User

class TestUser(unittest.TestCase):
    def setUp(self):

        """
        setter to set method
        """
 self.new_user = User("Christine", "Achieng", "0798401097", "achiengchristine14@gmail.com")

def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.first_name, "Christine")
        self.assertEqual(self.new_user.last_name, "Achieng")
        self.assertEqual(self.new_user.phone_number, "0798401097")
        self.assertEqual(self.new_user.email, "achiengchristine14@gmail.com")

def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """
        User.user_list = []  

def test_save_user(self):
        """
        test_save_user test case to test if the user object is saved into
         the user list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)
   
 
