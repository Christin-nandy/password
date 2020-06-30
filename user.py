class User:
     """
    Class that generates new instances of users
    """
       

    user_list = [] # Empty user list

    def __init__(self,first_name,last_name,number,email):

   def test_save_user(self):
        """def test_save_user(self):
        """
        test_save_user test case to test if the user object is saved into
         the users array
        """
        self.new_user.save_user_details()  # saving the new user
        self.assertEqual(len(User.user_list), 1)

        test_save_user test case to test if the user object is saved into
         the user list
        """
        self.new_user.save_user_details()  # saving the new user
        self.assertEqual(len(User.user_list), 1)

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email

        def save_user(self):

        """
        saves the new user account
        """
        
         User.user_list.append(self)

         @classmethod
    def display_users(cls):

        """
        a method that crates and  returns the class users
        """

        return cls.users_list