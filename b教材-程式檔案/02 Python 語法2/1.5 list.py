#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 11:01:33 2018

@author: Benson
"""


# list examples
numList = [1, 2, 5, 9, 12]                  # 整數 list
stringList = ["apple", "orange", "kiwi"]    # 字串 list
mixList 	= ["apple", 8, [1, 2, 3]]       # 混合 list
emptyList = []                              # 空 list



# get the elements by index
fruits = ["apple", "orange", "kiwi"]
fruits[0]					
fruits[1]						
fruits[2]					
fruits[-1]
fruits[-2]
fruits[-3]



# change the element value
fruits = ["apple", "orange", "kiwi"]
fruits[1] = "grape"



# get the elements by range
fruits = ["apple", "orange", "kiwi", "grape", "pear"]
fruits[ : ]		
fruits[ : 3 ]	
fruits[ : : 2 ]	
fruits[ 2 : 4 ]	


# list addition
["apple", "orange", "kiwi"] + ["grape", "strawberry"]


# list multiplication
["apple", "orange"] * 2



# length of the list
fruits = ["apple", "orange", "pear"]
print( len(fruits) )



# check if an item is in the list
fruits = ["apple", "orange", "pear"]
print( "orange" in fruits )      # 返回 True
print( "grape" in fruits )       # 返回 False



# append
fruits = ["apple", "orange"]
fruits.append("pear")




# removing an element
fruits = ["apple", "orange", "grape", "kiwi"]
del fruits[-1]     # 移除最後面元素
del fruits[0]      # 移除元素 0
del fruits[1]      # 移除元素 1



# removing a range of elements
fruits = ["apple", "orange", "grape", "kiwi"]
del fruits[1: 3]     # 移除元素 1, 2
del fruits[ : ]      # 移除所有元素






################   選讀部份   ################


# insert the element at a specified position
fruits = ["orange", "kiwi"]
fruits.insert(1, "grape")

fruits = ["orange", "kiwi"]
fruits.insert(0, "apple")



# insert the element at the end of the list
fruits = ["orange", "kiwi"]
fruits.insert(len(fruits), "pear")



# removing the element by specifying the value
fruits = ["apple", "orange", "kiwi"]
fruits.remove("orange")



# searching the index of an element
fruits = ["apple", "orange", "kiwi", "grape", "pear"]
fruits.index("kiwi")



# exercises





