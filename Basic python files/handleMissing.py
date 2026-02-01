import pandas as pd
data = {
"Name": [ 'Kelash', None, 'Suresh', 'Amrat', 'Adil', 'Jagdish', 'Raj', 'Simran'],
"Age" : [28,34,None,30,29,40,25,None],
"Salary": [50000, 60000,None,52000, None, 70000,48000,58000],
"Performance_Score": [85,90,79,None,78,90,70,69]
}
df=pd.DataFrame(data)
#this method will calculate mean and fill age column missing value
df['Age'].fillna(df['Age'].mean(),inplace=True)
print(df)