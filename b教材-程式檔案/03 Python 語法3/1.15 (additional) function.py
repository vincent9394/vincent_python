#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 15:55:17 2018

@author: Benson
"""
    
# simple function
def doWork():            
    print( "doWork!" )        # 函數內的語句需以Tab或空格起始

doWork()                      # 輸出 "doWork!"




# function with single argument
def doWork(a):
    print( a )

doWork("T恤")        # 輸出 "T恤"
doWork("褲")         # 輸出 "褲"
doWork(5)            # 輸出 5




# function with multiple arguments
def doWork(a, b, c):
    print( a+b+c )

doWork(1, 2, 3)        # 輸出 6



# function which return value
def add(a, b):
    return a+b       # 返回 a+b 值

c = add(1, 2)        # c = 3




# calling other function in a function
def add(c, d):
    return c+d
    
def addAndPrint(a, b):
    print( add(a, b) )

addAndPrint(1, 2)        # 輸出 3




# local variable
def addAndPrint(a, b):
    c = a+b          # 定義區域變數 c 儲存 a+b 值，c的數值只在函數範圍內生效
    print(c)         # 輸出 c 值

c = 10               # 定義區域變數 c 儲存 10
addAndPrint(1, 2)    # 輸出 3 ，因為函數內有print(c)
print(c)             # 輸出 10 ，而不是 3，因為函數內的c在函數範圍名是無效



# example
def areaOfCircle(radius):
    area = 3.14*radius**2
    return area

def areaOfRectangle(length,width):
    area = length*width
    return area

def totalArea(length,width,radius):
    area = areaOfCircle(radius) + areaOfRectangle(length, width)
    print(area)
    return area

area = totalArea(3,2,1)






