import numpy as np
arr1=np.array([1.2,3.4,4.6])
print(arr1)

# now change it to int
new_arr=arr1.astype('i')
print(new_arr)
print(f"type of new arr: {new_arr.dtype}")

print(arr1.base)
print(new_arr.base)