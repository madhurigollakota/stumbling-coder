# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 18:49:01 2021

@author: Madhuri
"""

if __name__ == '__main__':
    students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.insert(_,[name,score])