# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 12:59:02 2021

@author: Madhuri
"""
import sqlite3
from flask_restful import Resource,reqparse
from models.user import UserModel

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
            
            if UserModel.get_by_username(post_data['username']):
                return 'User with that name already exists',400
            
            conn=sqlite3.connect('data.db')
            cursor=conn.cursor()
            
            query="INSERT INTO users values (NULL,?,?)"
            
            cursor.execute(query,(post_data['username'],post_data['password']))
            conn.commit()
            conn.close()
            
            return 'User registered successfully',201