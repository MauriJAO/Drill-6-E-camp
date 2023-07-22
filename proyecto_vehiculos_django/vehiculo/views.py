from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Inputform, RegistroUsuarioForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from tokenize import PseudoExtras
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group

#
from .forms import VehiculoForm
from .models import VehiculoModel
# Create your views here.

class IndexPageView(TemplateView):
    template_name = 'base.html'


def menuView(request):
    context = {}
    return render(request, 'menu.html', context)

def registerView(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            rol = form.cleaned_data.get('rol')
            if rol == 'vendedor':
                group = Group.objects.get(name='vendedor')
                user.is_staff = True
            else:
                group = Group.objects.get(name='comprador')

            user.groups.add(group)
            user.save()
            login(request, user)
            messages.success(request, "Registrado Satisfactoriamente")
            return HttpResponseRedirect('/')
        messages.error(request, "Registro invalido, Algunos datos ingresados no son correctos")
    form = RegistroUsuarioForm()
    context = { "register_form": form}
    return render(request, "register.html", context)

def loginView(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Iniciaste sesión como: {username}.")
                return HttpResponseRedirect('/')
            else:
                messages.error(request, "Invalid username o password.")

    form = AuthenticationForm()
    context = {"login_form": form}
    return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    messages.info(request, "Se ha cerrado la sesión satisfactoriamente.")
    return HttpResponseRedirect('/')


@login_required(login_url='/login/')
@permission_required('vehiculo.adds_vehiculomodel',login_url='/login/')
def add_view(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = VehiculoForm()
    context = {'form': form}
    return render(request, 'add.html', context)

@login_required(login_url='/login/')
@permission_required('vehiculo.visualizar_catalogo', login_url='/login/')
def listar_vehiculos(request):
    vehiculos = VehiculoModel.objects.all()
    context = {'vehiculos': vehiculos}
    return render(request, 'list.html', context)
