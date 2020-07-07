from collections import Counter
import matplotlib.pylab as plt
#from collections import OrderedDict
from operator import itemgetter
import numpy as np
from sympy import *
import math
import json
import csv
import ast

#d = {7: 30881137, 6: 29078921, 8: 28678341, 9: 23682326, 5: 23446846, 10: 17599959, 4: 15763393, 11: 11886540, 3: 8468875, 12: 7362490, 13: 4204355, 2: 3411837, 14: 2231028, 15: 1103706, 1: 911441, 16: 511082,
     #17: 223494, 18: 91879, 19: 35485, 20: 13260, 21: 5028, 22: 1598, 23: 528, 24: 159, 25: 73, 26: 18, 27: 1}

with open('data_1x.txt', 'r') as file:
    d = {}
    for line in file:
        new_line = (line.replace('Counter','').replace('(','').replace(')',''))
        print(type(new_line))
        d = ast.literal_eval(new_line)
        print(type(d))
        
    
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


plt.suptitle("Aerospike Load 1x")
plt.title('alpha = '+str(alpha))
plt.xlabel("Positional Rank")
plt.ylabel("Prob(axis)")
plt.xlim([100,N])
li_scaled = scale_li()
m, n = zip(*li_scaled)
plt.plot(m, n)

alpha = .33161117497077947
A = constant(alpha)
model = zipf(A, alpha)
plt.plot(range(0, N, 100),model)
plt.show()

