from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.template.loader import get_template
import numpy as np
import numpy.matlib
from math import cos, sin, radians


def index(request):
    from random import randint
    '''a = np.array([[36. , 51., 13. ],
           [52. , 34., 74. ],
           [ 0. , 7.,  1.1]])
    b = np.array([ 3., 45., 33.])'''
    n = 48
    m = 48
    a1 = []

    for i in range(n):
        a1.append([randint(0, 1000) for i in range(m)])
    b = []
    a = []
    a = np.array(a1)
    b1 = []
    for i in range(1):
        for j in range(m):
            b1.append(randint(0, 100))
    b = np.array(b1)
    x = np.linalg.solve(a, b)
    resultado = x.tolist()
    return render_to_response('index.html', {'matriza': a, 'matrizb': b,
    'resultado': resultado})


def peso(request):

    return render_to_response('peso.html')


def matriz(request):

    if 'elementos' in request.GET and request.GET['elementos']:
        elementos = request.GET['elementos']
        nodos   = request.GET['nodos']
        #mensaje = 'vamos bien, dato enviado: %d' % int(request.GET['elementos'])
        return render_to_response('elementos.html', {'cantidadElementos':int(elementos), "cantidadNodos":int(nodos),
            'elementos':range(int(elementos)), 'nodos':range(int(nodos)+1)}, context_instance=RequestContext(request))
    else:
        mensaje = 'vamos mal'
    return HttpResponse(mensaje)

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


def matriz_rigidezEE(e=0.0, l=0.0, b=0.0, h=0.0):
    i = b * (h ** 3.0) / 12.0
    a = b * h
    return np.matrix([
        [e*a/l, 0.0, 0.0, -e*a/l, 0, 0],
        [0.0, 12*e*i/l**3, 6*e*i/l**2, 0, -12*e*i/l**3, 6*e*i/l**2],
        [0.0, 6*e*i/l**2, 4*e*i/l, 0, -6*e*i/l**2, 2*e*i/l],
        [-e*a/l, 0, 0, e*a/l, 0, 0],
        [0.0, -12*e*i/l**3, -6*e*i/l**2, 0.0, 12*e*i/l**3, -6*e*i/l**2],
        [0.0, 6*e*i/l**2, 2*e*i/l, 0.0, -6*e*i/l**2, 4*e*i/l]], dtype=float)


def matriz_rigidezAE(e=0.0, l=0.0, b=0.0, h=0.0):
    i = b * (h ** 3.0) / 12.0
    a = b * h
    return np.matrix([
        [e*a/l, 0.0, 0.0, -e*a/l, 0.0, 0.0],
        [0.0, 3 * e * i / l ** 3, 0.0, 0.0, -3 * e * i / l ** 3, 3 * e * i / l ** 2],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [-e*a/l, 0.0, 0.0, e*a/l, 0, 0],
        [0.0, -3*e*i/l**3, 0.0, 0.0, 3*e*i/l**3, -3*e*i/l**2],
        [0.0, 3*e*i/l**2, 0.0, 0.0, -3*e*i/l**2, 3*e*i/l]], dtype=float)


