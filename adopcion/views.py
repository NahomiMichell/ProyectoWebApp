from django.shortcuts import render
from adopcion.models import Adopcion

# Create your views here.
def adopcion (request):
    adopcion= Adopcion.objects.all()
    return render(request, "adopcion/adopcion.html", {"adopcion":adopcion})