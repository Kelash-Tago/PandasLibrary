import numpy as np
 
arr1=np.zeros((3,4))
print(arr1)
# check total rows and total columns
print("columns and rows: ",arr1.shape) 


#interger array
arr1=np.zeros((3,4),dtype="int64")
print(arr1)

arr1=np.ones((3,4)) #here 
print(arr1)

# fill with your own values
arr1=np.full((3,4),50)
print("array with 50:")
print(arr1)

arr1=np.eye(3) #identity matrix which takes only dimension
print(arr1)


arr1=np.arange(50,100,3) #create arr with start end and steps 
print(arr1)

arr1=np.linspace(1,100,4) #start end total arrayvalues
print(arr1)