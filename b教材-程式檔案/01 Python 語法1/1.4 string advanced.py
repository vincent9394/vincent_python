#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 17:33:04 2018

@author: Benson
"""

# string concatenation

s = "hello " + "world" + "!"       # s = "hello world!"
s = "1 + 1 = " + str(2)            # s = "1 + 1 = 2"


# string multiplication

s = "abc" * 3       # s = "abcabcabc"


# formatting string %s

s = "Numbers " + str(10) + ", " + str(20)      # 輸出 "Numbers 10, 20"
s = "Numbers %s, %s" % (10, 20)



# getting the length of string
print( len( "a string" ) )        
print( len( "字串長度" ) )



# find inside a string - in 
print( "kong" in "hello kong" )            # 輸出 True
print( "benson" in "hello kong" )          # 輸出 False



# replace()
print( "hello world".replace("world", "kong") )      # 輸出 "hello kong"
print( "hello world".replace("benson", "kong") )     # 輸出 "hello world"
print( "a b c".replace(" ", "") )                    # 輸出 "abc"



# split()
print( "a,b,c".split(",") )                 # 輸出 [ "a", "b", "c" ]
print( "line 1\nline 2".split("\n") )       # 輸出 [ "line 1", "line 2" ]
print( "line 1\nline 2\n".split("\n") )     # 輸出 [ "line 1", "line 2", "" ]



# startswith(), endswith()
print( "00001.hk".startswith("00001") )     # True
print( "00001.hk".endswith(".hk") )         # True



# strip()
print( "  a b c    ".strip() )              # 輸出 "a b c"
print( "  a b c    \n\t  ".strip() )        # 輸出 "a b c"
print( "%abc%%%".strip("%") )               # 輸出 "abc"





# exercise










