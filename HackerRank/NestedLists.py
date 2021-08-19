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
        students.append([name,score])
    
    print(*sorted([item[0] for item in students if item[1]==sorted(set([m for l,m in students]))[1]]),sep='\n')