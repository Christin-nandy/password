#!/usr/bin/env python3.6

from user import User
from credential import Credential

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
    
               