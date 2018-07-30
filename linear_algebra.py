import sys
import numpy as np

print("Python: {}".format(sys.version))
print("Numpy: {}".format(np.__version__))


# define a scalar
x = 6

# define a vector
v = np.array((1, 2, 3))
print("Vector dimensions {}".format(v.shape))
print("Vector size {}".format(v.size))

# define a matrix
m = np.matrix([[1,2,3], [4,5,6], [7,8,9]])
print("Matrix dimensions {}".format(m.shape))
print("Matrix size {}".format(m.size))