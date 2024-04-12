# tienda/views.py

from django.shortcuts import render
from .models import Producto, Opiniones

def home(request):
    productos = Producto.objects.all()
    return render(request, 'home.html', {'productos': productos})

def opiniones(request):
    opiniones = Opiniones.objects.all()
    return render(request, 'opiniones.html', {'opiniones': opiniones})
