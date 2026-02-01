import numpy as np

arr1=np.array([0,1,2,3,4,5,6])
#fancy indexing
index=[0,2,3]
print(arr1[index])

#boolean indexing
print(arr1[arr1>3]) #it will print values greater than 3 