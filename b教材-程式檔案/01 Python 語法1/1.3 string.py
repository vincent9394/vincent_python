#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 15:38:57 2018

@author: Benson
"""

# string
s = "This is a string"
s = "這是字串"
s = '12345'
s = 'Peter1，你好嗎?'
s = ""




# getting one character of the string
s = "Hello world"
s[0]        # "H"
s[5]        # " "
s[6]        # "w"
s[-1]       # "d"
s[-2]       # "l"


# getting part of the string
s = "Hello world"
s[ 0 : 5 ]      # "Hello"    
s[ : 5 ]        # "Hello"
s[ 0 : 5 : 2 ]  # "Hlo"
s[ : : 2 ]      # "Hlowrd"
    

s[ -2 : ]      # "ld"
s[ : -6 ]      # "Hello"
s[ -11 : 2 ]   # "He"
s[ : : -1 ]    # "dlrow olleH"
s[ 1 : 2 ]     # "e"



# changing number to string
num = str(10000)




# escape character \"
# this is wrong
# s = "I bought "Python Cookbook", it's great!"     


# these are correct!  
s = 'I bought "Python Cookbook", it\'s great!'
print(s)
s = "I bought \"Python Cookbook\", it's great!"
print(s)
s = "I bought \"Python Cookbook\", it\'s great!" 
print(s)

# escape character \n - new line
print("1st line\r\n2nd line")

# escape character \\ - slash
print("slash\\")

# escape character \t - tab  
print("1\t2\t3")


# raw string
print( 'C:\\Users\\User\\Desktop' )
print( r'C:\Users\User\Desktop' )



# excercise





