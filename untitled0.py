# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 12:49:30 2024

@author: EMAN
"""
def function1(x):
    def function2(y):
        print (y + 2)  
        return y + 2
    return 3 * function2(x)
a = function1(2) 
b = function2(2.5) 

