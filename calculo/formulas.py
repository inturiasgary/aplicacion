import numpy as np
from math import cos, sin, radians

#datos prueba
b = 0.2
h= 0.6
e=2.1e6
a=b*h
l=5.0
i=b*(h**3.0)/12.0

def matriz_rigidez(e=0.0,a=0.0,l=0.0,i=0.0):
    return np.matrix([
        [e*a/l, 0.0, 0.0, -e*a/l, 0, 0],
        [0.0, 12*e*i/l**3, 6*e*i/l**2, 0, -12*e*i/l**3, 6*e*i/l**2],
        [0.0, 6*e*i/l**2, 4*e*i/l, 0, -6*e*i/l**2, 2*e*i/l],
        [-e*a/l, 0, 0, e*a/l, 0, 0],
        [0.0, -12*e*i/l**3, -6*e*i/l**2, 0.0, 12*e*i/l**3, -6*e*i/l**2],
        [0.0, 6*e*i/l**2, 2*e*i/l, 0.0, -6*e*i/l**2, 4*e*i/l]], dtype=float)

def matriz_rotacion(grado=90.0):
    grado = radians(grado)
    return np.matrix([
        [float(cos(grado)), -(sin(grado)), 0.0, 0.0, 0.0, 0.0],
        [float(sin(grado)), float(cos(grado)), 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, float(cos(grado)), -(sin(grado)), 0.0],
        [0.0, 0.0, 0.0, sin(grado), cos(grado), 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]
        ], dtype=float)

#matriz de rigidez global del elemento 1

#k=r*k*r traspuesta

k = matriz_rigidez(e,a,l,i)
r = matriz_rotacion(90)
#r = np.matrix([[  0.0  ,-1.00000000e+00  , 0.0 ,  0.00000000e+00, 0.00000000e+00 ,  0.00000000e+00],
#         [  1.00000000e+00 ,  0.0 ,  0.00000000e+00 ,  0.00000000e+00,
#                 0.00000000e+00 ,  0.00000000e+00],
#          [  0.00000000e+00 ,  0.00000000e+00 ,  1.00000000e+00 ,  0.00000000e+00,
#                  0.00000000e+00 ,  0.00000000e+00],
#           [  0.00000000e+00 ,  0.00000000e+00 ,  0.00000000e+00 ,  0.0,
#                  -1.00000000e+00 ,  0.00000000e+00],
#            [  0.00000000e+00 ,  0.00000000e+00 ,  0.00000000e+00 ,  1.00000000e+00,
#                    0.0 ,  0.00000000e+00],
#             [  0.00000000e+00 ,  0.00000000e+00 ,  0.00000000e+00 ,  0.00000000e+00,
#                     0.00000000e+00 ,  1.00000000e+00]])

t = np.transpose(r)
#k = np.multiply(k,r)
#k = np.multiply(k,t)
k = r*k*t
print "mrmrmrmrmrmrmmrmrmrmrmrmrmr"
print matriz_rigidez(e,a,l,i)
print "rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr"
print r
print "tttttttttttttttttttttttttttttttttttttt"
print t
print "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"
print k.round(decimals=3)
