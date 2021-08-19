# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 12:19:26 2021

@author: Madhuri
"""
import sqlite3

class UserModel:
    def __init__(self,_id,username,password):
        self.id=_id
        self.username=username
        self.password=password
    
    @classmethod
    def get_by_username(cls,username):
        
        conn= sqlite3.connect('data.db')
        cursor = conn.cursor()
        
        query="SELECT * from users where username=?"
        
        result=cursor.execute(query,(username,))
        row=result.fetchone()
        
        if row:
            user= cls(*row)
        
        else:
            user=None
        
        conn.close()
        return user
        
    @classmethod
    def get_by_userid(cls,_id):
        
        conn= sqlite3.connect('data.db')
        cursor = conn.cursor()
        
        query="SELECT * from users where id=?"
        
        result=cursor.execute(query,(_id,))
        row=result.fetchone()
        
        if row:
            user= cls(*row)
        
        else:
            user=None
        
        conn.close()
        return user
        
