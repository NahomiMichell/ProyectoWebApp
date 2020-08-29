from django.urls import path
from ProyectoAdopApp import views

urlpatterns = [
    path('', views.home, name = "Home"),
]
