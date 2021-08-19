# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 17:26:19 2021

@author: Madhuri
"""
import sqlite3

class ItemModel:
    def __init__(self,name,price):
        self.name=name
        self.price=price
        
    def json(self):
        return {"name":self.name,"price":self.price}
        
    
    def get_item(self,name):
        conn=sqlite3.connect('data.db')
        cursor=conn.cursor()
        
        query="select * from items where name=?"
        result=cursor.execute(query,(name,))
        row=result.fetchone()
        conn.close()
        
        if row:
            return ItemModel(*row)
    

    def insert(self):
        conn=sqlite3.connect('data.db')
        cursor=conn.cursor()
        
        query="insert into items values(?,?)"
        cursor.execute(query,(self.name,self.price))
        conn.commit()
        conn.close()
        

    def update(self):
        conn=sqlite3.connect('data.db')
        cursor=conn.cursor()
        
        query="update items set price=? where name=?"
        cursor.execute(query,(price,name))
        conn.commit()
        conn.close()