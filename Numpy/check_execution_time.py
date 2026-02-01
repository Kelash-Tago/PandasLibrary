import numpy as np
import time

size=1_000_000

py_list=list(range(size))
start_time=time.time()
list_sqrt=[i**2 for i in py_list]
end_time=time.time()
print(f"time taken by python list: {end_time-start_time}")

np_arr=np.array(py_list)
start_time=time.time()
arr_sqrt=np_arr**2
end_time=time.time()
print(f"time taken by numpy array : {end_time-start_time}")
