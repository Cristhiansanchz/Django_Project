from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registrar_egresado', views.registrar_egresado, name='registrar_egresado'),
    path('listar_egresado', views.listar_egresado, name='listar_egresado'),
    path('editar_egresado/<int:id>', views.editar_egresado, name="editar_egresado"),
    path('export_excel', views.export_excel, name="export_excel")
]

