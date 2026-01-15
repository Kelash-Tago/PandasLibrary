import pandas as pd
data=pd.read_json("students.json")
print(data)
print(f"Shape {data.shape}") # it tells total rows and columns in the dataset
print(f"Columns Names : {data.columns}") #tells column names in list

