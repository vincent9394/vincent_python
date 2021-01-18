#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 09:53:14 2018

@author: Benson
"""


# Use the keys to get the elements
person = {
    "id": 1, 
    "name": "benson"
}

person["id"]      # 1
person["name"]    # "benson"

# replace the existing element
person["id"] = 2 


# add a element to dictionary
person["gender"] = "male"


# delete an element
del person["id"]


# count the length of the dictionary
print( len(person) )


# check the existance of key
print( "name" in person )



# Keys can be other types than string
mixed = {
    "10":   "data 1", 
    10:     "data 2", 
    (1, 2): "data 3"
}

print( mixed["10"] )
print( mixed[10] )
print( mixed[(1, 2)] )





################   選讀部份   ################


# get all the keys - .keys()
list( person.keys() )


# get all the values - .values()
list( person.values() )


# get all the key-values pairs - .items()
list( person.items() )



# joining the dictionaries
a = { "id": 1 }
b = { "name": "benson", "phone": "1234" }
c = { "name": "kong", "year": "2018" }
d = { **a, **b, **c }
print( d )




# exercise


# answer of the challenge question


# If not using dict, you need three variables to store stock data!
share = ["00001", "00002", "00001", "00002"]
price = [10.0, 16.5, 10.3, 16.7]
time  = ["10:30", "10:30", "10:31", "10:31"]


# Rewrite above using list of dicts to store data in a single variable
shares = [
    {"share": "00001", "price": 10.0, "time": "10:30"}, 
    {"share": "00002", "price": 16.5, "time": "10:30"}, 
    {"share": "00001", "price": 10.3, "time": "10:31"}, 
    {"share": "00002", "price": 16.7, "time": "10:31"}
]










