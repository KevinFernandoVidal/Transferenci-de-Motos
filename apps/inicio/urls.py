from django.urls import path
from .views import *
urlpatterns = [
    path('', inicio_view, name='inicio'),
    #seccion autentificacion
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registro/', registro_view, name='registro'),
   
    #seccion nmoto
    path('mis_motos/', mis_moto_view, name='mis_motos'),
    path('moto_agregar/', moto_agregar_view, name='moto_agregar'),
    path('moto_editar/<int:id_moto>/', moto_editar_view, name='moto_editar'),
    path('moto_eliminar/<int:id_moto>/', moto_eliminar_view, name='moto_eliminar'),
    path('moto_detalles/<int:id_moto>/', moto_detalles_view, name='moto_detalles'),

    #seccion mantenimiento
    path('mantenimiento/<int:id_moto>/', mantenimiento, name='mantenimiento'),
    path('mantenimiento_agregar/<int:id_moto>/', mantenimiento_agregar_view, name='mantenimiento_agregar'),
    path('manteniento_editar/<int:id_mantenimiento>/', mantenimiento_editar_view, name='mantenimiento_editar'),
    path('mantenimiento_eliminar/<int:id_mantenimiento>/', mantenimiento_eliminar_view, name='mantenimiento_eliminar'),
    path('mantenimiento_detalles/<int:id_mantenimiento>/', mantenimiento_detalles_view, name='mantenimiento_detalles'),
    
    #seccion de trasferencia
    # path('trasferencia/', trasferencia_view, name='trasferencia'),
    # path('trasferencia_moto/<int:id_moto>', trasferencia_view, name='trasferencia_moto'),
    # path('trasferencia_aceptar/', trasferencia_view, name='trasferencia_aceptar'),
]