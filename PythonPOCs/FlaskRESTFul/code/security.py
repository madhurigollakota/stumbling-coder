# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 12:15:48 2021

@author: Madhuri
"""
from werkzeug.security import safe_str_cmp
from user import User

users= [User(1,'Jin','BTS'),
        User(2,'V','BTS'),
        User(3,'Jungkook','BTS'),
        User(4,'Harry','1D'),
        User(5,'Louis','1D'),
        User(6,'ChrisMartin','Coldplay')]

user_id_mapping= {u.id:u for u in users }

username_mapping = {u.username:u for u in users}

def authenticate(username,password):
    user=username_mapping.get(username,None)
    if user and safe_str_cmp(user.password,password):
        return user
    
def identity(payload):
    user_id=payload['identity']
    return user_id_mapping.get(user_id,None)