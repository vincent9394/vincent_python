# -*- coding:utf-8 -*-
import re
import numpy as np

text = ""



separators =  ", ",'\n',',["', 'me",["',"\n",'\"]\n,1]\n,[\"description\",[\"',"\\n"
 
 
 
def custom_split(sepr_list, str_to_split):
    # create regular expression dynamically
    regular_exp = '|'.join(map(re.escape, sepr_list))
    return re.split(regular_exp, str_to_split)
 
 
abc = custom_split(separators, text)
subs = '店名|類別|詳細分類|地址|電話'
 
res = [x for x in abc if re.search(subs, x)]
arr = np.array(res)

#newarr = arr.reshape(-1,5 )

#print(newarr)

for x in res:
   print(x)