def matriz_rigidezEA(e=0.0, l=0.0, b=0.0, h=0.0):
    i = b * (h ** 3.0) / 12.0
    a = b * h
    return np.matrix([
        [e*a/l, 0.0, 0.0, -e*a/l, 0.0, 0.0],
        [0.0, 3 * e * i / l ** 3,  3 * e * i / l ** 2, 0.0, -3 * e * i / l ** 3, 0.0],
        [0.0, 3 * e * i / l ** 2, 3 * e * i / l, 0.0, -3 * e * i / l ** 2, 0.0],
        [-e*a/l, 0.0, 0.0, e*a/l, 0, 0],
        [0.0, -3*e*i/l**3, -3 * e * i / l ** 2, 0.0, 3*e*i/l**3, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], dtype=float)


def matriz_rigidezAA(e=0.0, l=0.0, b=0.0, h=0.0):
    a = b * h
    return np.matrix([
        [e*a/l, 0.0, 0.0, -e*a/l, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [-e*a/l, 0.0, 0.0, e*a/l, 0, 0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], dtype=float)


def calcular(request):
    matrices_de_rigidez = []
    if request.method == 'POST':
        elementos = int(request.POST['cantidadElementos'])
        nodos = int(request.POST['cantidadNodos'])
        listaElementos = []
        for e in range(elementos):
            listaElementos.append([request.POST['elemento' + str(e + 1) + 'b'],
            request.POST['elemento' + str(e + 1) + 'h'], request.POST['elemento'
            + str(e + 1) + 'e'], request.POST['elemento' + str(e + 1) + 'l'],
            request.POST['elemento' + str(e + 1) + 'g']])
            mr = matriz_rotacion(float(request.POST['elemento' + str(e + 1) + 'g']))
            condicion = request.POST['condicionRigidez' + str(e + 1)]
            if condicion == 'ee':
                mri = matriz_rigidezEE(float(request.POST['elemento'+ str(e + 1) + 'e']),float(request.POST['elemento' + str(e + 1) + 'l'])
                , float(request.POST['elemento' + str(e + 1) + 'b']), float(request.POST['elemento' + str(e + 1) + 'h']))
                matrices_de_rigidez.append(mr*mri*np.transpose(mr))
            if condicion == 'ea':
                mri = matriz_rigidezEA(float(request.POST['elemento'+ str(e + 1) + 'e']),float(request.POST['elemento' + str(e + 1) + 'l'])
                , float(request.POST['elemento' + str(e + 1) + 'b']), float(request.POST['elemento' + str(e + 1) + 'h']))
                matrices_de_rigidez.append(mr*mri*np.transpose(mr))
            if condicion == 'ae':
                mri = matriz_rigidezAE(float(request.POST['elemento'+ str(e + 1) + 'e']),float(request.POST['elemento' + str(e + 1) + 'l'])
                , float(request.POST['elemento' + str(e + 1) + 'b']), float(request.POST['elemento' + str(e + 1) + 'h']))
                matrices_de_rigidez.append(mr*mri*np.transpose(mr))
            if condicion == 'aa':
                mri = matriz_rigidezAA(float(request.POST['elemento'+ str(e + 1) + 'e']),float(request.POST['elemento' + str(e + 1) + 'l'])
                , float(request.POST['elemento' + str(e + 1) + 'b']), float(request.POST['elemento' + str(e + 1) + 'h']))
                matrices_de_rigidez.append(mr*mri*np.transpose(mr))
        matriz_de_ceros = np.matlib.zeros((nodos*3, nodos*3))
        matriz_de_compatibilidad = np.matlib.zeros((elementos*6, nodos*3))
        m = 0
        n = 0
        iterador = 0
        print matrices_de_rigidez

        print "impreso matriz"
        while iterador < (nodos*3-3):
            for matriz1 in matrices_de_rigidez:
                for i in range(6):
                    for j in range(6):
                        matriz_de_ceros[[i+iterador],[j+iterador]] = float(matriz_de_ceros[[i+iterador],[j+iterador]])+float(matriz1[[i],[j]])
                        print "%d , %d"%(i,j)
                        print matriz1[[i],[j]]
                iterador = iterador+3
                print "otra matriz"
        print "Posicion 14 14"
        bucle = 0

        for e in range(elementos):
            i = int(request.POST['elemento' + str(e + 1) + 'i'])
            f = int(request.POST['elemento' + str(e + 1) + 'f'])

            matriz_de_compatibilidad[[(3*(e+1)-3)+bucle],[(3*i-2)-1]] = 1
            matriz_de_compatibilidad[[(3*(e+1)-2)+bucle],[(3*i-2)]] = 1
            matriz_de_compatibilidad[[(3*(e+1)-1)+bucle],[(3*i-2)+1]] = 1

            matriz_de_compatibilidad[[(3*(e+1)-3)+bucle+3],[(3*f-2)-1]] = 1
            matriz_de_compatibilidad[[(3*(e+1)-2)+bucle+3],[(3*f-2)]] = 1
            matriz_de_compatibilidad[[(3*(e+1)-1)+bucle+3],[(3*f-2)+1]] = 1


            bucle = bucle +3
        print matriz_de_ceros
        print matriz_de_compatibilidad
        resultado=matriz_de_compatibilidad*matriz_de_ceros*np.transpose(matriz_de_compatibilidad)
        longitudMatriz = range(6*elementos)


        for key in request.POST:
            value = request.POST[key]
    # loop through keys and values
        for key, value in request.POST.iteritems():
            print key, value
#        print matrices_de_rigidez
#        for matrizi in matriz_de_ceros:
#            print matrizi




        return render_to_response('reducir.html', locals(), context_instance=
        RequestContext(request))
#    template = loader.get_template('calculo/index.html')
#    return HttpResponse(template.render())
#    html = get_template('index.html')
#    return HttpResponse(html)
# Create your views here.
