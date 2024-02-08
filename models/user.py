#!/usr/bin/python 3
'''
class User that inherits from BaseModel
'''
from models.base_model import BaseModel


class User(BaseModel):
    '''
    class User that handles users' information
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
