# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 23:12:24 2021

@author: Madhuri
"""

if __name__=='__main__':
    n=int(input())
    student_scores={}
    for i in range(n):
        student_name,*l=input().split(' ')
        scores=list(map(float,l))
        student_scores[student_name]=scores
    query_name = input()
    print(format(sum(student_scores[query_name])/len(student_scores[query_name]),'.2f'))