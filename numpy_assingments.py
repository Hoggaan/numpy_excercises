import numpy as np

# Question - 1
a = np.array([[6, 28], [8, 56], [7, 19]])

x=np.transpose(a).reshape(1,6)
# print(x.shape)

# Take away: (1,6) = [[]]. 2D array

# Question 2
a = np.array([[16, 5], [81, 6], [33, 1]])

x=np.transpose(a).reshape(2,3)

# print(x.flatten().shape)
# Take away: flatten() gives you []. 1 D array

a = np.array([[34, 28,55], [8, 56, 3], [77, 87, 19]])

# print(a.transpose()[-2,-2])

# -----------

# arr = 2*np.arange(0,2,0.5)
# if np.any(arr <= 0.6):
#     print ("condition satisfies")
# else:
#     print ("condition doesn't satisfy")


arr = np.array([1,2,3,0,-2,4])
arr1 = arr1 = arr[arr > 0]
arr[0] = 10
# print(arr)
# print(arr1)

arr = np.arange(16).reshape(4,4)  

# print(np.split(arr, 4))
 
 
import numpy as np

X = np.arange(12).reshape((3, 4))
row = np.array([0, 1, 2])
mask = np.array([1, 0, 1, 0], dtype=bool)
# print(X[row[:, np.newaxis], mask].shape)

arr1 = np.arange(4)
arr2 = np.arange(3).reshape(3,1)

arr2 = np.zeros(3, int).reshape(3,1)
# print(arr2)
# print(X[arr2, mask])
# print(X)


# arr = np.arange(3)
# print(arr)
# arr1 = arr[:, np.newaxis]
# print(arr1.shape)
# arr2 = arr[np.newaxis,:]
# print(arr2)

import numpy as np
arr= np.array([[2,3,4,5],[1,7,3,5],[2,8,6,9],[11,23,12,19]])

arr1 = 2
def func(x, y):
    return x * y
vec = np.vectorize(func)
# print(vec(arr, arr1))


arr = np.arange(9).reshape(3,3,1)
# print(arr.shape)
arr = np.squeeze(arr,2)
# print(arr.shape)

import numpy as np
arr = np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])

# ar = np.hstack((arr,arr[:, 0])) 
# print(ar)


arr = np.arange(16).reshape(2,2,4)
# print(arr[0,0:,1].shape)

j = 2
arr = np.array([[5,3,9],[2, 1, 4], [7,6,8]])
arr = arr[arr[:, 1].argsort()]
# print(arr)

# print(np.random.normal())

A = np.arange(960).reshape(10,3,32)
B = np.arange(30).reshape(10,3, 1)
X = A + B
print(X.shape)

x = (2,2)
print(x[0])