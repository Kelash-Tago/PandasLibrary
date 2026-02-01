import pandas as pd
data=pd.read_csv("students.csv")

#selecting one specific column
print("one name column")
name=data['Name']
print(name)

# for selecting multiple columns 
print("printing multiple columns")
subset=data[["Name","Age"]]
print(subset)


