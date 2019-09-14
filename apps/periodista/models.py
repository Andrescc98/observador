from django.db import models

class Periodista(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30, blank=True)
    correo=models.EmailField()
    descripcion=models.TextField()

    def __str__(self):
        return '%s %s' %(self.nombre,self.apellido)

    