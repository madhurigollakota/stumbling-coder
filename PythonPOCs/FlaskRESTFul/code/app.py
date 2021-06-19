# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 20:34:45 2021

@author: Madhuri
"""

from flask import Flask,request
from flask_restful import Resource,Api,reqparse
from flask_jwt import JWT,jwt_required

from security import authenticate,identity


app=Flask(__name__)
app.secret_key='maddy'
api=Api(app)

jwt=JWT(app,authenticate,identity)

items=[]


class Item(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('price',
                            required=True,
                            type=float,
                            help='This argument is madatory')
    
    def get(self,name):
        item=next(filter(lambda x: x['name']==name,items),None)
        return {'item':item}, 200 if item else 404
    
    @jwt_required()
    def post(self,name):
        
        if next(filter(lambda x: x['name']==name,items),None):
            return 'Item with name {} already exists'.format(name),400
        
        post_data=Item.parser.parse_args()        
        item={'name':name,'price':post_data['price']}
        items.append(item)
        return item, 201
    
    @jwt_required()
    def delete(self,name):
        global items
        new_items=list(filter(lambda x: x['name']!=name,items))
        items=new_items
        return items,200
    
    def put(self,name):
        
        put_data=Item.parser.parse_args()
        item=next(filter(lambda x:x['name']==name,items),None)
        if item:
            item.update(put_data)
            return {'item':item}, 202
        
        new_item={'name':name,'price':put_data['price']}
        items.append(new_item) 
        return {'item':new_item},201
    
api.add_resource(Item,'/item/<string:name>')

class Items(Resource):
    def get(self):
        return {'items':items}

api.add_resource(Items, '/items')

app.run(port=7888,debug=True)