import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

arr1 = np.reshape(arr, (4,3))

"""Indexing"""
print(arr[::2])
print(arr1[:,::2])