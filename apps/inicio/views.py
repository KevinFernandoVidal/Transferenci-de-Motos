from django.core.checks import messages
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate

from .models import *
from .forms import *

# Create your views here.

def inicio_view(request):
    lista = Moto.objects.filter()
    return render(request, 'inicio/inicio.html',locals())

def login_view (request):
    usu = ""
    cla = ""
    if request.method == 'POST':
        form_l = login_form(request.POST)
        if form_l.is_valid():
            usu = form_l.cleaned_data['usuario']
            cla = form_l.cleaned_data['clave']
            usuario = authenticate(email=usu,password=cla)
            if usuario is not None and usuario.is_active:
                login(request, usuario)
                return redirect('inicio')
            else:
                messages.Error(request, "Error en el usuario o clave")
    form_l = login_form()
    return render(request, 'inicio/login.html',locals())

def logout_view (request):
    logout(request)
    return redirect('login/')

def registro_view(request):
    form_r =register_from()
    if request.method == 'POST':
        form_r = register_from(request.POST)
        if form_r.is_valid():
            # apodo     = form_r.cleaned_data['apodo']
            # nombre    = form_r.cleaned_data['nombre']
            # apellido  = form_r.cleaned_data['apellido']
            # email     = form_r.cleaned_data['email']
            form_r.save()
            email     = form_r.cleaned_data['email']
            password     = form_r.cleaned_data['password1']
            account = authenticate(email=email, password=password)
            login(request, account)
            return redirect('inicio')
        else:
            return render(request,'inicio/registro.html/', locals())
    return render(request, 'inicio/registro.html', locals())



def moto_agregar_view(request): 
    if request.method == 'POST':
        form_m = agregar_moto_form(request.POST, request.FILES)
        if form_m.is_valid():
            form_m.save()
            #h = Historia.objects.create(moto=moto, usuario=, estado='Pendiente')
            return redirect('inicio/inicio.html/')
    return render(request, 'inicio/moto_agregar.html',)

def moto_editar_view(request,id_moto):
    moto = Moto.objects.get(id = id_moto)
    if request.method == 'GET':
        form_edit_moto = mantenimiento_form(instance=moto) 
        if form_edit_moto.is_valid():
            form_edit_moto.save()
            return redirect('inicio/inicio.html')
    else:
        form_edit_moto = mantenimiento_form()
    return render(request,'inicio/moto_editar.html', locals())
    
def mis_moto_view(request):
    usu = Usuario.objects.get(id = request.Usuario.id)
    list = Historia.objects.filter(usuario = usu, propiedad='Propietario')
    return render(request, 'inicio/mis_moto.html', locals())

def moto_eliminar_view(request, id_moto):
    moto = Moto.objects.get(id =  id_moto)
    moto.delete()
    return redirect('inicio/inicio.html')

def moto_detalles_view(request,id_moto): 
    moto=Moto.objects.get(id =id_moto)
    return render(request, 'inicio/moto_ver.html',locals())

def mantenimiento(request, id_moto):
    mantenimiento= Mantenimiento.objects.filter(moto = id_moto)
    return render(request, 'inicio/mantenimiento.html',locals())

def mantenimiento_agregar_view(request):
    if request.method == 'POST':
        form_add_mant = mantenimiento_form(request.POST)
        if form_add_mant.is_valid():
            form_add_mant.save()
            return redirect('inicio/inicio.html')
    else:
        form_add_mant =mantenimiento_form()
    return render(request, 'inicio/moto_mantenimiento')   

def mantenimiento_editar_view(request,id):
    mantenimiento = Mantenimiento.objects.get(id)
    if request.method == 'GET':
        form_edit_mant = mantenimiento_form(instance=mantenimiento) 
        if form_edit_mant.is_valid():
            form_edit_mant.save()
            return redirect('inicio/inicio.html')
    else:
        form_edit_mant = mantenimiento_form()
    return render(request,'inicio/editar_mantenimiento', locals())

def mantenimiento_eliminar_view(request,id_mantenimiento):
    mantenimiento = Mantenimiento.objects.get(id = id_mantenimiento)
    mantenimiento.delete()
    return redirect('inicio/inicio.html')

def mantenimiento_detalles_view(request, id_moto):
    mantenimiento = Mantenimiento.objects.filter(moto= id_moto)
    return render(request, 'inicio/mantenimiento_detalles.html',locals())

def moto_venta_view(request):
    if request.method == 'POST':
        form_venta = trasferencia_form(request.POST)
        if form_venta.is_valid():
            nombre   = form_venta.cleaned_data['nombre']
            moto     = form_venta.cleaned_data['moto']
            h = Historia.objects.create(moto=moto, usuario=nombre, estado='Pendiente')
            return redirect('mis_motos')
    return render(request,'inicio/moto_venta.html')     
