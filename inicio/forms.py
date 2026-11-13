from django import forms
from .models import Profesor

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'dni', 'domicilio', 'legajo', 'especialidad']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Ej. Juan Pérez'
            }),
            'dni': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Ej. 35123456'
            }),
            'domicilio': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Ej. Av. Siempre Viva 742'
            }),
            'legajo': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Ej. LEG-1042'
            }),
            'especialidad': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Ej. Programación Web / Algoritmos'
            }),
        }
