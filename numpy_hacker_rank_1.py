import numpy as np

# Changing the data type 
a = np.array([1,2,3,4])
b = np.array(a, float)
c = np.array([1,2,3], float)
d = np.array([1,2,4], dtype=float)
print(a,b,c,d)