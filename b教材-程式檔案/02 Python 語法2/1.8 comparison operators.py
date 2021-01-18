#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 18:21:00 2018

@author: Benson
"""

# comparison operator



# bigger than, bigger or equal to
price = 20
print( price > 10 )		# 輸出 True
print( price >= 20 )		# 輸出 True



# smaller than, smaller or equal to
price = 20
print( price < 10 )		# 輸出 False
print( price <= 20 )		# 輸出 True



# equal to, not equal to
print( 2 != 1 )                    # 輸出 True
print( 1 == 1 )                    # 輸出 True
print( False == False )            # 輸出 True
print( "abc" == "abc" )            # 輸出 True



# real life application
stock = "00001.hk"
print( stock == "00001.hk" )			# 輸出 True
print( stock[ 0 : 5 ] == "00001" )		# 輸出 True
print( stock.startswith("00001") )		# 輸出 True
print( stock[ -3 :  ] == ".hk" )		# 輸出 True
print( stock.endswith(".hk") )			# 輸出 True



# exercise
