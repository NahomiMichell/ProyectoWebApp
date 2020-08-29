from django.shortcuts import render
from contacto.models import Contacto
from contacto.forms import FormularioContactoR

# Create your views here.
def contacto (request):
    contacto = Contacto.objects.all()
   # if request.method == "POST":
        #formularioCR = FormularioContactoR(request.POST)

        #if formularioCR.is_valid():
            #inFormR = formularioCR.cleaned_data
            #send_database(inFormR['nombre'],inFormR['direccion'], inFormR['telefono'],inFormR['email'])
           # return print("hola")
   # else:
       # formularioCR = FormularioContactoR()
    return render(request, "contacto/contacto.html", {"contacto":contacto})