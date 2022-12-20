from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class FormularioRegistro(UserCreationForm):
    
    email = forms.EmailField(label='e-mail') 
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_text = {key: '' for key in fields}
        
        
class FormularioEditarPerfil(forms.Form):
    email = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField(required=False)
    avatar = forms.ImageField(required=False)
    descripcion = forms.CharField()