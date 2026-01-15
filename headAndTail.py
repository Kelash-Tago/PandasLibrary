import pandas as pd
data=pd.read_json("data.json")
print("two rows of data:") #this read two lines of data
data.head(2)
print("5 rows")
print (data.head()) #by default it displays 5 rows from head if it is in data

#same works for tail method i
print("2rows using tail method")
print(data.tail(2))


