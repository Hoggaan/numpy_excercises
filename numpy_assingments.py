import numpy as np

# Question - 1
a = np.array([[6, 28], [8, 56], [7, 19]])

x=np.transpose(a).reshape(1,6)
print(x.shape)

# Take away: (1,6) = [[]]. 2D array

# Question 2
a = np.array([[16, 5], [81, 6], [33, 1]])

x=np.transpose(a).reshape(2,3)

print(x.flatten().shape)
# Take away: flatten() gives you []. 1 D array

a = np.array([[34, 28,55], [8, 56, 3], [77, 87, 19]])

print(a.transpose()[-2,-2])