#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 11:26:23 2018

@author: Benson
"""

# define tuple
tuple1 = (1, 2, 5, 9, 12)				
tuple2 = ("apple", "orange", "kiwi")		
tuple3 = ("apple", 8, (1, 2, 3))			
tuple4 = ()								


# some other ways to define tuple
t1 = ("apple", )		
t2 = 1, 2, 3				
t3 = 1, 					
t4 = ()					


# getting tuple element by index
fruits = ("apple", "orange", "kiwi")  
fruits[0]		
fruits[1]		
fruits[2]
fruits[-1]
fruits[-2]
fruits[-3]


# getting tuple element by range
fruits[ : ]		
fruits[ : 3]	
fruits[ : : 2]	
fruits[2 : 4]


# length of the tuple
fruits = ("apple", "orange", "pear")
print( len(fruits) )


# check if an item is in the tuple
fruits = ("apple", "orange", "pear")
print( "orange" in fruits )      # 返回 True
print( "grape" in fruits )       # 返回 False


# finding the position index of the element
fruits = ("apple", "orange", "kiwi", "grape", "pear")
fruits.index("kiwi")


# exercises

