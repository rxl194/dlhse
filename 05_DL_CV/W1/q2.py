
import numpy
import scipy.signal

I = [[8, 6, 2, 7], [6, 2, 4, 1], [5, 8, 5, 2], [3, 0, 3, 2]]
K = [[4, 3], [7, 2]]

result = scipy.signal.convolve2d(I,K)
print (result)
