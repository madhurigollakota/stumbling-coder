# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 20:34:45 2021

@author: Madhuri
"""

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate,identity
from user import UserRegister
from item import Item,Items

app=Flask(__name__)
app.secret_key='maddy'
api=Api(app)

jwt=JWT(app,authenticate,identity)

api.add_resource(Item,'/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(UserRegister,'/register')

app.run(port=7888,debug=True)