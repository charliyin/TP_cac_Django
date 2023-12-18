from django.db import models

# Create your models here.
class Trabajador (models.Model):
    nombre= models.TextField(max_length=50)
    legajo= models.IntegerField(blank=True, null=True)
    titulo= models.CharField(max_length=50)
    contenido= models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='trabajadores')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='trabajador'
        verbose_name_plural='trabajadores'

    def __str__(self):
        return self.titulo