import numpy as np

np.zeros(10)
np.ones(10)

np.zeros(10) + 5
np.ones(10) * 5

np.arange(10 , 51)

np.arange(10 , 51, 2)

np.arange(9).reshape(3, 3)

np.eye(3)

np.random.rand(1)

np.random.randn(25)
np.random.randn(25).shape

np.arange(1, 101).reshape(10, 10)/ 100

np.linspace(0.01, 1, 100).reshape(10, 10)

np.linspace(0, 1, 20)

mat = np.arange(1, 26).reshape(5, 5)

mat[2:, 1:]

mat[3, 4]

mat[:3, 1: 2]

mat[4, :]

mat[-1, :]

mat[3:5, :]

np.sum(mat)
mat.sum()

np.std(mat)
mat.std()

mat.sum(axis=0)