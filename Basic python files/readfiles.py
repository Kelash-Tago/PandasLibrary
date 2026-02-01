import pandas as pd
# data=pd.read_csv("students.csv",encoding='utf-8')
# print(data)
data=pd.read_json("students.json")
print(data)