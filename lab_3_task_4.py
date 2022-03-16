import numpy as np
K = int(input('K = '))
M = int(input('M = '))
Y = np.zeros((K, M))
for i in range(K):
  for j in range(M):
    if (np.sin(K * (i+1) + M * (j+1))) > 0:
      Y[i, j] = np.sin(K * (i+1) + M * (j+1))
    else:
      Y[i, j] = 0
print(Y)