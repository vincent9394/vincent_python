#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 13:58:01 2018

@author: Benson
"""


# 捕捉某個種類的例外，根據不同的例外類型，做不同的錯誤處理動作。
try:
    1/0
    1+"a"
    b
except ZeroDivisionError as e:  # 只捕捉 ZeroDivisionError
    print( "ZeroDivisionError")
except TypeError as e:          # 只捕捉 TypeError
    print( “Type Error” )
except Exception as e:          # 捕捉所有 Exception
    print( “Exception” )

    
    
# exception names
1/0       # 輸出 "ZeroDivisionError: division by zero"
1 + "a"   # 輸出 "TypeError: unsupported operand type(s) for +: 'int' and 'str'"
b         # 輸出 "NameError: name 'b' is not defined"



# try-except-else-finally
try:
    print( "計算中" )
    1/0
except:
    print( "計算失敗" )      # 如發生錯誤，這裡會被執行
else:
    print( "計算成功" )      # 如沒有發生錯誤，這裡會被執行
finally:
    print( "程式繼續")       # 不論有無錯誤，這裡都會被執行

    

# manually raise exception
try:
    num = input("輸入數字:")
    num = int(num)
    if num > 2:
        raise Exception("數字必須小於或等於2")       # 拋出例外後，函數會立刻跳出，之後的語句不會執行
    else:
        print( 1/num )
    
    print("這句子只有在沒有執行 raise exception時，才不會被跳過 ")
    
except Exception as e:
    print(e)
    



# exercise





