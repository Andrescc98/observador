from django.db import models
from apps.periodista.models import Periodista

class Categoria(models.Model):
    categoria=models.CharField(max_length=40)

    def __str__(self):
        return '%s'%self.categoria

class Articulo(models.Model):
    Periodista=models.ForeignKey(Periodista, on_delete=models.CASCADE)
    titulo=models.CharField(max_length=50)
    contenido=models.TextField()
    f_publicacion=models.DateTimeField(auto_now=True)
    Categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen=models.ImageField( upload_to='imagen_articulo', default='default_img.png', blank=True)
    
    def __str__(self):
        return '%s %s %s'%(self.titulo, self.Periodista, self.f_publicacion)