import pandas as pd
import numpy as np

df=pd.DataFrame([["Kelash",19],["Sanjay",20],["Aneel",21]],columns=["Name","Age"])
print(df)

#another method using numpy arr

arr=np.array([[1,2,3,4],[5,6,7,8]])
df2=pd.DataFrame(arr,columns=["A","B","C","D"])
print(df2)


#for one dimensional
arr2=np.array([1,2,3,4])
df3=pd.DataFrame(arr2,columns=["A"])
print(df3)