#!/usr/bin/env python3.6

from user import User
from credential import Credential

import string

def create_user(first_name,last_name,phone ,email):
    '''
    Function to create a new contact
    '''
    new_user = User(first_name,last_name,phone,email)
    return new_user

def create_credential(user_name,password):
    '''
    Function to create a new contact
    '''
    new_credential = Credential(user_name,password)
    return new_credential
    
def save_users(user):
    '''
    Function to save user
    '''
    user.save_users()

def save_credentials(credential):
    '''
    Function to save credential
    '''
    credential.save_credentials()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user() 

def del_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()  

def check_existing_credentials(user_name,password):
    '''
    Function that check if a credential exists with that number and return a Boolean
    '''
    return Credential.credential_exist(user_name,password)

def add_credential(acc,user_name,password):
    """
    adds a credential
    """
    added_credential = Credential(acc, user_name,password)

    return added_credential

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credential.display_credentials()
def main():
    print("Hello,Welcome to PASSWORD LOCKER!")
    print('\n')

    while True:
        print("Use these short codes : cc - create a new user credential account, dc - display user credential account, fc -find a user credential account, ex -exit the user credential account list ")
        short_code = input().lower()
        if short_code == 'cc':
                            print("New Credential")
                            print("-"*10)

                            print ("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("Phone number ...")
                            p_number = input()

                            print("Email address ...")
                            e_address = input()

                            print("user name ...")
                            u_name = input()

                            print("password ...")
                            password = input()

                            save_credential(create_credential(u_name,password)) # create and save new credential.
                            print ('\n')
                            print(f"New Credential {u_name} {password} created")
                            print ('\n')

                            elif short_code == 'dc':

                            if display_credentials():
                                    print("The following are all your credentials")
                                    print('\n')

                                    for credential in display_credentials():
                                            print(f"{credential.user_name} {credential.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You don't an account please create a new one to log in !!")
                                    print('\n')

       