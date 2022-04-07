import numpy as np

N = 4

grid = np.zeros((N, N))

poss = list(zip(*np.where(grid == 0)))

print(grid)
print(poss)