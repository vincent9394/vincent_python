#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 15:01:03 2018

@author: Benson
"""


# if 
price = 20
if price > 10:
    print( "Sell 1" )
    print( "Sell 2" )
print( "Continue" )

    

# if - else
price = 5
if price > 10:
    print( "Sell" )
else:
    print( "Buy" )
print( "Continue" )


    
    
# if - elif
price = 50
if price < 10:
    print( "Buy" )
elif price > 40:	# 意思是 else if
    print( "Sell" )
print( "Continue" )

    
    
    
# multiple elif
price = 150
if price <= 50:
    print( "smaller than or equals to 50" )
elif price <= 100:
    print( "Between 50 and 100" )
elif price <= 200:
    print( "Between 100 and 200" )
elif price <= 300:
    print( "Between 200 and 300" )
else:
    print( "Larger than 300" )

    
	

# pass
price = 80
if price <= 50:
    print( "less than 50" )
elif price <= 100:
    pass		# 不做任何動作
else:
    print( "More than 100" )




# nested if
price = 40
if price <= 50:
    if price <= 25:
        print( "小於 25" )
    else:
        print( "26 至 50" )
    print( "Continue" )
else:
    print( "大於 50" )

    
    
	
# more nested if 
price = 10
if price <= 50:
    print( "Action 1" )  
	
    if price <= 25:
        print( "less than 25" )
    else:
        print( "Between 26 and 50" )
		
    print( "Action 2" )
	
else:
    print( "More than 50" )
	
print( "Action 3" ) 
    
	
	

# if sequences
price = input( "請輸入貨品價錢：" )
price = float(price)

if price <= 100:
    print( "很便宜，我會買！" )
elif price <= 200:            
    print( "有點貴，我再考慮！" )
else:
    print( "太貴，不會買！" )

    
    
# excercise
weather = "sunny"
forecast = "rainy"

if weather == "sunny":
    print( "hiking" )


