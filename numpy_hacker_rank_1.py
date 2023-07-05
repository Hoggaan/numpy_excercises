import numpy as np

# Changing the data type 
a = np.array([1,2,3,4])
b = np.array(a, float)
c = np.array([1,2,3], float)
d = np.array([1,2,4], dtype=float)
# print(a,b,c,d)

# Shape 
arr = np.array([1,2,3,4,5,6])
arr1 = np.array([1,2,3,4,5,6])

arrs = arr.shape = (3,2)
# print(arr.shape)
# print(arrs)
# print(arr1.reshape(3,2).shape)
# print(arr1.shape)

# Transpose 
arr = np.array([[1,2,3], [4,5,6]])
arr_t = np.transpose(arr)
arr_t1 = arr.transpose()
arr_t2 = arr.T
# print(arr_t)
# print(arr_t1)
# print(arr_t2)
# print(arr)

# Flatten
arr = np.array([[1,2,3], [6,5,2]])
# print(arr.flatten())

import random
lst = [4,3,5]
for i in range(6,9):
    lst = lst + [i]
# print(lst)

arr = np.array([1,2,3])
arr1 = 2**arr
arr2 = arr ** 2
# print(arr1, arr2)
arr = np.array(range(10))
lst = list(range(10))
# print(lst)

# arr1 = np.array(range(0,10,0.5))
arr2 = np.arange(0,10, 0.5)
# print(arr1)
# print(arr2)

'''---------------------------------------'''
arr = np.array([1, "kow"])
# print(arr.dtype)
# print(np.array([1,2,3]).dtype)
# print(np.array([0.2, 1]).dtype)

# In numpy the array elements must be the same data type. 
# If you give different elements with different data types it will convert
# The same data type. 

""" Changing the data type of an array"""
# arr2 = arr2.astype("int")
arr2 = arr2.astype("float")
print(arr2)