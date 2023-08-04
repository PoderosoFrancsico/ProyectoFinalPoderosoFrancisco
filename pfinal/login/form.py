from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User



class UserRegisterForm(UserCreationForm): 
    email=forms.EmailField()
    password1=forms.CharField(label='Indique contraseña', widget= forms.PasswordInput)
    password2=forms.CharField(label='Repita la contraseña', widget= forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2', 'last_name', 'first_name' ]
        help_text = { k:'' for k in fields}