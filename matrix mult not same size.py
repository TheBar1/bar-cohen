import numpy as np

x = np.array([[2, 5], [3, 10]])
'''
2 5
3 10
'''
y = np.array ([[20, 6], [5, 1], [5, 8]])
'''
20 6
5 1
5 8
'''
#y = y[:2]

while(not x.shape[1] == y.shape[0]):
    y = y[:y.shape[1]]
print(np.dot(x, y))