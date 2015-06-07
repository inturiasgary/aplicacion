from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.template.loader import get_template


def index(request):
    from random import randint
    import numpy as np
    '''a = np.array([[36. , 51., 13. ],
           [52. , 34., 74. ],
           [ 0. , 7.,  1.1]])
    b = np.array([ 3., 45., 33.])'''
    n = 48
    m = 48
    a1 = []

    for i in range(n):
        a1.append([randint(0,1000) for i in range(m)])
    b = []
    a = []
    a = np.array(a1)
    b1 =[]
    for i in range(1):
        for j in range(m):
           b1.append(randint(0,100))
    b = np.array(b1)
    x = np.linalg.solve(a,b)
    resultado = x.tolist()
    return render_to_response('index.html', {'matriza':a,'matrizb':b,'resultado': resultado})

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

def calcular(request):
    if request.method == 'POST':
        elementos = int(request.POST['cantidadElementos'])
        listaElementos = []
        for e in range(elementos):
            listaElementos.append([request.POST['elemento'+str(e+1)+'b'], request.POST['elemento'+str(e+1)+'h'], request.POST['elemento'+str(e+1)+'e'], request.POST['elemento'+str(e+1)+'l'], request.POST['elemento'+str(e+1)+'g']])
        for key in request.POST:
            value = request.POST[key]
            # loop through keys and values
            print key, value
        print listaElementos
        print listaElementos[0]
        return render_to_response('index.html',locals(), context_instance=RequestContext(request))
#    template = loader.get_template('calculo/index.html')
#    return HttpResponse(template.render())
#    html = get_template('index.html')
#    return HttpResponse(html)
# Create your views here.
