from unittest.util import _MAX_LENGTH
import datetime
from django import forms

from .models import Nivel_Educativo, Titulo, Modalidad, Territorial, Cetap, Egresado

class EgresadoForm(forms.Form):
    nombre = forms.CharField(label="Nombres", min_length=5, max_length=50, required=True)
    apellido = forms.CharField(label="Apellidos", min_length=5, max_length=50, required=True)
    cedula = forms.CharField(label="Documento", min_length=7, max_length=10, required=True)
    email_personal = forms.EmailField(label="Email Personal", max_length=50, required=True)
    email_institucional = forms.EmailField(label="Email Institucional", max_length=50, required=True)
    celular = forms.CharField(label="Celular", min_length=10, max_length=10, required=True)
    fecha_grado = forms.DateField(label="Fecha Grado", required=True, initial=datetime.date.today)
    nivel_educativo = forms.ModelChoiceField(label="Nivel Educativo", queryset=Nivel_Educativo.objects.all())
    titulo = forms.ModelChoiceField(label="Titulo", queryset=Titulo.objects.all())
    modalidad = forms.ModelChoiceField(label="Modalidad", queryset=Modalidad.objects.all())
    territorial = forms.ModelChoiceField(label="Territorial", queryset=Territorial.objects.all())
    cetap = forms.ModelChoiceField(label="Cetap", queryset=Cetap.objects.all())

    


