from datetime import datetime
from fileinput import filename
from urllib import response
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse
from django.db import IntegrityError

import xlwt

from .models import Egresado
from .forms import EgresadoForm

# Create your views here.

# Home

@login_required
def home(request):
    return render (request, "home.html")

# Registrar Egresado

@permission_required('Academica.add_egresado')
def registrar_egresado(request):

    form = EgresadoForm()

    if request.method == "POST":

        form = EgresadoForm(request.POST)

        if form.is_valid():

            egresado = Egresado()

            egresado.nombre = form.cleaned_data['nombre']
            egresado.apellido = form.cleaned_data['apellido']
            egresado.cedula = form.cleaned_data['cedula']
            egresado.email_personal = form.cleaned_data['email_personal']
            egresado.email_institucional = form.cleaned_data['email_institucional']
            egresado.celular = form.cleaned_data['celular']
            egresado.fecha_grado = form.cleaned_data['fecha_grado']
            egresado.nivel_educativo = form.cleaned_data['nivel_educativo']
            egresado.titulo = form.cleaned_data['titulo']
            egresado.modalidad = form.cleaned_data['modalidad']
            egresado.territorial = form.cleaned_data['territorial']
            egresado.cetap = form.cleaned_data['cetap']
            
            egresado.save()

            messages.success(request, "Egresado Registrado correctamente")
           
    return render (request, "registrar_egresado.html", {'form' : form})

# Listar Egresado

@login_required
def listar_egresado(request):

    busqueda = request.GET.get("buscar")

    listaEgresados = Egresado.objects.all().order_by('nombre')

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(listaEgresados, 8)
        listaEgresados = paginator.page(page)
    except:
        raise Http404

    if busqueda:
        listaEgresados = Egresado.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(apellido__icontains = busqueda) |
            Q(cedula__icontains = busqueda) |
            Q(email_personal__icontains = busqueda) |
            Q(email_institucional__icontains = busqueda) |
            Q(celular__icontains = busqueda) |
            Q(fecha_grado__icontains = busqueda) |
            Q(nivel_educativo__nombre__icontains = busqueda) |
            Q(titulo__nombre__icontains = busqueda) |
            Q(modalidad__nombre__icontains = busqueda) |
            Q(territorial__nombre__icontains = busqueda) |
            Q(cetap__nombre__icontains = busqueda)
        ).distinct()
        

    return render (request, "listar_egresado.html", {"egresados" : listaEgresados, "paginator" : paginator})


# Editar Egresado

@permission_required('Academica.change_egresado')
def editar_egresado(request, id):
    
    egresado = get_object_or_404(Egresado, id=id)

    form = EgresadoForm(initial={'nombre' : egresado.nombre, 'apellido' : egresado.apellido, 'cedula' : egresado.cedula, 
    'email_personal' : egresado.email_personal, 'email_institucional' : egresado.email_institucional, 'celular' : egresado.celular, 
    'fecha_grado' : egresado.fecha_grado, 'nivel_educativo' : egresado.nivel_educativo, 'titulo' : egresado.titulo, 'modalidad' : egresado.modalidad, 
    'territorial' : egresado.territorial, 'cetap' : egresado.cetap})

    if request.method == "POST":

        form = EgresadoForm(request.POST)

        if form.is_valid():

            egresado.nombre = form.cleaned_data['nombre']
            egresado.apellido = form.cleaned_data['apellido']
            egresado.cedula = form.cleaned_data['cedula']
            egresado.email_personal = form.cleaned_data['email_personal']
            egresado.email_institucional = form.cleaned_data['email_institucional']
            egresado.celular = form.cleaned_data['celular']
            egresado.fecha_grado = form.cleaned_data['fecha_grado']
            egresado.nivel_educativo = form.cleaned_data['nivel_educativo']
            egresado.titulo = form.cleaned_data['titulo']
            egresado.modalidad = form.cleaned_data['modalidad']
            egresado.territorial = form.cleaned_data['territorial']
            egresado.cetap = form.cleaned_data['cetap']
        
            egresado.save()

            messages.success(request, "Egresado Modificado correctamente")

    return render(request, 'editar_egresado.html', {'form' : form})

    # Exportar data a Excel

def export_excel(request):
    response=HttpResponse(content_type='applications/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Egresados' + \
        str()+'.xls'
    
    wb = xlwt.Workbook(encoding='UTF-8')
    ws = wb.add_sheet('Egresados')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns=['Nombre', 'Apellido', 'Cedula', 'Email_personal', 'Email_institucional', 'Celular', 'Fecha Grado',
    'Nivel Educativo', 'Titulo', 'Modalidad', 'Territorial', 'Cetap']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = Egresado.objects.all().values_list('nombre', 'apellido', 'cedula', 'email_personal',
    'email_institucional', 'celular', 'fecha_grado', 'nivel_educativo__nombre', 'titulo__nombre', 'modalidad__nombre', 'territorial__nombre', 'cetap__nombre')

    for row in rows:
        row_num+=1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    
    wb.save(response)

    return response

