#   NumPyArrays.py learning to use NumPy arrays

import numpy as np

#   2D
my_list = [1, 2, 3]
arr = np.array(my_list)

#   3D
my_mat = [[1,2,3],[4,5,6],[7,8,9]]
mat = np.array(my_mat)

#   NumPy built in methods

np.arange(0, 10)    #   Range function (start, size, steps)

np.zeros(3)         #   1D
np.zeros((3,3))     #   2D
np.ones(3)
np.ones((2,4))

np.linspace(0, 10, 20)

np.eye(4)       #   Square matrix (ID matrix)

#   RANDOMS

np.random.rand(5)       #   1D
np.random.rand(5, 5)    #   2D

np.random.randn(2)      #   1D (normal distribution)

np.random.randint(1, 100, 5)

stopper = input()
