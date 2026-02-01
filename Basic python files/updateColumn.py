import pandas as pd
data = {
"Name": [ 'Kelash', 'Ramesh', 'Suresh', 'Amrat', 'Adil', 'Jagdish', 'Raj', 'Simran'],
"Age" : [28,34,22,30,29,40,25,32],
"Salary": [50000, 60000,45000,52000, 49000, 70000,48000,58000],
"Performance_Score": [85,90,79,92,78,90,70,69]
}

df=pd.DataFrame(data)
#update any column 
df['Salary']=df['Salary']*1.5
print(df)

#remove Performance_Score column
df.drop(columns=['Performance_Score'],inplace=True)
print("Modified data")
print(df)