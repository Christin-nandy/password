 import unittest
 from  credential import Credential

class TestUser(unittest.TestCase):
    def setUp(self):

        """
        setter to set method before run
        """ 

    self.new_user = User("user_name", "password")
    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.user_name, "user_name")
        self.assertEqual(self.new_user.password, "password")

        def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """
        User.credential_list = []

        def test_save_credential(self):
        """
        test_save_credential test case to test if the user object is saved into
         the credential list
        """
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 1)
     
    


  