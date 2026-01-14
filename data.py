import pandas as pd
data={
    "Name":["Kelash","Ramesh","Suresh"],
    "Age":[20,30,23],
    "City":["Sukkur","Larkana","Karachi"]
}

df=pd.DataFrame(data)
print(df)
#write index false to avoid writing index
# column in csv file otherwise it will write index also automatically
df.to_csv("data.csv",index=False)
df.to_json("data.json")
