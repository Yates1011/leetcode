# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 10:49:44 2024

@author: william.yates
"""

def shift_list_left(lst, n):
    return lst[n:] + lst[:n]

students = [1,1,0,0]
sandwiches = [0,1,0,1]

# students = [1,1,1,0,0,1]

# sandwiches = [1,0,0,0,1,1]

# print(shift_list_left(students, 1))


tempS = students.copy()


def compare(students,sandwiches):
    tempS = 0 
    for idx, iStudent in enumerate(students):
        if iStudent == sandwiches[idx]:
            students.pop(idx)
            sandwiches.pop(idx)
        else:
            tempS = shift_list_left(students, 1)
    return students, sandwiches, tempS
            
            
a,b,c = compare(students, sandwiches)

            
d,e,f = compare(c,b)

    
        
