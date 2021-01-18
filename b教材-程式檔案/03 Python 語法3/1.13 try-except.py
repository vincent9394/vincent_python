#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 13:58:01 2018

@author: Benson
"""


# error example
amount = 10000                      # 總消費金額
numOfPeople = input("請輸入人數：")   # input() 永遠返回字串 string
numOfPeople = int(numOfPeople)      # 將 string 轉成 integer

print( "每人須付 $" + str(amount / numOfPeople) )
print( "繼續運行程式" )




# using if to avoid error
amount = 10000    # 總金額 10000
numOfPeople = int( input("請輸入人數：") )   # 如果用戶輸入非數字字母，程式到這句還是會出錯！
if numOfPeople > 0:
    print( "每人須付 $" + str(amount / numOfPeople) )
else:
    print( "人數必須為整數，且大於零！" )
    
print( "繼續運行程式" )   





# try-except method
try:
    amount = 10000
    numOfPeople = int( input("請輸入人數：") )
    amountPerPerson = amount / numOfPeople
    print( "每人須付 $" + str(amountPerPerson)  )
except:
    print( "人數必須為整數，且大於零！" )

print( "繼續運行程式" )




# get error message
try:
    1/0
except Exception as e:                 # 取得錯誤碼，儲存到變數 e
    print( "發生了錯誤：" + str(e) )     # 輸出錯誤碼



# nested try-except
try:
    try:
        1/0
    except:
        print("Caught by inner")

    print("Continue")
except:
    print("Caught by outer")




# exercise





