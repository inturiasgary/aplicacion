
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def matriz(request):
    
    if 'q' in request.GET and request.GET['q]:
        mensaje = "lo logramos"
    else:
        mensaje = "No logrado"
    return HttpResponse(mensaje)
