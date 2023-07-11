import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

arr1 = np.reshape(arr, (4,3))

"""Indexing"""

# print(arr[:])
# print(arr1[:,::2])

# print(np.array([12,3,4], int))

## Sorting - np.argsort() and np.sort()

arr = np.array([3,5,2])
# print(np.sort(arr))
# arr.sort()
# print(arr) # This returns None. 

arr = np.array([5,3,26,732,29])
arr.sort()
# print(arr)

lst = [5,3,26,732,29] 
# print(lst.sort()) # --> None
lst.sort() # Original gets sorted. 
# print(lst)

arr = np.array([[5,3,2,8], [5,2,6,4]])
print(np.sort(arr,1)) # --> [[2,3,5,8], [2,4,5,6]]
arr.sort()
print(arr) # --> [[2,3,5,8], [2,4,5,6]]
