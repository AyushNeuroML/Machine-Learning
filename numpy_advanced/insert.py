import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr)
new_arr = np.insert(arr,2,100,axis=0)
print(new_arr)