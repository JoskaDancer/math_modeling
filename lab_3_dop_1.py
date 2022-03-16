import numpy as np

c = 1
a = np.zeros((4, 3))
b = a[:]
for i in range(4):
  for j in range(3):
    a[i, j]=c
    c += 1

print(a, '\n', b)

