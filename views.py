from django.http import HttpResponse
from django.shortcuts import render

import Auto
from Auto.models

# Create your views here.
def Auto_list (request):
    # mensajes = {'msg1': 'valor mensaje 1', 'msg2': 'valor mensaje 2'}
    no_autos = Auto.objects.count()
    autos = Auto.objects.all()
    # return render (request, 'autos.html', {'msg1': 'valor mensaje 1', 'msg2': 'valor mensaje 2'})
    return render(request, 'autos.html', {'no_autos': no_autos, 'autos': autos})
