import pandas as pd
data=pd.read_json("students.json")
print(data.describe())  