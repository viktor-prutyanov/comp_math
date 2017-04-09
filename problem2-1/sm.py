#!/usr/bin/python3

'''
    @author: Viktor Prutyanov mailto:viktor.prutyanov@phystech.edu
'''

import math
import sys

def df(x, u):
    return ((-1.5*u[0]/(x+1)+2/math.sqrt(x+1)), u[0])

def euler_solve(a, b, u0, n, hasFile, file):
    x = a
    u = u0
    h = (b - a) / n

    if hasFile:
        file.write("x,y,y'\n")
        file.write(str(x) + "," + str(u0[0]) + "," + str(u0[1]) + "\n")

    for i in range(0, n):
        u = (u[0] + h * df(x, u)[0], u[1] + h * df(x, u)[1])
        x = x + h
        if hasFile:
            file.write(str(x) + "," + str(u[0]) + "," + str(u[1]) + "\n")

    return u

def main():
    if (len(sys.argv) != 6):
        print("usage:", sys.argv[0], "[out_file] [a_initial] [eps] [K] [N]")
        sys.exit(-1)
    
    out_file = open(sys.argv[1], 'w') 
    a   = float(sys.argv[2])
    eps = float(sys.argv[3])
    K   = int(sys.argv[4])
    N   = int(sys.argv[5])

    print("a =", a, "eps =", eps, "K =", K, "N =", N)

    for k in range(0, K):
        u1 = euler_solve(0.0, 1.0, (0, a),       N, False, out_file)
        print("u1 = ", u1)
        u2 = euler_solve(0.0, 1.0, (0, a + eps), N, False, out_file)
        print("u2 = ", u2)
        a = a - u2[1] * eps / (u2[1] - u1[1])
        print("k =", k, "a =", a)

    u1 = euler_solve(0.0, 1.0, (0, a), N, True, out_file)

if __name__ == '__main__':
    main()