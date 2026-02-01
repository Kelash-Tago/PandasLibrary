import numpy as np

arr=np.array([[1,4,3],[1,2,3]])
# for sum of all values
print(np.sum(arr))

# for coulumn wise printing sum
print(np.sum(arr,axis=0)) 

#for each row
print(np.sum(arr,axis=1)) 
