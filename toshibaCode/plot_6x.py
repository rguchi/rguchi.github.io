from collections import Counter
import matplotlib.pylab as plt
#from collections import OrderedDict
from operator import itemgetter
import numpy as np
from sympy import *
import math
import json
import csv

d = {44: 12519547, 45: 12408723, 43: 12355407, 46: 12036085, 42: 11904078, 47: 11420534, 41: 11221122, 48: 10617082, 40: 10312583, 49: 9667200, 39: 9252632, 50: 8626844, 38: 8093738, 51: 7545993, 37: 6900590, 52: 6478022, 36: 5723632, 53: 5450868, 35: 4621156, 54: 4503534, 55: 3654685, 34: 3630375, 56: 2914483, 33: 2766335, 57: 2282507, 32: 2048657, 58: 1755708, 31: 1471417, 59: 1329278, 30: 1021904, 60: 989031, 61: 724697, 29: 686119, 62: 521873, 28: 446590, 63: 369603, 27: 279518, 64: 258673, 65: 177073, 26: 169049, 66: 120985, 25: 98466, 67: 80338, 24: 55630, 68: 52963, 69: 34084, 23: 29414, 70: 21933, 22: 15096, 71: 13975, 72: 8488, 21: 7490, 73: 5397, 20: 3542, 74: 3165, 75: 1857, 19: 1702, 76: 1114, 18: 728, 77: 620, 78: 373, 17: 322, 79: 179, 80: 107, 16: 105, 81: 58,
     15: 37, 82: 34, 83: 21, 14: 16, 13: 7, 84: 3, 85: 3, 12: 2, 86: 1}
j = (sorted(d.items(), reverse = True))

def total_count():
    s = Counter(d.values())
    print('total count:',sum(s))
    return sum(s)

N = int(209E6)
print('N:',N)
x, y = zip(*j)
#print(y)

def scale_li():
    s = li_sum()
    scaled = []
    pos = 1
    for i in range(int(len(x))):
        if pos >= N:
            break
        scaled.append((min(pos, N)-1, x[i]/s))
        scaled.append((min(pos-1 + y[i], N)-1, x[i]/s))
        pos = min(pos-1 + y[i], N)
    return scaled

def li_sum():
    ax = 0
    ys = 0
    for i in range(int(len(x))): 
        diff = min(N-ys, y[i])
        if diff <= 0:
            break
        ys = ys + diff
        a = ((x[i]))*diff
        ax = ax + a
    print('sum: ',ax)
    return ax

def constant(alpha):
    z = 0
    for i in range(1, N):
        z = z + 1/i**alpha
    A = 1/z
    print('A: ',A)
    return A

def zipf(A, alpha):
    zi = np.zeros(int(N/100))
    for i in range(0, N, 100):
        zi[int(i/100)] = A/(i+1)**alpha
    return zi


plt.suptitle("Aerospike Load 6x")
plt.title('alpha = .13277299247789226')
plt.xlabel("Positional Rank")
plt.ylabel("Prob(axis)")
li_scaled = scale_li()
m, n = zip(*li_scaled)
plt.plot(m, n)

alpha = .13277299247789226
A = constant(alpha)
model = zipf(A, alpha)
plt.plot(range(0, N, 100),model)
plt.show()

