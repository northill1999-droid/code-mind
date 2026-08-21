import numpy as np

k = 1
A = np.array([
    [1, 30],
    [1, 6]
])
b = np.array([8*k*30, 10*k*6])

y, r = np.linalg.solve(A, b)

t_target = 10
n = (y + r * t_target) / (k * t_target)
print(n)