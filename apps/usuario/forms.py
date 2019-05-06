from django import forms
from .models import *

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")

class LoginForm(forms.Form):
    name_user = forms.CharField(max_length=20, required=True, label="",
                                widget=(forms.TextInput(attrs={"placeholder":"Nombre del Usuario", "class":"input-login"})))
    password_user = forms.CharField(max_length=20, required=True, label="",
                                    widget=(forms.PasswordInput(attrs={"placeholder":"Contrasena","class":"input-login"})))

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ("Telefono", "Calle", "Colonia", "CodigoPostal", "Municipio", "Estado", "Pais")
