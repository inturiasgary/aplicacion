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


#    template = loader.get_template('calculo/index.html')
    return render_to_response('index.html', {'matriza':a,'matrizb':b,'resultado': resultado})
#    return HttpResponse(template.render())
#    html = get_template('index.html')
#    return HttpResponse(html)
# Create your views here.