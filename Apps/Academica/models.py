from django.db import models

# Create your models here.

class Nivel_Educativo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = "Nivel_Educativo"

class Titulo(models.Model):
    nombre = models.CharField(max_length=100)
    nivel_educativo = models.ForeignKey(Nivel_Educativo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = "Titulo"


class Modalidad(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = "Modalidad"


class Territorial(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = "Territorial"


class Cetap(models.Model):
    nombre = models.CharField(max_length=50)
    territorial = models.ForeignKey(Territorial, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = "Cetap"

class Egresado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.CharField(max_length=10, unique=True)
    email_personal = models.EmailField(max_length=50, unique=True)
    email_institucional = models.EmailField(max_length=50, unique=True)
    celular = models.CharField(max_length=10, unique=True)
    fecha_grado = models.DateField()
    nivel_educativo = models.ForeignKey(Nivel_Educativo, on_delete=models.CASCADE)
    titulo = models.ForeignKey(Titulo, on_delete=models.CASCADE)
    modalidad = models.ForeignKey(Modalidad, on_delete=models.CASCADE)
    territorial = models.ForeignKey(Territorial, on_delete=models.CASCADE)
    cetap = models.ForeignKey(Cetap, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = "Egresado"

