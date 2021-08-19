# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 10:30:49 2021

@author: Madhuri
"""
import sqlite3
from flask_jwt import jwt_required
from flask_restful import reqparse,Resource
from models.item import ItemModel


class Item(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('price',
                            required=True,
                            type=float,
                            help='This argument is madatory')
           
    def get(self,name):
        item=ItemModel.get_item(name)
        
        if item:
            return {'name':item[0],'price':item[1]}, 200
        return 'Item doesnt exist' ,404
    
    @jwt_required()
    def post(self,name):
        
        if ItemModel.get_item(name):
            return 'Item with name {} already exists'.format(name),400
        
        post_data=Item.parser.parse_args() 
        ItemModel.insert(name,post_data['price'])
        item={'name':name,'price':post_data['price']}
        return item, 201
    
    @jwt_required()
    def delete(self,name):
        
        if self.get_item(name):
            conn=sqlite3.connect('data.db')
            cursor=conn.cursor()
        
            query="delete from items where name=?"
            cursor.execute(query,(name,))
            conn.commit()
            conn.close()
            
            return 'Item deleted',200
        return 'Item doesnt exist',400
    
    def put(self,name):
        
        put_data=Item.parser.parse_args()
        updated_item={'name':name,'price':put_data['price']}
        if ItemModel.get_item(name):
            ItemModel.update(name,put_data['price'])
            return {'item':updated_item}, 202
        else:
            ItemModel.insert(name,put_data['price'])
            return {'item':updated_item},201


class Items(Resource):
    def get(self):
        conn=sqlite3.connect('data.db')
        cursor=conn.cursor()
        
        query="select * from items"
        result=cursor.execute(query)
        
        items=[]
        
        for row in result:
            items.append({'name':row[0],'price':row[1]})
        conn.close()
        return {'items':items}
