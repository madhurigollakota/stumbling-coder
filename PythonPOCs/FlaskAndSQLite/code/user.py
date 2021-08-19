# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 12:19:26 2021

@author: Madhuri
"""
import sqlite3

from flask_restful import Resource,reqparse

class User:
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
        
class UserRegister(Resource):
        
        parser=reqparse.RequestParser()
        parser.add_argument('username',
                            type=str,
                            required=True,
                            help="This is a mandatory field")
        parser.add_argument('password',
                            type=str,
                            required=True,
                            help="This is a mandatory field")
        
        def post(self):
            
            post_data=self.parser.parse_args()
            
            if User.get_by_username(post_data['username']):
                return 'User with that name already exists',400
            
            conn=sqlite3.connect('data.db')
            cursor=conn.cursor()
            
            query="INSERT INTO users values (NULL,?,?)"
            
            cursor.execute(query,(post_data['username'],post_data['password']))
            conn.commit()
            conn.close()
            
            return 'User registered successfully',201
            
            
            
            
            
            