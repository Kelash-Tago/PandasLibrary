import pandas as pd
data = {
"Name": [ 'Kelash', None, 'Suresh', 'Amrat', 'Adil', 'Jagdish', 'Raj', 'Simran'],
"Age" : [28,34,22,30,29,40,25,32],
"Salary": [50000, 60000,None,52000, None, 70000,48000,58000],
"Performance_Score": [85,90,79,None,78,90,70,69]
}
df=pd.DataFrame(data)
#this method will remove all the rows which are incomplete 
# df.dropna(inplace=True)
# print(df)

#or we can fill data
df.fillna(0,inplace=True) #fill 0 where there is missing value
print("modified data")
print(df)
