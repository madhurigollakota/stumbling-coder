# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 10:24:32 2021

@author: Madhuri
"""

import sqlite3

conn=sqlite3.connect('data.db')
cursor=conn.cursor()

user_table="CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,username text,password text)"

cursor.execute(user_table)

item_table="CREATE TABLE IF NOT EXISTS items(name text PRIMARY KEY,price real)"

cursor.execute(item_table)

conn.commit()
conn.close()