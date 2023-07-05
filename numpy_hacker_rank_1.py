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
print(lst)

