import pandas as pd
data = {
"Name": [ 'Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
"Age" : [28,34,22,30,29,40,25,32],
"Salary": [50000, 60000,45000,52000, 49000, 70000,48000,58000],
"Performance_Score": [85,90,78,92,88,95,80,89]
}

df = pd.DataFrame(data) 
df["bonous"]=df["Salary"]*0.1 #this will add new column to data named bonous
print(df)

df.insert(0,"EmployeeID",[10,20,30,40,50,60,70,80]) #this method will add new column 
#if one value in list is less or greater than rows then it will show error message
print(df)
