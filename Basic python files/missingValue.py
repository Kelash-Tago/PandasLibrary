import pandas as pd
data = {
"Name": [ 'Kelash', None, 'Suresh', 'Amrat', 'Adil', 'Jagdish', 'Raj', 'Simran'],
"Age" : [28,34,22,30,29,40,25,32],
"Salary": [50000, 60000,None,52000, None, 70000,48000,58000],
"Performance_Score": [85,90,79,None,78,90,70,69]
}
df=pd.DataFrame(data)
print(df.isnull()) # this method shows true where there is not value

print(df.isnull().sum()) # this will show column name with total missing values


