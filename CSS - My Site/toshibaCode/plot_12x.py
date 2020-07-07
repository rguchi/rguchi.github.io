from collections import Counter
import matplotlib.pylab as plt
#from collections import OrderedDict
from operator import itemgetter
import numpy as np
from sympy import *
import math
import json
import csv

d = {89: 8860429, 88: 8838333, 90: 8786845, 87: 8721937, 91: 8613496, 86: 8500196, 92: 8354899, 85: 8194973,
     93: 8012742, 84: 7802212, 94: 7606076, 83: 7353974, 95: 7140096, 82: 6838504, 96: 6638649, 81: 6285672,
     97: 6107996, 80: 5711028, 98: 5554306, 79: 5119178, 99: 5010347, 78: 4533227, 100: 4467499, 77: 3962113,
     101: 3940918, 102: 3447522, 76: 3422298, 103: 2987382, 75: 2912929, 104: 2562264, 74: 2446162, 105: 2178375,
     73: 2028960, 106: 1829957, 72: 1660093, 107: 1523874, 71: 1339378, 108: 1259139, 70: 1065521, 109: 1026590,
     69: 836322, 110: 832696, 111: 667531, 68: 645593, 112: 531755, 67: 492158, 113: 418555, 66: 370184, 114: 328365,
     65: 273832, 115: 254261, 64: 199151, 116: 194526, 117: 148379, 63: 143720, 118: 111227, 62: 101594, 119: 83797,
     61: 70253, 120: 62302, 60: 48494, 121: 45838, 122: 33362, 59: 32637, 123: 24429, 58: 21556, 124: 17603, 57: 14042,
     125: 12431, 56: 9004, 126: 8805, 127: 6293, 55: 5579, 128: 4345, 54: 3581, 129: 3077, 130: 2143, 53: 2135, 131: 1481, 52: 1311, 132: 1052, 51: 701, 133: 691, 134: 486, 50: 432, 135: 283, 49: 247, 136: 202, 48: 141, 137: 128, 138: 102, 47: 77, 139: 56, 46: 42, 140: 42, 45: 22, 142: 16, 141: 15, 143: 9, 44: 6,
     144: 4, 147: 4, 43: 2, 40: 1, 145: 1, 148: 1, 150: 1}

j = (sorted(d.items(), reverse = True))

def total_count():
    s = Counter(d.values())
    print('total count:',sum(s))
    return sum(s)

N = int(total_count()/100)*100
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
    zi = []
    #zi = np.zeros(int(N/100))
    print(type(zi))
    for i in range(1, N, 100):
        zi.append(A/(i)**alpha)
    print(len(zi))
    return zi


alpha = .09395004006428298
plt.suptitle("Aerospike Load 12x")
plt.title('alpha = '+str(alpha))
plt.xlabel("Positional Rank")
plt.ylabel("Prob(axis)")
plt.xlim([100,N])
#plt.xscale('log')
#plt.yscale('log')
li_scaled = scale_li()
m, n = zip(*li_scaled)
plt.plot(m, n)


A = constant(alpha)
model = zipf(A, alpha)
plt.plot(range(100, N, 100),model)
plt.show()

