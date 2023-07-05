import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

arr1 = np.reshape(arr, (3,4))
arr2 = arr.reshape(3,4)
print(arr1)
print(arr2)