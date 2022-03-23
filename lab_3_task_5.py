import numpy as np
import random

N = 2
M = 3
m = np.zeros((N, M))

for i in range(N):
  for j in range(M):
    m[i, j] = random.randit(1, 50) * (i+1) *(j+1)

print(a)

a = 0
b = 2

for i in range(N):
  m[i, a], m[i, b] = m[i, b], m[i, a]

print(m)