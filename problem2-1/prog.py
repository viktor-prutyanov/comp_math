#!/usr/bin/python3

'''
    @author: Viktor Prutyanov mailto:viktor.prutyanov@phystech.edu
'''

import math
import sys

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

def p(x): 
    return 1.5/(x+1)

def f(x):
    return 2/math.sqrt(x+1)

def main():
    N   = int(sys.argv[1])
    out_file = open(sys.argv[2], 'w') 
    h = 1 / N

    H = [i*h for i in range(0, N)]
    C = [-1] + [-2/(h*h)] * (N - 1) + [0]
    A = [1/(h*h) - p(x)/(2*h) for x in H] + [0]
    B = [1] + [1/(h*h) + p(x)/(2*h) for x in H]
    F = [h*h] + [f(x) for x in H] + [0]

    y = tridiag_solve(A, C, B, F, N + 1)
    out_file.write("x, y\n")
    [out_file.write(str(H[i]) + "," + str(y[i]) + "\n") for i in range(0, N)]

if __name__ == '__main__':
    main()
