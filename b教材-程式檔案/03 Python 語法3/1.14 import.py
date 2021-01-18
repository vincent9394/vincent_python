# 一般匯入
import math
print( math.log(100, 10) )   # 計算 log(100) = 2
print( math.factorial(5) )   # 計算 5! = 120



# 一般匯入加上別名 import as
import math as m
print( m.add(1,3) )
print( m.subtract(1,3) )




# 匯入所有函數
from math import *
print( log(100, 10) )
print( factorial(5) )



# 只匯入 log, factorial 函數
from math import log, factorial
print( log(100, 10) )
print( factorial(5) )




# 一句匯入多個模組
import math, datetime
math.log(100, 10)         # 計算 log(100) = 2
datetime.datetime.now()   # 取得現在日期時間



# List 函數
sum( [1, 2, 3, 4, 5] )
max( [1, 5, 60, 2, 1] )
reversed( [1, 2, 3, 4, 5] )


# 日期時間程式庫
import datetime, time
time.sleep(5)
print( datetime.datetime.now() )



# 數學程式庫
import math
print( math.log(100, 10) )
print( math.ceil(1.1) )



# glob 程式庫
import glob
glob.glob( "*.*" )



# json 程式庫
import json
json.dumps( [1, 2, 3] )
json.loads( "[1, 2, 3]" )


