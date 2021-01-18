#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 12:26:28 2018

@author: Benson
"""


# while loop
i = 0
while i < 5:
    print(i)
    i = i + 1

    
    
# 無限迴圈
i = 0
while i < 5:    
    print(i)
    # 忘記加上 i = i + 1 語句，i 永遠等於 0！

    
    
# 無限迴圈也可寫成以下語法：
while True:
    print(i)


    
    
# break 用法
i = 0
while True:
    i += 1
    if i >= 5:
        break
    print(i)

    
    
# continue 用法
i = 0
while i < 5:
    i += 1
    if i == 2:
        continue
    print(i)


    
#exercises


