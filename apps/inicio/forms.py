
from django import forms
from django.core.exceptions import ValidationError 
from django.contrib.auth.forms import UserCreationForm
from .models import *
class agregar_moto_form(forms.ModelForm):
    class Meta:
        model = Moto
        fields = '__all__'
 
class mantenimiento_form(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = '__all__'
 
class login_form(forms.Form):
   usuario = forms.CharField(widget=forms.EmailInput)
   clave  = forms.CharField(widget=forms.PasswordInput)
 
class trasferencia_form(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput)
    moto   = forms.CharField(widget=forms.TextInput)
 
class register_from(UserCreationForm): 
    
    class Meta:
        model = Usuario
        fields = 'apodo', 'nombre', 'apellido', 'email', 'password1', 'password2'

        def clean_nombre(self):
            nombre = self.cleaned_data['nombre']
            if len(nombre) > 3:
                return nombre
            else:
                raise forms.ValidationError('nombre muy corto')
        
        def clean_apellido(self):
            apellido = self.cleaned_data['apellido']
            if len(apellido) > 3:
                return apellido
            else:
                raise forms.ValidationError('apellido muy corto')

        def clean_apodo(self):
            apodo = self.cleaned_data['apodo']
            try:
                u = Usuario.objects.get(apodo=apodo)
            except Usuario.DoesNotExist:
                return apodo
            raise forms.ValidationError('Apodo ya registrado')

        def clean_email(self):
            email = self.cleaned_data['email']
            try:
                u = Usuario.objects.get(email = email)
            except Usuario.DoesNotExist:
                return email
            raise forms.ValidationError('Email ya registrado')

        # def clean_clave (self):
        #     clave  = self.cleaned_data['clave']
        #     clave1 = self.cleaned_data['clave1']
        #     if len(clave) <6 and len(clave1)<6:
        #         raise forms.ValidationError ('La contraseña bede tener mas de 6 caracteres')
        #     else:
        #         if clave == clave1:
        #             return clave
        #         else:
        #             raise forms.ValidationError ('las claves no coinciden')

        
 
