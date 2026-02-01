import numpy as np
arr=np.array([-4,4,6,88,101,3,-4,-8])

print("wtih invalid readings:",arr)

average=sum(arr)/len(arr)
print("Average: ",average)

invalid_readings=0
for i in range(0,len(arr)):
    if(arr[i]>100 or arr[i]<0):
        invalid_readings+=1
        arr[i]=average
print("Total invalid readings: ",invalid_readings)
print("after removing invalid with average: ",arr)