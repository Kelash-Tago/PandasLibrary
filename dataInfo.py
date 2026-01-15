import pandas as pd
df=pd.read_json("students.json")
print(df.to_string(index=False)) #printing without indexes

#check info of data
print(df.info())  