import pandas as pd

arr=pd.Series([1,2,3,4])
print(arr)

# with labelled indexes
arr2=pd.Series([1,2,3,4],index=["one","two","three","four"])
print(arr2)
print(arr2["one"])
print(arr2[0])