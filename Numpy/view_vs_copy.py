import numpy as np

arr=np.array([1,2,3,4,5])
sub_arr=arr[1:4]
sub_arr[2]=99 
#99 will be reflect in both arrays
print(f"Original array: {arr}") #1,2,3,99,5
print(f"Sub array: {sub_arr}") #2,3,99


#now we will create copy
copy_arr=arr[1:4].copy()
copy_arr[2]=888 # now this will be only in copied array not in original
print(f"original array {arr}")
print(f"sub array {copy_arr}")