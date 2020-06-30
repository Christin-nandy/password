class Credential:

     """
    Class that generates new instances of credentials
    """

    Credential_list = [] # Empty credential List

    def __init__(self,user_name,password):

        self.user_name = user_name
        self.password = password

    def save_credential(self):

        """
        saves the new credential account
        """
        
         Credential.credential_list.append(self)

    @classmethod
    def display_credential(cls):

        """
        a method that crates and returns the class credentials
        """

        return cls.credentials_list     
    


