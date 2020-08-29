from django import forms

class FormularioContactoR(forms.Form):
    nombre = forms.CharField()
    direccion = forms.CharField()
    telefono = forms.CharField()
    email = forms.EmailField()
