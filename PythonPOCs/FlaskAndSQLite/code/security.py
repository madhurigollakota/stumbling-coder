# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 12:15:48 2021

@author: Madhuri
"""
from werkzeug.security import safe_str_cmp
from user import User


def authenticate(username,password):
    user=User.get_by_username(username)
    if user and safe_str_cmp(user.password,password):
        return user
    
def identity(payload):
    user_id=payload['identity']
    return User.get_by_userid(user_id)