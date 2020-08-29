from django.shortcuts import render
from .forms import Fcontacto


# Create your views here.
def home (request):
    if request.method == "POST":
        formularioC = Fcontacto(request.POST)

        if formularioC.is_valid():
            inForm = formularioC.cleaned_data
            send_mail(inForm['asunto'],inForm['mensaje'], inForm['email'], ['nahomimichell14@gmail.com'])
            return 
    else:
        formularioC = Fcontacto()
    return render(request, "ProyectoAdopApp/home.html", {"form": Fcontacto})




