from django import forms


class UsuariosFormulario(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField()