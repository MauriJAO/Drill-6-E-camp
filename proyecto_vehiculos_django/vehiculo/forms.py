from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#
from .models import VehiculoModel

class Inputform(forms.Form):
    nombres = forms.CharField(max_length=200)
    apellidos = forms.CharField(max_length=200)
    contraseña = forms.CharField(widget= forms.PasswordInput)

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    OPCIONES_ROL = (
        ('vendedor', 'Vendedor'),
        ('comprador', 'Comprador'),
    )
    rol = forms.ChoiceField(
        choices=OPCIONES_ROL,
        widget=forms.RadioSelect,
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(RegistroUsuarioForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = VehiculoModel
        fields = '__all__'