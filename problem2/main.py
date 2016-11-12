#!/usr/bin/python3

import sys
from functools import reduce
from itertools import chain
import operator

def tridiag_solve(a, c, b, f, N):
    c_new = [c[0]] + [0] * (N - 1)
    f_new = [f[0]] + [0] * (N - 1)
    for i in range(1, N):
        c_new[i] = c[i] - a[i-1] * b[i-1] / c_new[i-1]
        f_new[i] = f[i] - a[i-1] * f_new[i-1] / c_new[i-1]  

    x = [0] * (N - 1) + [f_new[N-1] / c_new[N-1]] 
    for i in reversed(range(0, N-1)):
        x[i] = (f_new[i] - b[i] * x[i+1]) / c_new[i]
    
    return x

class S3:
    def __init__(self, X, F, N):
        self.X = X.copy()
        a = F.copy()
        c = [0] + tridiag_solve([X[i+1] - X[i] for i in range(1, N-2)],
            [2 * (X[i+2] - X[i]) for i in range(0, N-2)],
            [X[i+2] - X[i+1] for i in range(0, N-3)],
            [6 * ((F[i+2] - F[i+1]) / (X[i+2] - X[i+1]) - (F[i+1] - F[i])/(X[i+1] - X[i])) for i in range(0, N-2)], N - 2) + [0]
        d = [0] + [(c[i] - c[i-1]) / (X[i] - X[i-1]) for i in range(1, N)]
        b = [0] + [(F[i+1] - F[i]) / (X[i+1] - X[i]) + (X[i+1] - X[i]) * (2 * c[i+1] + c[i]) / 6 for i in range(0, N-1)]
        self.splines = list(zip(a[1:], b[1:], c[1:], d[1:], X[1:]))
   
    def get_val_by_spline(self, s, t):
        return s[0] + s[1] * (t - s[4]) + s[2] / 2 * (t - s[4])**2 + s[3] / 6 * (t - s[4])**3 

    def get_val(self, t):
        return self.get_val_by_spline(self.splines[list(filter(lambda s: (s[0] <= s[3]) and (s[3] <= s[1]), 
                                                               zip(self.X, self.X[1:], range(0, N), [t] * N)))[0][2]], t)

class Lagrange:
    def __init__(self, X, F, N):
        self.X = X.copy()
        self.L = lambda t, k: reduce(operator.mul, [t - X[i] for i in chain(range(0,k), range(k+1,N))])
        self.c = [F[i] / self.L(X[i], i) for i in range(0,N)]

    def get_val(self, t):
        return sum([a * b for a,b in zip(self.c, [self.L(t, i) for i in range(0,len(self.X))])]) 

class Newton:
    def __init__(self, X, F, N):
        Y = F.copy()
        self.c = [Y[0]]
        self.X = X

        for i in range(1, N):
            Y = list(map(lambda a: (a[0] - a[1]) / (a[2] - a[3]), zip(Y, Y[1:], X, X[(N - len(Y) + 1):])))
            self.c.append(Y[0])

    def get_val(self, t):
        return self.c[0] + sum([reduce(operator.mul, [t - x for x in self.X[:i]]) * self.c[i] for i in range(1, len(self.c))])

if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print("usage:", sys.argv[0], "<input_file> <output_file>")
        exit(1)
    
    in_file = open(sys.argv[1], 'r')
    out_file = open(sys.argv[2], 'w')
    N = int(in_file.readline())
    lines = in_file.readlines()
    
    x = [float(line) for line in lines[:N]]
    f = [float(line) for line in lines[N:]]
    h = min(map(lambda a: abs(a[1] - a[0]), zip(x, x[1:]))) / 10
    
    p1 = Newton(x, f, N)
    p2 = Lagrange(x, f, N)
    p3 = S3(x, f, N)
    
    out_file.write("x,Newton,Lagrange,S3,f\n")
    for i in range(0, N):
        t = x[i]
        out_file.write(str(t)+","+str(p1.get_val(t))+","+str(p2.get_val(t))+","+str(p3.get_val(t))+","+str(f[i])+"\n")
        t += h
        while (i != N - 1) and (t < x[i + 1]):
            out_file.write(str(t)+","+str(p1.get_val(t))+","+str(p2.get_val(t))+","+str(p3.get_val(t))+"\n")
            t += h
